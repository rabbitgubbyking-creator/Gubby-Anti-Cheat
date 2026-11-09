# Detection and Shared Ban Policy

## Authority

The shared anti-cheat service is the sole authority for shared ban state. Lobby hosts may view a player's status but cannot issue, revoke, or override a shared ban.

A lobby may still apply its own local moderation rules. Local actions must never be represented as shared anti-cheat bans.

## Evidence requirements

A report must include:
- A pseudonymous mod-issued player identifier.
- Lobby and adapter version identifiers.
- A known detection rule identifier.
- A sequence of server-verifiable events sufficient to reproduce the rule decision.
- A timestamp and unique report identifier.

Do not accept a client claim such as "this player is hacking" as evidence. Do not collect real names, phone numbers, precise location, or unrelated device data.

## Decision levels

- **Observation:** suspicious but not conclusive. Log only.
- **Temporary restriction:** repeated, independently verified suspicious behavior. Prevent entry to participating lobbies for a short period while the evidence is checked.
- **Confirmed shared ban:** only deterministic, high-confidence evidence from a trusted compatible lobby adapter. Apply across participating lobbies and record the exact rule and evidence reference.

A permanent or long-duration ban must never be triggered by a single unverified client report or a statistical anomaly alone.

## Integrity protections

- Authenticate lobby adapters.
- Sign reports and reject invalid signatures.
- Reject duplicate report IDs and replayed event sequences.
- Apply rate limits and abuse monitoring.
- Keep an append-only audit trail for ban decisions.
- Use expiry timestamps and a documented review/correction process.

## Privacy

Use pseudonymous identifiers scoped to this mod ecosystem. Store only the minimum event evidence needed to explain and validate a decision. Publish a retention period before collecting real player data.

## Compatibility boundary

Only participating modded lobbies that query this service can enforce its decisions. This service cannot ban players from ordinary official Among Us servers.
