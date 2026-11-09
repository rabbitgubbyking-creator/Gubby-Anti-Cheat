# Planned In-Game Settings and Lobby Features

This document records requested features for a future compatible Gubby Anti-Cheat mod. These are proposals, not features that currently work. They must be implemented and tested only in compatible community modded lobbies and must not interfere with official Among Us servers.

## Player settings

### Dark chat and interface theme
- Add a Dark Mode option for the chat panel and GAC menus.
- Offer System Default, Light, and Dark.
- Keep message text, timestamps, buttons, and warning notices readable with accessible contrast.
- Do not change the game's theme globally if the mod cannot safely control that interface.

### Frame-rate setting
- Offer supported frame-rate caps such as 30, 60, 90, 120, and Uncapped.
- Show only modes the device and game build can actually support.
- Default to Auto/Recommended to avoid overheating, battery drain, or unstable performance.
- Changing this setting must not change game simulation speed or provide a gameplay advantage.

### Graphics quality
Among Us is not a conventional video player, so 480p/720p/1080p labels may not map directly to its graphics. Prefer graphics presets such as Low, Medium, High, and Highest, plus an optional render-scale control if the game engine exposes it safely.
- If a resolution-style control is technically supported, explain that it changes rendering resolution, not the quality of chat messages or internet streaming.
- Never promise 1080p or a particular visual result unless the target device and game build support it.
- Include Auto/Recommended and restore-default options.

### Automatic chat translation
- Let each player choose a preferred display language in GAC settings.
- Optionally translate incoming lobby messages into that language.
- Optionally translate a player's outgoing message from their typed language into the recipient's chosen language.
- Preserve the original message and provide a one-tap Show Original / Show Translation control.
- Clearly mark translated text so players do not mistake it for the exact original wording.
- Translation should be opt-in, with a per-lobby disable option. Do not silently send private messages or collect unrelated chat.
- Use a trusted translation provider or an offline translation model where practical. If a provider is used, disclose that message text is sent to it, minimize retention, and never put API keys in the APK.
- Handle unsupported languages, timeouts, rate limits, and failed translations by showing the original message.
- Do not use machine translation alone as proof for moderation or bans; reviewers should check the original context.

## Host lobby settings

### Lobby rules editor
- Let the host create and publish a rules card before players join.
- Include editable rules such as respectful chat, no spam, language expectations, minimum account level, AFK behavior, and whether chat translation is enabled.
- Show the rules to players before joining and keep a viewable copy inside the lobby.
- Require the host to confirm changes; show an updated notice when rules change during a session.
- Keep rules within the game's and platform's policies. Do not let hosts add discriminatory or abusive rules.
- A rules card explains expectations; it does not itself prove a violation or automatically create a global ban.

### AFK ghost / observer mode
- Let a player manually enable AFK mode, and optionally let the host configure an inactivity timeout before the game offers AFK mode.
- When AFK mode starts, move the player out of active gameplay into a neutral, non-interactive observer state with no visible player body.
- Clearly mark the player as **AFK / Observer** in the lobby or player list, and announce the state change so nobody mistakes the disappearance for a kill.
- AFK mode must not create a corpse, trigger a kill report, count as a death, or make another player appear responsible.
- While AFK, the player cannot move, complete tasks, sabotage, kill, call meetings, vote, or affect round outcomes.
- When the player returns, let them rejoin only at a safe game-state boundary chosen by the host/mod rules; do not silently restore them mid-action.
- The host can enable or disable AFK mode and set the inactivity timeout, but cannot use it to secretly remove or impersonate a player.
- If the game integration cannot support a reliable observer state, use a clearly labelled AFK lobby state instead of pretending the player died.


### Minimum account-level requirement
- In a compatible private/community lobby, let the host optionally set a minimum Among Us account level.
- If enabled, players below the selected threshold can be automatically removed from that lobby with a clear notice explaining the host's minimum-level rule.
- Let the host disable the rule, change the threshold, and optionally allowlist invited/friend accounts.
- If a player's level cannot be verified reliably, do not silently assume they are under the threshold. Let the host choose whether unknown levels are allowed or require manual review.
- Apply this only to the current lobby. It must not create a global GAC ban or prevent the player from using the game elsewhere.
- Explain that account level is not a reliable measure of skill or trustworthiness. Hosts should avoid setting unfairly high thresholds.
- The host setting must be visible before joining where the game integration allows it. Do not use hidden or deceptive removal behavior.

## Additional useful ideas

1. **Reconnect grace period:** allow a disconnected player a short window to rejoin their previous seat.
2. **Lobby rules editor and card:** let hosts publish clear rules and show them before players join and inside the lobby.
3. **Chat controls:** player mute, report, and block controls with clear local-versus-shared effects.
4. **Translation language indicator:** show each player's selected language and whether a message is original or translated.
5. **Performance preset:** one Auto option that selects conservative graphics and frame-rate settings based on supported device capabilities.
6. **Appeal/status screen:** let a player see whether a GAC service restriction is temporary or permanent, its reason, expiry, and the appeal route without exposing private reporter details.\n7. **AFK observer mode:** safely pause an inactive player without creating a fake death or misleading kill report.

## Implementation order

1. Dark chat theme and basic settings screen.
2. Supported frame-rate caps and safe graphics presets, after confirming the game engine exposes those controls.
3. Translation prototype with original-text fallback and privacy disclosure.
4. Host-configurable minimum-level rule, only after a reliable level source and lobby-only kick API are available.
5. Lobby rules editor and AFK observer mode, after validating safe game-state transitions.\n6. Reconnect improvements.

## Compatibility and safety limits

- These features are not implemented yet.
- They require a compatible game integration; a standalone service API cannot change Among Us menus or lobby behavior by itself.
- Do not patch or interfere with ordinary official servers.
- Never claim a feature is available until it has been built and tested on the target game version.
