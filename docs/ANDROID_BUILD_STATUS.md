# Android APK build status

Last checked: November 10, 2026.

## Current state

This repository does not currently contain an Android application module or an Among Us game integration. It contains project documentation, a Python service prototype, service tests, and a GitHub Actions workflow for the service tests.

**There is no installable GAC APK yet.** The existing Python service cannot be packaged as an Among Us mod APK, and building an empty Android shell would not add the requested in-game features.

## Compatibility target

- Android-first development.
- Minimum device baseline for development and testing: Android 11 (API 30), with arm64 support.
- Current Among Us mobile baseline to investigate: v19.0.1, announced by Innersloth on November 3, 2026.
- Every game integration change must be checked against the exact installed game build. Do not assume that an integration for an older version still works.

## Required before a real APK can be built

1. A lawful, permitted modding/integration approach compatible with Innersloth's current policies.
2. The exact target game build and a compatible integration API or mod framework.
3. An Android Gradle project with a real application module, manifest, Kotlin/Java sources, and reproducible build configuration.
4. Implementations for the in-game UI and supported lobby hooks: rules card, AFK notice-before-observer transition, optional level display/requirement, saved presets, lobby filters, and reconnect handling.
5. Tests on Android 11 and newer, including multiplayer compatibility and safe fallback behavior.
6. A signed debug APK for private testing, with clear disclosure that it is unofficial and only intended for compatible community lobbies.

## Build honesty

- Do not distribute a repackaged or modified commercial game client without permission.
- Do not claim compatibility with official public servers.
- Do not claim any feature works until it has been implemented and tested.
- Do not request or embed account passwords, private tokens, or signing secrets in source control.
- If a feature cannot be implemented through a supported integration, leave it as a documented proposal rather than faking it.

## Current project contents

- `.github/workflows/service-tests.yml`: service test workflow.
- `service/server.py`: report-only Python service prototype.
- `service/tests/test_server.py`: service tests.
- `docs/PLANNED_FEATURES.md`: planned player and lobby features.
- `docs/COMMUNITY_REQUESTS.md`: community-request research summary.
- `docs/COMMUNITY_SAFETY_POLICY.md` and `docs/DETECTION_POLICY.md`: moderation and anti-cheat policies.
