# Community Safety and Conduct Policy

This policy applies only in participating Gubby Anti-Cheat community lobbies. It is separate from gameplay-cheat detection. The service should use consistent, published rules and protect users from abuse without turning unverified accusations into automatic permanent bans.

## Default restriction schedule

These are default durations for a first substantiated violation. Repeated or especially severe violations may receive a longer restriction after review. The shared service must store the rule ID, decision, start time, expiry, evidence reference, and reviewer.

| Rule ID | Category | Default restriction |
| --- | --- | --- |
| `HATE_SPEECH` | Racism and targeted hate | 6 months |
| `HARASSMENT` | Bullying and harassment | 14 days |
| `SEXUAL_HARASSMENT` | Sexual harassment | 1 year |
| `MINOR_SEXUAL_SAFETY` | Grooming or sexual exploitation involving minors | Permanent, after urgent authorized review |
| `THREATS_VIOLENCE` | Credible threats or intimidation | 31 days |
| `DOXXING_PRIVACY` | Sharing private identifying information without permission | 1 year |
| `SPAM_DISRUPTION` | Spam, chat flooding, or raids | 1 day |
| `IMPERSONATION` | Impersonation or fraud | 30 days |
| `BAN_EVASION` | Evading an active shared restriction | 90 days |
| `UNSAFE_CONTENT` | Other serious prohibited conduct | Case-by-case, based on severity |

Durations are defaults, not a substitute for reviewing context. A warning or shorter action may be appropriate for a minor first-time incident. Repeated violations can escalate. Severe conduct can justify a longer restriction, but the reason and evidence must be recorded.

## Discord community membership

The Gubby Anti-Cheat community invite is https://discord.gg/GBgmps6X6. Joining the Discord server is intended to be a requirement for activating the anti-cheat lobby service.

Membership must be verified securely by a future Discord OAuth2/bot integration before issuing an anti-cheat service session. A pasted username, screenshot, or invite click is not proof of membership. Link the Discord account to the game's pseudonymous player ID using an explicit consent flow; do not expose bot tokens or OAuth secrets in the Android app or repository. If membership cannot be verified, explain that the player must join the community and complete account linking. This Discord requirement is not implemented in the current prototype.

## Restriction behavior: disable the service, do not kick

A shared restriction suspends access to Gubby Anti-Cheat features for the restriction period. It is not a ban from Among Us itself.

- Do not kick, disconnect, or forcibly remove a restricted player from their own lobby.
- Do not prevent them from using the ordinary game's lobby features outside Gubby Anti-Cheat.
- If a restricted player opens or hosts a lobby, leave them in that lobby but do not activate Gubby Anti-Cheat protection or shared services for that account.
- Show a clear in-game system chat notice to that player: **"Gubby Anti-Cheat access is suspended. Reason: [category]. Duration: [time remaining or permanent]."**
- If a restricted player tries to activate the service in another participating lobby, deny only the anti-cheat service session and show the same notice. Do not issue a game kick.
- Notify the host privately that the player's anti-cheat service access is suspended. Do not publish the notice to the whole lobby.
- When a temporary restriction expires, service access may be restored automatically after the status is rechecked.

## Host notification when a restricted player attempts to use the service

When a player with an active shared restriction attempts to activate Gubby Anti-Cheat in a participating lobby, privately notify that lobby's host. The notice may include the player's current in-game username, policy category, restriction duration or expiry, and a report/reference ID.

Example: **"Gubby Anti-Cheat: [username] cannot use anti-cheat services. Reason: Bullying/Harassment. Restriction: 14 days. Reference: [report ID]."**

- Send the notice only to the host through a private host-only interface. Do not post it in public lobby chat or broadcast it to other players.
- Show only the minimum information needed to explain the restriction. Never include explicit material, private contact details, or sensitive details about a minor.
- For `MINOR_SEXUAL_SAFETY`, use a neutral label such as **"Serious safety policy violation"** and a reference ID. Do not disclose allegations or identifying details about a potential victim.
- Use the username recorded for that account at the time of the attempted service activation, and make clear that usernames can change and are not proof of real-world identity.
- The host is informed of the shared service decision but cannot change, revoke, or override it.

## Decision levels

- **Flag for review:** Automated filters or a player report indicate possible misconduct. No ban is applied solely from a keyword match.
- **Temporary safety restriction:** For a credible urgent report involving grooming or sexual exploitation of a minor, the account may be temporarily prevented from activating the service while an authorized reviewer urgently checks the report. This is a precaution, not a finding of guilt.
- **Moderator action:** A reviewer checks the available context and may issue a warning, mute, or short lobby restriction under the published rules.
- **Temporary shared restriction:** Used for substantiated serious or repeated violations. Apply the default schedule above and record the evidence reference and reviewer.
- **Permanent shared restriction:** For confirmed grooming or sexual exploitation involving minors, or other exceptionally severe cases, only after strong evidence and authorized review. Provide an appeal/correction route where safe and appropriate.

A single report is not proof. Coordinated false reports, edited screenshots without context, and impersonated evidence must be considered. A permanent restriction must never be triggered by an automated keyword match alone.

## Special handling for sexual safety involving minors

- Treat credible grooming, sexual coercion, or attempts to obtain sexual material from a minor as urgent safety reports.
- Do not ask users to upload, forward, or reproduce sexual images or videos.
- Never store, display, or redistribute sexual imagery involving minors.
- Store only minimal non-explicit metadata, such as report ID, timestamps, account identifiers scoped to the service, and a safe evidence reference.
- Restrict access to these reports to specifically authorized safety reviewers.
- Follow the relevant platform's reporting process and applicable law. Do not conduct amateur investigations or contact an alleged offender to confront them.

## Evidence and privacy

- Collect only evidence relevant to the rule, such as message IDs, timestamps, lobby IDs, and limited surrounding text where safe and necessary.
- Prefer platform message references over copying entire private conversations.
- Do not collect real names, phone numbers, precise location, device fingerprints, or unrelated personal data.
- Keep reports private and access-controlled. Never publish a public shame list.
- Record who reviewed a report, the rule applied, the decision, and when a restriction expires.
- Provide a clear appeal/correction process and remove restrictions when evidence is overturned.

## Authority and boundaries

The shared service is the authority for shared restrictions. Lobby hosts may submit evidence and apply separate local lobby moderation, but they cannot create, revoke, or override a global shared restriction.

This policy only works in participating compatible modded lobbies. It cannot moderate ordinary official Among Us servers or replace the reporting tools of the game platform.
