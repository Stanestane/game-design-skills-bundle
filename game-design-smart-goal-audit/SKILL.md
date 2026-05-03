---
name: game-design-smart-goal-audit
description: Audit game design goals, feature objectives, OKRs, initiative aims, or any stated design intent against the SMART criteria adapted for game design. Use when a user shares a design goal, player experience target, retention goal, or feature aim and wants it evaluated or rewritten. Trigger on phrases like "audit my design goals", "is this a good design objective", "my feature goal is...", "we want players to feel...", "our aim for this feature is...", or whenever someone states what a design should achieve and it feels vague or unmeasurable. Also trigger when a design document contains aims or success criteria that need stress-testing. Even soft goals like "players should feel powerful" are valid — apply the framework and return both the audit and a rewritten version.
---

# Game Design SMART Goal Audit

Audit game design goals against the SMART criteria, adapted for the realities of game design work — where goals often mix player experience intentions, behavioral outcomes, and business metrics.

## Why SMART in Game Design

Game design goals often fail in predictable ways:
- **Too vague to evaluate**: "Players should feel engaged" — what does engaged look like? How do you know when you've achieved it?
- **Unmeasurable by intent**: "The loop should feel good" — feeling is real, but untestable without a proxy metric or a defined observation method.
- **Scoped to infinity**: "Improve retention" — which segment? Which part of the funnel? By how much?
- **Disconnected from the design itself**: A goal that could apply to any feature is not a design goal, it's a business wish.

SMART forces clarity. Applied to game design, it helps distinguish *design intent* (what experience you're crafting) from *design success criteria* (how you'll know you achieved it).

---

## The SMART Framework — Game Design Interpretation

| Letter | Criterion | Game design lens |
|--------|-----------|-----------------|
| **S** | **Specific** | Does the goal name a concrete mechanic, system, player segment, moment, or behavior — not just a vague direction? |
| **M** | **Measurable** | Is there a metric, behavioral signal, playtest observation method, or proxy indicator that confirms the goal was achieved? |
| **A** | **Achievable** | Is it realistic given team size, scope, platform, timeline, and existing systems? Does it avoid over-promising on player behavior? |
| **R** | **Relevant** | Does it connect to the game's pillars, the feature's purpose, or a known player need? Would hitting this goal actually matter? |
| **T** | **Time-bound** | Does it have a milestone, sprint, release, or playtest checkpoint attached? |

---

## Audit Process

### Step 1: Identify goal type

Before auditing, classify the goal — this shapes how you apply SMART:

- **Experience goal** — describes a player feeling or state ("players feel powerful")
- **Behavioral goal** — describes a player action or pattern ("players return 3 sessions per week")
- **Design output goal** — describes what the team will build ("ship the crafting system in Q2")
- **Metric goal** — describes a KPI or indicator ("increase D7 retention by 5%")
- **Mixed goal** — combines intent and outcome (common, often the weakest)

Flag the type at the top of the audit. Experience goals require special handling — they need a *proxy metric or observation method* to become measurable.

### Step 2: Score each SMART criterion

For each criterion:
- ✅ **Strong** — clearly met
- ⚠️ **Partial** — implied or weakly present
- ❌ **Missing** — absent

Write 1–2 sentences per criterion explaining specifically what is strong or what is missing. For game design goals, pay special attention to:
- **S**: Is the player segment named? Is the game moment or system named?
- **M**: For experience goals, is there a playtest method, behavioral proxy, or survey instrument defined?
- **A**: Does the goal respect the scope and constraints of the feature or team?
- **R**: Does the goal connect to a design pillar, player need, or business objective?
- **T**: Is there a playtest gate, milestone, or release tied to evaluation?

### Step 3: Overall assessment

2–3 sentences on the goal's overall quality. Name the single biggest weakness and why it matters.

### Step 4: Rewrite the goal

Rewrite as a stronger SMART version that:
- Preserves the original design intent
- Adds a concrete scope, measurable signal, and timeframe
- For experience goals: adds a proxy metric or observation method (e.g., "as measured by playtest sessions showing X behavior" or "validated by a post-session survey score of Y")
- Flags assumptions in brackets: [assumed: D7 retention proxy] [assumed: Q3 milestone]
- Avoids inventing design decisions the team hasn't made

### Step 5: Coaching note (optional)

If the goal reveals a pattern — e.g., all goals are experience-focused with no measurement plan, or all goals are metric-focused with no design intent — add a brief pattern observation.

---

## Output Format

```
## Goal: [quote or paraphrase]
**Type**: [Experience / Behavioral / Design output / Metric / Mixed]

### SMART Audit

**S – Specific**: [✅ / ⚠️ / ❌] [explanation]
**M – Measurable**: [✅ / ⚠️ / ❌] [explanation]
**A – Achievable**: [✅ / ⚠️ / ❌] [explanation]
**R – Relevant**: [✅ / ⚠️ / ❌] [explanation]
**T – Time-bound**: [✅ / ⚠️ / ❌] [explanation]

### Overall
[2–3 sentence summary. Name the biggest weakness.]

### Rewritten Goal
> [Improved SMART version]

[Assumptions noted if any]
```

If multiple goals are provided, audit each in sequence, then add a **Patterns Across Goals** section if relevant.

---

## Tone and approach

- Treat this like a senior designer giving a brief review — direct, specific, not condescending.
- Don't reject experience goals as "unmeasurable by nature." Instead, challenge the team to define the measurement method (playtest behavior, NPS proxy, session survey, behavioral telemetry).
- If a goal is genuinely well-written, say so briefly and move on. Don't pad weak praise.
- If the user provides context (game genre, player segment, live vs. pre-launch) — use it. Goals that are vague in isolation might be appropriate for the stage.
- If a goal is really a vision statement or principle, flag it gently: "This reads more like a design pillar than a goal — here's how to turn it into one."
