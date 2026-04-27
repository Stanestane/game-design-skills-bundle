---
name: game-design-friction-journey-audit
description: Audit a game, feature flow, economy path, onboarding journey, progression chain, or live-ops loop for friction quality and friction accumulation. Use when diagnosing where players stall, disengage, churn, or feel overloaded; when distinguishing productive challenge from harmful friction; or when evaluating whether constraints, waiting, confusion, resource pressure, or multi-step dependencies are creating strategy, tension, frustration, or deadlock.
---

# Game Design Friction Journey Audit

Audit a design by mapping where friction appears across a player journey, what kind of friction it is, how it accumulates, and where useful challenge mutates into harmful drag.

Use this skill when a feature feels sticky in the wrong way, when progression seems to slow down for reasons players cannot articulate clearly, or when you need to separate meaningful challenge from accidental obstruction.

## Core principle

Not all friction is bad.

Some friction creates commitment, decision-making, anticipation, and mastery. Other friction creates confusion, paralysis, resentment, or churn. The job is not to remove all resistance. The job is to identify which resistance is doing design work and which is merely getting in the player's way.

## What to produce

Generate:
1. **Audit target** - what journey, loop, or feature is being reviewed
2. **Journey breakdown** - the major steps in player progression through the target flow
3. **Friction map** - where friction appears, what kind it is, and what causes it
4. **Accumulation analysis** - where multiple frictions stack into exhaustion or deadlock
5. **Diagnosis** - where the design shifts from meaningful challenge to harmful blockage
6. **Recommendations** - what to preserve, reduce, surface, reorder, or remove

## Process

### 1. Define the journey being audited

Clarify:
- what system or flow is under review
- what kind of player it applies to
- what stage of play it belongs to: FTUE, early game, mid-game, elder game, event loop, monetization path, social loop, etc.
- what desired player behavior the flow is supposed to support

Write:
- **Audit target**
- **Expected player goal**
- **Player context**

### 2. Break the journey into steps

Map the journey as a sequence of player-facing steps.

For each step, identify:
- player action
- player decision
- requirement or dependency
- feedback or reward
- what unlocks the next step

Keep steps coarse enough to be readable but concrete enough to locate friction.

### 3. Identify friction at each step

For each step, ask:
- what slows progress?
- what blocks progress?
- what creates uncertainty?
- what consumes time, attention, or resources?
- what forces tradeoffs or commitment?

Possible friction sources:
- resource scarcity
- dependency chains
- waiting and timers
- unclear affordances or goals
- UI or information opacity
- cognitive overload
- skill challenge
- social coordination burden
- random variance
- harsh penalty or recovery cost
- monetization pressure

### 4. Classify the friction

Classify each friction point as one of these:

#### Productive friction
Supports:
- decision-making
- planning
- anticipation
- mastery
- commitment
- strategic tradeoff
- emotional tension that feels fair and legible

#### Harmful friction
Produces:
- confusion
- dead time without meaning
- arbitrary blocking
- unreadable requirements
- overloaded task chains
- repeated admin work
- punishment without learning
- progress paralysis

#### Mixed friction
Useful in principle, but currently too strong, too opaque, too stacked, or too poorly timed.

Do not treat this as binary if it is not. Many systems are good ideas implemented at the wrong intensity.

### 5. Assess intensity and visibility

For each friction point, rate:
- **Intensity** - low / medium / high
- **Visibility** - obvious / partially hidden / opaque
- **Fairness feel** - fair / borderline / unfair-feeling

A friction can be mild but still dangerous if it is hidden. It can also be intense but acceptable if the player clearly understands it and sees why it exists.

### 6. Analyze friction accumulation

Look for stack effects.

Ask:
- where do several medium frictions compound into a high-friction moment?
- where are players forced to satisfy too many constraints at once?
- where does the flow ask for too much memory, too much waiting, or too many parallel tasks?
- where do repeated harmful frictions appear without enough reward, clarity, or release?

Common accumulation patterns:
- multiple resources plus timer plus low clarity
- complex chain plus weak feedback plus low inventory space
- repeated losses plus long recovery plus weak learning signal
- social obligation plus schedule pressure plus poor coordination tools

### 7. Find the breakpoints

Identify:
- where challenge turns into drag
- where strategy turns into opacity
- where anticipation turns into dead time
- where difficulty turns into helplessness
- where a healthy loop turns into churn risk

These are the key design breakpoints.

### 8. Diagnose the role of friction in the design

Answer:
- which friction points are core to the fantasy or mastery arc?
- which friction points only exist because of weak clarity, weak UX, poor pacing, or over-constrained economy?
- what friction is essential and should be protected?
- what friction is currently doing accidental damage?

### 9. Recommend design changes

For each major friction issue, specify:
- **Issue**
- **Why it hurts**
- **Keep / reduce / remove / surface / reorder / soften**
- **Expected effect**

Typical interventions:
- surface hidden requirements
- reduce simultaneous constraints
- improve feedback and goal clarity
- shorten dead-time without removing commitment
- preserve meaningful tradeoffs while removing admin burden
- stagger dependencies instead of stacking them all at once

## Response structure

### Audit Target
- ...

### Journey Breakdown
1. ...
2. ...
3. ...

### Friction Map
| Step | Friction Point | Type | Cause | Intensity | Visibility | Fairness Feel |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

### Accumulation Analysis
- ...

### Breakpoints
- ...

### Diagnosis
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode

Use this quick pass when speed matters:
- where does the player slow down or stop?
- is the friction creating strategy or confusion?
- is it fair and legible?
- what other frictions are stacking nearby?
- what should be preserved, softened, surfaced, or removed?

## Working principle

Good friction gives the player something meaningful to push against.
Bad friction makes the player wonder why they are pushing at all.
