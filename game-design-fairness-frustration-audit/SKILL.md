---
name: game-design-fairness-frustration-audit
description: Audit a game, feature, failure loop, combat encounter, reward system, progression wall, or high-variance mechanic for perceived fairness and frustration. Use when diagnosing whether players feel cheated, whether difficulty feels deserved, whether randomness, feedback, and challenge interact badly, or why a design remains technically functional yet still produces anger, blame, or refusal to retry.
---

# Game Design Fairness and Frustration Audit

Audit a design by asking whether it feels fair, understandable, and worth retrying.

Use this skill when the real question is not merely "is it balanced" but "why does this make players mad?" This audit combines three lenses:
- attribution theory: who or what players blame
- flow theory: whether challenge and skill stay aligned over time
- perceived randomness: whether uncertainty feels exciting, suspicious, or rigged

Focus on player perception. Mechanical correctness is not enough if the experience still feels hostile.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

Players will accept difficulty, failure, and uncertainty when they feel:
- the cause is understandable
- they had meaningful influence
- the challenge matched a learnable demand
- luck was visible, bounded, or mitigable

Players reject the same systems when outcomes feel:
- arbitrary
- hidden
- uncontrollable
- disproportionate
- repeatedly punishing without teaching

## What to produce

Generate:
1. **Fairness assessment** - whether the experience feels fair, questionable, or unfair
2. **Frustration profile** - what kind of frustration it creates and why
3. **Attribution diagnosis** - how players explain the outcome
4. **Randomness diagnosis** - how uncertainty is perceived and whether it is trusted
5. **Flow diagnosis** - where challenge-skill mismatch amplifies frustration
6. **Design actions** - what to change first to reduce hostility and improve retry willingness

## Process

### 1. Define the audit target
Clarify:
- what exact mechanic, loop, or scenario is producing the concern
- whether the issue centers on failure, reward, difficulty, or inconsistency
- what player segment is feeling the pain most

Write:
- **Audit target**
- **Player segment**
- **Observed complaint or risk**

### 2. Reconstruct the player-facing event
Map:
- what the player tried to do
- what the system did in response
- what role randomness played
- what feedback the player saw
- what the cost of failure was

Ask:
- What did the player think would happen?
- What actually happened?
- What evidence did the game provide to explain the result?
- What could the player realistically have done differently?

### 3. Run the attribution lens
Judge whether the likely reading is:
- internal or external
- stable or unstable
- controllable or uncontrollable

Translate that into the likely player sentence, not just the technical classification.

### 4. Run the randomness lens
Examine:
- whether randomness is visible or hidden
- whether it changes frequency, impact, or both
- whether the player can mitigate, predict, or prepare for it
- whether streaks or outliers feel suspicious
- whether randomness is being mistaken for execution failure or designer malice

### 5. Run the flow lens
Check:
- whether challenge exceeded current skill too sharply
- whether the player had enough teaching or support before the demand hit
- whether repetition creates learning or just repeated punishment
- whether the experience becomes anxious, exhausting, or deadening over time

### 6. Identify compounding frustration patterns
Pay special attention to combinations like:
- high challenge + low clarity
- high punishment + low controllability
- hidden RNG + severe loss
- repeated failure + stable external attribution
- long retry cycle + low learning value

This is where frustration often shifts from healthy tension into "I am done with this."

### 7. Grade the fairness experience
Use a direct classification:
- **Fair** - hard, but understandable and teachable
- **Questionable** - some understandable basis, but trust is fragile
- **Unfair** - outcomes feel hostile, hidden, or insufficiently controllable

State clearly whether the main problem is:
- clarity
- control
- randomness
- pacing
- punishment
- inconsistency
- or a combination

### 8. Convert findings into design changes
For each issue, specify:
- **Problem**
- **Why it feels unfair**
- **Suggested change**
- **Expected emotional effect**

Examples:
- add telegraphing -> reduces external blame
- expose odds or logic -> reduces suspicion
- add mitigation or counterplay -> increases control
- soften punishment during learning -> preserves retry motivation
- shorten retry cycle -> converts frustration into iteration

## Response structure

Use this structure unless the user asks for something else:

### Audit Target
- ...

### Fairness Assessment
- Overall: Fair / Questionable / Unfair
- Why: ...

### Frustration Profile
- ...

### Attribution Diagnosis
- ...

### Randomness Diagnosis
- ...

### Flow Diagnosis
- ...

### Root Causes
- ...

### Recommendations
1. ...
2. ...
3. ...

### Minimal Fix
- ...

## Fast mode

Use this quick pass when speed matters:
- Why does the player feel cheated?
- Is the main issue hidden cause, low control, bad RNG framing, or challenge mismatch?
- Does the player feel like retrying or quitting?
- What is the smallest change that most improves trust?

## Usage notes

This audit is especially useful for:
- boss fights
- roguelite losses
- gacha or loot outcomes
- PvP or PvE streak complaints
- onboarding punishments
- progression walls
- one-shot kills
- card draw variance
- AI behavior that feels inconsistent or "scripted"

Common patterns to watch for:
- a mathematically fair system can still feel unfair if its logic is hidden
- low-probability disasters feel much worse when the player had no mitigation tools
- high punishment demands high clarity
- frustration becomes toxic when players cannot convert failure into learning
- if players blame luck, the system, and pacing at the same time, fix trust before tuning difficulty

## Working principle

A fair game can still frustrate. The key question is whether the frustration points toward mastery or away from the game.

Use this skill when players are not just struggling, but suspecting the design itself.