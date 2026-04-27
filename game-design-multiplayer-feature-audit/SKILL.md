---
name: game-design-multiplayer-feature-audit
description: Audit a game, feature, live-ops layer, social system, or multiplayer concept for the quality and fit of its social design. Use when evaluating collaboration, competition, collaborate-to-compete structures, matchmaking, guilds/clubs, synchronous versus asynchronous play, realtime constraints, depth of social interaction, community formation, vanity/status systems, or how to add social play to a mostly single-player game.
---

# Game Design Multiplayer Feature Audit

Audit a design by asking what kind of social experience it is actually creating, for whom, at what coordination cost, and with what likely community effect.

Use this skill when a design has multiplayer or social ambitions and you need to judge whether those ambitions are coherent, motivating, scalable, and well matched to the core fantasy of the game.

## Core principle

Social design is not a checklist of features.

A leaderboard, guild, chat channel, or PvP mode does not automatically create meaningful social play. Strong multiplayer design aligns player motivation, time structure, coordination demands, visibility, and community purpose.

## What to produce

Generate:
1. **Audit target** - what is being reviewed and what kind of social experience it appears to aim for
2. **Social promise** - the core social fantasy or player promise
3. **Motivation map** - competition, collaboration, collaborate-to-compete, belonging, vanity/status, knowledge exchange
4. **Time and synchronization audit** - realtime, non-realtime, synchronous, asynchronous, or hybrid
5. **Social depth audit** - how deep the interaction really goes
6. **Community and status audit** - whether the system supports durable groups, identity, and readable prestige
7. **Risks / failure modes** - where the design is likely to break, flatten, or create friction
8. **Recommendations** - what to strengthen, stage, simplify, avoid, or postpone

## Process

### 1. Define the social promise

State in one or two sentences what the feature is socially promising.

Examples:
- compete for rank and status against peers
- cooperate with a small squad to solve hard encounters
- contribute to a group goal while still pursuing personal goals
- show off taste, city design, wealth, or mastery
- let solo players feel the presence of others without hard coordination

If the design appears to promise incompatible things at once, say so early.

Common tension examples:
- calm self-expression versus destructive PvP
- casual mobile bursts versus rigid appointment play
- individual authorship versus committee-driven collaboration

### 2. Map the motivation structure

Audit the feature across these motivation buckets:

- **Competition** - rivalry, ranking, domination, comparison
- **Collaboration** - helping, supporting, coordinating, solving together
- **Collaborate-to-compete** - teamwork in service of beating another team, club, faction, or cohort
- **Belonging** - identity, membership, shared rituals, durable group attachment
- **Vanity / status** - visible prestige, taste display, wealth display, proof of mastery
- **Knowledge exchange** - teaching, strategy sharing, build discussion, optimization culture

Do not just list them. Judge which ones are truly doing work and which are merely implied.

### 3. Check motivational fit

Use a Self-Determination-Theory-inspired check:

- **Autonomy** - does the player have choice of role, pace, route, or strategy?
- **Competence** - can the player demonstrate mastery, improvement, contribution, or skill?
- **Relatedness** - can the player meaningfully connect, compare, help, coordinate, or belong?

Flag fake-social systems that mostly create obligation, admin work, or shallow compliance.

Examples:
- a guild donation button may create duty without meaningful relatedness
- a giant anonymous global leaderboard may technically create comparison but fail emotionally
- a cosmetic showcase may create status only if others can actually see and decode it

### 4. Audit time model and synchronization demands

Classify the feature explicitly:

- **Realtime synchronous**
- **Non-realtime synchronous window**
- **Asynchronous competitive**
- **Asynchronous collaborative**
- **Hybrid**

Then ask:
- how long does a typical social interaction last?
- must players overlap in time?
- what happens if one player misses the window?
- does the audience/platform support this coordination burden?
- is the feature mobile-friendly, session-friendly, or appointment-heavy?

Call out time-model mismatch clearly. A socially appealing idea can still be wrong for the audience if it demands too much synchronization.

### 5. Audit depth of social interaction

Rate the design using this depth ladder:

1. **Awareness** - others exist
2. **Comparison** - scores, rankings, visible collections, ghosts, showcases
3. **Indirect exchange** - gifting, trading, donations, borrowing
4. **Communication** - chat, pings, negotiation, requests
5. **Coordination** - timing, role division, tactical cooperation
6. **Collective strategy** - shared plans, doctrine, adaptation, team optimization
7. **Community identity** - durable groups, leadership, rituals, norms, reputation, belonging

State where the feature sits now, where it wants to sit, and whether the gap is credible.

