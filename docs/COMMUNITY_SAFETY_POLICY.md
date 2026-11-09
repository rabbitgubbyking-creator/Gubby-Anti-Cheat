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

## Rule categories

Use stable rule IDs in reports.

| Rule ID | Category | Examples |
| --- | --- | --- |
| `HATE_SPEECH` | Racism and hate | Slurs, dehumanizing attacks, or targeted hate based on protected traits |
| `HARASSMENT` | Harassment and bullying | Repeated targeted insults, intimidation, or coordinated bullying |
| `SEXUAL_HARASSMENT` | Sexual harassment | Unwanted sexual comments, pressure, or repeated sexual remarks |
| `MINOR_SEXUAL_SAFETY` | Sexual exploitation or grooming involving minors | Attempts to solicit sexual content, sexual coercion, grooming, or sexualized targeting of anyone under 18 |
| `THREATS_VIOLENCE` | Threats | Credible threats to hurt, stalk, or intimidate someone |
| `DOXXING_PRIVACY` | Privacy violations | Sharing someone's private address, phone number, account credentials, or other identifying information without permission |
| `IMPERSONATION` | Impersonation and fraud | Pretending to be another player, moderator, or official service to deceive people |
| `SPAM_DISRUPTION` | Spam and disruption | Flooding chat, raids, malicious repeated disruption, or abusive automation |
| `BAN_EVASION` | Ban evasion | Returning through alternate accounts or identifiers to evade an active shared restriction |
| `UNSAFE_CONTENT` | Other prohibited content | Content that violates the published rules of the participating community |

A rule should not punish respectful discussion, quoting a slur to report it, counterspeech, or good-faith safety reports. Context matters.

## Decision levels

- **Flag for review:** Automated filters or a player report indicate possible misconduct. No ban is applied solely from a keyword match.
- **Temporary safety restriction:** For a credible urgent report involving grooming or sexual exploitation of a minor, the account may be temporarily prevented from joining participating lobbies while an authorized reviewer urgently checks the report. This is a precaution, not a finding of guilt.
- **Moderator action:** A reviewer checks the available context and may issue a warning, mute, or short lobby restriction under the published rules.
- **Temporary shared restriction:** Used for substantiated serious or repeated violations. Apply the default schedule above and record the evidence reference and reviewer.
- **Permanent shared ban:** For confirmed grooming or sexual exploitation involving minors, or other exceptionally severe cases, only after strong evidence and authorized review. Provide an appeal/correction route where safe and appropriate.

A single report is not proof. Coordinated false reports, edited screenshots without context, and impersonated evidence must be considered. A permanent ban must never be triggered by an automated keyword match alone.

## Host notification when a restricted player joins

When a player with an active shared restriction attempts to enter a participating lobby, the system should privately notify that lobby's host. The notification may include the player's in-game username, the policy category, restriction duration or expiry, and a report/reference ID.

Example: **"Gubby Anti-Cheat: [username] is blocked from this community lobby for Bullying/Harassment. Restriction: 14 days. Reference: [report ID]."**

- Send the notice only to the host through a private host-only interface. Do not post it in public lobby chat or broadcast it to other players.
- Show only the minimum information needed to explain the restriction. Never include explicit material, private contact details, or sensitive details about a minor.
- For `MINOR_SEXUAL_SAFETY`, use a neutral label such as **"Serious safety policy violation"** and a reference ID. Do not disclose allegations or identifying details about a potential victim.
- Use the username recorded for that account at the time of the attempted join, and make clear that usernames can change and are not proof of real-world identity.
- The host is informed of the shared service decision but cannot change, revoke, or override it.

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

The shared service is the authority for shared restrictions. Lobby hosts may submit evidence and apply separate local lobby moderation, but they cannot create, revoke, or override a global shared ban.

This policy only works in participating compatible modded lobbies. It cannot moderate ordinary official Among Us servers or replace the reporting tools of the game platform.
