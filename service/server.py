#!/usr/bin/env python3
"""Minimal shared anti-cheat report API. Python 3.11+, standard library only.

This first version records authenticated reports for review. It deliberately
does NOT automatically ban players: detection rules and lobby adapters must
be independently validated before enforcement is enabled.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import sqlite3
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

DB_PATH = os.environ.get("GAC_DB_PATH", "gac.sqlite3")
HOST = os.environ.get("GAC_HOST", "127.0.0.1")
PORT = int(os.environ.get("GAC_PORT", "8080"))
MAX_BODY = 16_384
CLOCK_SKEW_SECONDS = 180
ID_RE = re.compile(r"^[a-zA-Z0-9_-]{8,80}$")
RULE_RE = re.compile(r"^[A-Z][A-Z0-9_]{2,63}$")


def load_adapter_keys() -> dict[str, str]:
    raw = os.environ.get("GAC_ADAPTER_KEYS", "{}")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError("GAC_ADAPTER_KEYS must be a JSON object") from exc
    if not isinstance(data, dict) or not all(
        isinstance(k, str) and isinstance(v, str) and len(v) >= 32
        for k, v in data.items()
    ):
        raise RuntimeError("Each adapter key must be a string of at least 32 characters")
    return data


ADAPTER_KEYS = load_adapter_keys()


def connect_db() -> sqlite3.Connection:
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            report_id TEXT PRIMARY KEY,
            player_id TEXT NOT NULL,
            adapter_id TEXT NOT NULL,
            rule_id TEXT NOT NULL,
            evidence_ref TEXT NOT NULL,
            occurred_at INTEGER NOT NULL,
            received_at INTEGER NOT NULL,
            review_state TEXT NOT NULL DEFAULT 'pending'
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS used_nonces (
            adapter_id TEXT NOT NULL,
            nonce TEXT NOT NULL,
            seen_at INTEGER NOT NULL,
            PRIMARY KEY(adapter_id, nonce)
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS shared_bans (
            player_id TEXT PRIMARY KEY,
            reason_code TEXT NOT NULL,
            evidence_ref TEXT NOT NULL,
            created_at INTEGER NOT NULL,
            expires_at INTEGER
        )
    """)
    db.commit()
    return db


def player_key(value: str) -> str:
    """Store a one-way pseudonymous lookup key, not the supplied identifier."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class Handler(BaseHTTPRequestHandler):
    server_version = "GACReportAPI/0.1"

    def send_json(self, code: int, data: dict) -> None:
        payload = json.dumps(data, separators=(",", ":")).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/health":
            self.send_json(200, {"ok": True, "service": "gubby-anti-cheat-report-api", "enforcement": "disabled"})
            return
        if path.startswith("/v1/status/"):
            supplied_id = path.rsplit("/", 1)[-1]
            if not ID_RE.fullmatch(supplied_id):
                self.send_json(400, {"error": "invalid_player_id"})
                return
            now = int(time.time())
            with connect_db() as db:
                row = db.execute(
                    "SELECT reason_code, evidence_ref, expires_at FROM shared_bans WHERE player_id=?",
                    (player_key(supplied_id),),
                ).fetchone()
            if row and (row["expires_at"] is None or row["expires_at"] > now):
                self.send_json(200, {"status": "confirmed_shared_ban", "reason": row["reason_code"], "evidence_ref": row["evidence_ref"]})
            else:
                self.send_json(200, {"status": "not_banned"})
            return
        self.send_json(404, {"error": "not_found"})

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/v1/reports":
            self.send_json(404, {"error": "not_found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json(400, {"error": "invalid_content_length"})
            return
        if length < 1 or length > MAX_BODY:
            self.send_json(413, {"error": "body_size_invalid"})
            return
        body = self.rfile.read(length)
        adapter_id = self.headers.get("X-GAC-Adapter", "")
        timestamp = self.headers.get("X-GAC-Timestamp", "")
        nonce = self.headers.get("X-GAC-Nonce", "")
        signature = self.headers.get("X-GAC-Signature", "")
        secret = ADAPTER_KEYS.get(adapter_id)
        if not secret or not timestamp.isdigit() or not re.fullmatch(r"[a-f0-9]{32}", nonce):
            self.send_json(401, {"error": "adapter_authentication_failed"})
            return
        now = int(time.time())
        if abs(now - int(timestamp)) > CLOCK_SKEW_SECONDS:
            self.send_json(401, {"error": "request_expired"})
            return
        signed = timestamp.encode() + b"\n" + nonce.encode() + b"\n" + body
        expected = hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, signature):
            self.send_json(401, {"error": "invalid_signature"})
            return
        try:
            item = json.loads(body)
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_json(400, {"error": "invalid_json"})
            return
        required = {"report_id", "player_id", "rule_id", "evidence_ref", "occurred_at"}
        if not isinstance(item, dict) or not required.issubset(item):
            self.send_json(400, {"error": "missing_fields"})
            return
        if (
            not isinstance(item["report_id"], str) or not ID_RE.fullmatch(item["report_id"])
            or not isinstance(item["player_id"], str) or not ID_RE.fullmatch(item["player_id"])
            or not isinstance(item["rule_id"], str) or not RULE_RE.fullmatch(item["rule_id"])
            or not isinstance(item["evidence_ref"], str) or not ID_RE.fullmatch(item["evidence_ref"])
            or not isinstance(item["occurred_at"], int)
            or abs(now - item["occurred_at"]) > 86_400
        ):
            self.send_json(400, {"error": "invalid_report"})
            return
        try:
            with connect_db() as db:
                db.execute(
                    "INSERT INTO used_nonces(adapter_id,nonce,seen_at) VALUES(?,?,?)",
                    (adapter_id, nonce, now),
                )
                db.execute(
                    """INSERT INTO reports(report_id,player_id,adapter_id,rule_id,evidence_ref,occurred_at,received_at)
                       VALUES(?,?,?,?,?,?,?)""",
                    (item["report_id"], player_key(item["player_id"]), adapter_id,
                     item["rule_id"], item["evidence_ref"], item["occurred_at"], now),
                )
                db.execute("DELETE FROM used_nonces WHERE seen_at < ?", (now - 600,))
        except sqlite3.IntegrityError:
            self.send_json(409, {"error": "duplicate_report_or_replayed_nonce"})
            return
        self.send_json(202, {
            "accepted": True,
            "review_state": "pending",
            "enforcement": "disabled",
            "message": "Report stored for review; this API does not automatically ban players."
        })

    def log_message(self, fmt: str, *args) -> None:
        # Avoid logging request bodies or player identifiers.
        super().log_message(fmt, *args)


if __name__ == "__main__":
    connect_db().close()
    print(f"GAC report API listening on {HOST}:{PORT}; enforcement is disabled")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