Do not assume deeper is always better. More depth usually means more friction, moderation burden, onboarding cost, and design risk.

### 6. Audit competition design

If the feature includes competition, evaluate:

- leaderboard scale
- intimacy of comparison group
- freshness of score movement
- reward brackets and goal density
- fairness and matchmaking logic
- anti-exploit / anti-smurf / anti-boost concerns
- visibility of rivals and stakes
- whether losing still feels legible and motivating

Prefer emotionally legible comparison over giant anonymous ranking walls.

Small groups, leagues, seasons, and visible rivals are often stronger than one global list.

### 7. Audit collaboration design

If the feature includes cooperation, evaluate:

- clarity of shared goal
- role differentiation
- visibility of contribution
- whether casual or weaker players can still help
- whether personal goals can also feed the group goal
- dependency risk if one player flakes or churns
- communication need versus communication tools provided

Strong collaborative systems often let players pursue personal goals that still contribute to a shared outcome.

### 8. Audit community formation

Ask whether the design supports durable social structure:

- clubs, clans, guilds, alliances, squads
- friend discovery and invitations
- reasons to stay in a group
- recurring cadence and rituals
- visible contribution and group memory
- discoverability of healthy groups
- lightweight leadership roles or responsibilities

Ask the blunt question:
**Why would a player bother joining or maintaining this group?**

If the answer is only chat access, habit, or raw rewards, call that out as thin.

### 9. Audit vanity and status

Evaluate the status layer through four checks:

1. **Visibility** - can other players see the signal?
2. **Legibility** - can they understand what it means?
3. **Desirability** - is it aspirational?
4. **Fairness** - what exactly is being signaled: skill, taste, effort, money, tenure, luck?

Common status surfaces:
- ranks and leagues
- trophies and seasonal records
- rare cosmetics
- city/base/avatar/profile display
- titles and badges
- featured placements and judged showcases

Vanity systems are weak when they are private, unreadable, or disconnected from any real social surface.

### 10. Audit fit for mostly single-player games

When the design adds social play to a mostly solo experience, ask:

- what player behaviors already suggest social demand?
- what social fantasy naturally fits the core loop?
- what part of the fantasy should remain personal and unshared?
- should the first social layer be comparison, exchange, clubs, judged showcases, or direct PvP?
- is the design trying to force deep collaboration onto a fantasy built around individual authorship or control?

Be skeptical of bolted-on realtime multiplayer when the core fantasy is solitary mastery, self-expression, or authorship.

A safer migration path often goes:
1. observe others
2. compare with others
3. exchange with others
4. group with others
5. collaborate to compete
6. only then add tightly synchronized modes if the audience proves it wants them

### 11. Diagnose failure patterns

Common failure shapes:
- **social wallpaper** - many social features, little actual social meaning
- **coordination overkill** - audience asked for more synchronization than it can sustain
- **status fog** - prestige exists but players cannot read or value it
- **guild shell** - groups exist but have no real purpose
- **comparison numbness** - ranks exist but movement feels emotionally meaningless
- **solo fantasy violation** - the social layer damages the core fantasy instead of extending it
- **high-friction collaboration** - teamwork exists but the cost of organizing it is too high
- **shallow relatedness** - players are adjacent, not meaningfully connected

### 12. Convert findings into actions

For each major issue, specify:
- **Issue**
- **Why it hurts**
- **What kind of player it hurts most**
- **Suggested change**
- **Expected effect**

## Response structure

### Audit Target
- ...

### Social Promise
- ...

### Motivation Map
- Competition: ...
- Collaboration: ...
- Collaborate-to-compete: ...
- Belonging: ...
- Vanity / status: ...
- Knowledge exchange: ...

### Time and Synchronization Audit
- ...

### Social Depth Audit
- Current depth: ...
- Intended depth: ...
- Gap: ...

### Community and Status Audit
- ...

### Risks / Failure Modes
1. ...
2. ...
3. ...

### Recommendations
- Do now: ...
- Do later: ...
- Avoid: ...

## Fast mode

Use this quick pass when speed matters:
- what social fantasy is this actually selling?
- is it mostly competition, collaboration, or collaborate-to-compete?
- does the time model fit the audience?
- how deep is the social interaction really?
- why would players stay in a group?
- what visible status or prestige does the system create?
- what is the single biggest mismatch or risk?

## References

Read these when useful:
- `references/social-design-dimensions.md` for the deeper multiplayer audit checklist and sharper prompts

## Working principle

Strong multiplayer design does not merely place players near each other.
It creates meaningful comparison, contribution, coordination, recognition, or belonging at a coordination cost the audience is actually willing to pay.
