# Gubby Anti-Cheat

A defensive anti-cheat and community-safety project for compatible, community-run Among Us modded lobbies.

## Current scope

- No host-controlled global bans.
- Shared decisions are made by the service, not by an individual lobby host.
- Only compatible lobbies that check the shared service can enforce shared restrictions.
- The system must not modify or interfere with ordinary official Among Us servers.
- No cheats, wallhacks, role reveals, noclip, or gameplay advantages are part of this project.
- Gameplay cheating and community-conduct moderation use separate rule categories and evidence standards.

## Architecture

1. **Lobby adapter** collects only events the compatible lobby can authoritatively verify.
2. **Detection engine** evaluates impossible or inconsistent gameplay events.
3. **Safety report flow** accepts reports about harmful conduct, with privacy safeguards and human review for serious cases.
4. **Evidence record** stores the rule triggered, event sequence or evidence reference, build/version, and confidence.
5. **Ban service** makes shared decisions. Lobby hosts cannot create or remove global restrictions.
6. **Service activation check** asks the service whether a player is restricted before enabling Gubby Anti-Cheat features; it does not block ordinary game or lobby access.
7. **Android companion app** displays match logs, report status, explanations, and ban status. It does not need to patch the official game.

## Planned features

See [Planned In-Game Settings and Lobby Features](docs/PLANNED_FEATURES.md) for proposed dark chat mode, frame-rate and graphics settings, automatic chat translation, host-configurable minimum account level, AFK message-before-observer mode, saved presets, lobby filters, reconnect support, and other ideas. These are plans only, not implemented features.

See [Community Requests](docs/COMMUNITY_REQUESTS.md) for a dated summary of player suggestions, and [Android Build Status](docs/ANDROID_BUILD_STATUS.md) for the current APK prerequisites and exact build status.

## Anti-false-positive policy

- A client-side suspicion alone is never enough for a permanent gameplay-cheat ban.
- Prefer server-verified evidence and deterministic rules.
- Low-confidence cases are logged or temporarily restricted, not permanently banned.
- Serious conduct reports require review by trained moderators; automated text filters may flag content but must not be the sole basis for a permanent shared ban.
- Every decision records a reason code, evidence reference, decision time, expiry, and review path.
- The service must rate-limit reports and reject forged or replayed evidence.
- Never store or redistribute illegal sexual imagery. For reports involving possible child sexual exploitation, preserve only the minimum safe metadata needed for escalation and follow applicable platform/legal reporting procedures.

## Development stages

1. Write and test the detection and community-safety policies.
2. Define a signed lobby-event and safety-report format.
3. Build a small ban-service API and database.
4. Build a test lobby adapter and automated tests.
5. Build the Android companion interface.
6. Package and test only after a compatible lobby integration exists.

## Important limitation

This repository is an early project scaffold. It is not a working APK or a functioning Among Us integration yet. Shared decisions cannot affect ordinary official lobbies.
