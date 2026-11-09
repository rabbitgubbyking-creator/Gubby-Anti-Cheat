import hashlib
import hmac
import json
import os
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request

SECRET = "test-secret-that-is-long-enough-for-hmac-256"
os.environ["GAC_ADAPTER_KEYS"] = json.dumps({"test-lobby": SECRET})
_tmp = tempfile.NamedTemporaryFile(delete=False)
_tmp.close()
os.environ["GAC_DB_PATH"] = _tmp.name

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import server


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = server.ThreadingHTTPServer(("127.0.0.1", 0), server.Handler)
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.httpd.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        os.unlink(_tmp.name)

    def request(self, path, body=None, headers=None):
        data = None if body is None else json.dumps(body, separators=(",", ":")).encode()
        req = urllib.request.Request(self.base + path, data=data, headers=headers or {})
        try:
            with urllib.request.urlopen(req) as response:
                return response.status, json.loads(response.read())
        except urllib.error.HTTPError as exc:
            return exc.code, json.loads(exc.read())

    def signed_headers(self, body, nonce=None):
        timestamp = str(int(time.time()))
        nonce = nonce or hashlib.md5(os.urandom(32)).hexdigest()
        raw = json.dumps(body, separators=(",", ":")).encode()
        signed = timestamp.encode() + b"\n" + nonce.encode() + b"\n" + raw
        signature = hmac.new(SECRET.encode(), signed, hashlib.sha256).hexdigest()
        return raw, {
            "Content-Type": "application/json",
            "X-GAC-Adapter": "test-lobby",
            "X-GAC-Timestamp": timestamp,
            "X-GAC-Nonce": nonce,
            "X-GAC-Signature": signature,
        }

    def test_health_disables_enforcement(self):
        status, data = self.request("/health")
        self.assertEqual(status, 200)
        self.assertEqual(data["enforcement"], "disabled")

    def test_unsigned_report_rejected(self):
        status, data = self.request("/v1/reports", {"report_id": "report_00001"})
        self.assertEqual(status, 401)
        self.assertEqual(data["error"], "adapter_authentication_failed")

    def test_signed_report_is_pending_not_banned(self):
        body = {
            "report_id": "report_00002",
            "player_id": "player_00002",
            "rule_id": "IMPOSSIBLE_MOVEMENT",
            "evidence_ref": "evidence_00002",
            "occurred_at": int(time.time()),
        }
        raw, headers = self.signed_headers(body)
        req = urllib.request.Request(self.base + "/v1/reports", data=raw, headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            self.assertEqual(response.status, 202)
        self.assertEqual(result["review_state"], "pending")
        self.assertEqual(result["enforcement"], "disabled")

    def test_status_defaults_to_not_banned(self):
        status, data = self.request("/v1/status/player_00003")
        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "not_banned")


if __name__ == "__main__":
    unittest.main()
