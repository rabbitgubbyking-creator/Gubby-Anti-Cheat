# Gubby Anti-Cheat

A defensive anti-cheat project for compatible, community-run Among Us modded lobbies.

## Current scope

- No host-controlled global bans.
- Shared ban decisions are made by the anti-cheat service, not by the lobby host.
- Only compatible lobbies that check the shared service can enforce shared bans.
- The system must not modify or interfere with ordinary official Among Us servers.
- No cheats, wallhacks, role reveals, noclip, or gameplay advantages are part of this project.

## Architecture

1. **Lobby adapter** collects only events the compatible lobby can authoritatively verify.
2. **Detection engine** evaluates impossible or inconsistent gameplay events.
3. **Evidence record** stores the rule triggered, event sequence, build/version, and confidence.
4. **Ban service** makes the shared decision. Lobby hosts cannot create or remove global bans.
5. **Lobby admission check** asks the service whether a player is blocked before allowing entry.
6. **Android companion app** displays local match logs, detection explanations, and ban status. It does not need to patch the official game.

## Anti-false-positive policy

- A client-side suspicion alone is never enough for a permanent ban.
- Prefer server-verified evidence and deterministic rules.
- Low-confidence cases are logged or temporarily restricted, not permanently banned.
- Every automated decision records a reason and evidence reference.
- Ban records should have expiry and an administrator-independent review mechanism.
- The service must rate-limit reports and reject forged or replayed evidence.

## Development stages

1. Write and test the detection policy.
2. Define a signed lobby-event format.
3. Build a small ban-service API and database.
4. Build a test lobby adapter and automated tests.
5. Build the Android companion interface.
6. Package and test only after a compatible lobby integration exists.

## Important limitation

This repository is an early project scaffold. It is not a working APK or a functioning Among Us integration yet. Shared bans cannot affect ordinary official lobbies.
