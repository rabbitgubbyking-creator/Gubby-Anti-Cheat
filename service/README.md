# Gubby Anti-Cheat report API (prototype)

This is a small Python 3.11+ prototype using only the standard library. It stores authenticated lobby reports and exposes player ban-status lookups. **Automatic enforcement is intentionally disabled.** Reports remain pending; this version has no public endpoint that can issue bans.

## Run locally

```sh
cd service
export GAC_ADAPTER_KEYS='{"test-lobby":"replace-with-a-random-secret-of-at-least-32-characters"}'
python3 server.py
```

The service listens on 127.0.0.1:8080 by default. Set `GAC_HOST=0.0.0.0` only behind a properly configured HTTPS reverse proxy. Never expose this prototype directly to the public internet.

## Routes

- `GET /health` — health and enforcement state.
- `GET /v1/status/{player_id}` — returns whether a pseudonymous player ID has a confirmed shared ban.
- `POST /v1/reports` — accepts a report signed by a configured adapter.

## Signed report requests

The adapter sends these headers:

- `X-GAC-Adapter`: configured adapter ID.
- `X-GAC-Timestamp`: Unix timestamp in seconds.
- `X-GAC-Nonce`: 32 lowercase hexadecimal characters, unique per request.
- `X-GAC-Signature`: lowercase hex HMAC-SHA256 of `timestamp + newline + nonce + newline + exact_request_body`, using that adapter's secret.

Example JSON body:

```json
{
  "report_id": "report_00000001",
  "player_id": "player_0000001",
  "rule_id": "IMPOSSIBLE_MOVEMENT",
  "evidence_ref": "evidence_000001",
  "occurred_at": 1794000000
}
```

Use generated opaque IDs, not usernames, email addresses, phone numbers, or hardware identifiers. Evidence itself should remain in a controlled evidence store; send only its opaque reference.

## Important prototype limitations

- This API is not connected to Among Us yet.
- It does not verify the truth of a gameplay event; trusted adapter implementation is still required.
- Reports are stored as pending and do not trigger bans.
- The status route only reflects ban records created through a future reviewed administrative process. No ban-management route is included.
- SQLite is for local development only. A deployed service needs managed storage, HTTPS, secret rotation, backups, monitoring, and a documented appeal process.


## Planned Discord membership and restriction behavior

- Community invite: https://discord.gg/GBgmps6X6
- Discord membership is a planned prerequisite for activating the anti-cheat lobby service. The prototype does not yet verify Discord membership or link Discord accounts.
- A future secure OAuth2/bot integration must verify guild membership server-side. Never place a Discord bot token or OAuth client secret in the Android app or a public repository.
- A confirmed restriction should suspend Gubby Anti-Cheat service access only. It must not kick or disconnect the player from their own Among Us lobby or disable ordinary game features.
- The status response reports the policy reason, expiry, remaining time, and a safe chat notice. A compatible lobby adapter still needs to display that notice and privately notify the host; that adapter is not implemented yet.
