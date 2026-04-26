---
name: game-design-failure-loop-audit
description: "Audit a game, feature, encounter structure, roguelite run, puzzle sequence, onboarding path, or progression gate through the lens of its failure loop: what happens after the player fails, what they learn, what they lose, and why they would or would not try again. Use when diagnosing whether failure teaches, motivates, stalls, humiliates, exhausts, or ejects the player, or when tuning punishment, retry structure, and post-failure recovery."
---

# Game Design Failure Loop Audit

Audit what the game does after the player fails, and whether that loop produces learning, motivation, and retry energy instead of confusion, resentment, or collapse.

Use this skill when a design includes repeated failure states and the real question is not merely "is failure possible" but "what does failure do to the player over time?" The goal is to evaluate what the player loses, what they understand, what they retain, how fast they re-enter, and whether the failure loop makes them want another attempt.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

A good failure loop does not just punish. It converts defeat into renewed intention.

A strong failure loop usually provides:
- readable cause of failure
- meaningful lesson or hypothesis for next attempt
- tolerable cost relative to clarity
- manageable re-entry friction
- emotional permission to try again

A bad failure loop produces:
- confusion without learning
- punishment without agency
- downtime without anticipation
- repetition without adaptation
- shame, fatigue, or helplessness

## What to produce

Generate:
1. **Failure loop summary** - the current structure from failure to re-entry
2. **Loss-learning-retry analysis** - what the player loses, learns, and does next
3. **Friction diagnosis** - where punishment, delay, opacity, or humiliation break the loop
4. **Motivation diagnosis** - why players will retry, hesitate, or quit
5. **Design implications** - what to tune in cost, clarity, pacing, recovery, or support

## Process

### 1. Define the audit target
Clarify:
- what exact failure state or loop is being audited
- what player segment is most affected
- whether the focus is early churn, midgame frustration, endgame mastery, or broad retention

Write:
- **Audit target**
- **Player segment**
- **Failure context**

### 2. Reconstruct the full failure loop
Map the sequence:
- fail
- receive feedback
- pay consequence
- recover or reset
- prepare again
- retry or abandon

Ask:
- What happens immediately after failure?
- What is the player told or shown?
- What is lost?
- What remains?
- How long until the next meaningful attempt?
- What emotional state is the player likely in by then?

### 3. Audit loss, learning, and retention
Evaluate:
- what resources, progress, time, status, or opportunity are lost
- what information or understanding is gained
- what progression, meta-progress, or unlocked knowledge is retained
- whether the player can form a better next-attempt plan

Use this format:

| Dimension | Current state | Effect on retry motivation |
|---|---|---|
| Loss | ... | ... |
| Learning | ... | ... |
| Retention | ... | ... |
| Re-entry speed | ... | ... |

### 4. Diagnose re-entry friction
Look for:
- long dead time before the next real attempt
- tedious setup or replay of solved content
- unclear recovery path
- punishment that exceeds the educational value of the failure
- restart structures that encourage resignation rather than iteration

Ask:
- Is the retry fast enough?
- Is the player replaying meaningful challenge or just chores?
- Does the recovery path preserve tension or drain it?

### 5. Diagnose emotional effect
Check whether the failure loop tends to create:
- determination
- curiosity
- annoyance
- humiliation
- dread
- learned helplessness
- numb repetition

Name the most likely felt response and why.

### 6. Check fairness and attribution inside failure
Ask:
- does the player understand why they failed?
- does the punishment feel deserved?
- does the loop preserve a sense of control?
- does repeated failure harden into external blame?

If needed, call out connections to attribution, flow, or fairness problems without fully re-running those audits.

### 7. Identify failure-loop archetypes
Useful patterns include:
- **learning loop** - fast retry, high clarity, strong adaptation
- **grindback loop** - too much rebuild between real attempts
- **shame loop** - public or ego-threatening failure with weak learning
- **attrition loop** - death by repeated low-grade exhaustion
- **helpless loop** - repeated failure without better hypotheses
- **mastery loop** - hard punishment justified by high clarity and strong growth

Classify the current loop and say whether that shape suits the game.

### 8. Convert findings into design changes
For each issue, specify:
- **Failure-loop problem**
- **Why it hurts retry willingness**
- **Suggested change**
- **Expected effect on learning and motivation**

Examples:
- unclear death cause -> improve post-failure feedback and telegraphing
- long rebuild before retry -> shorten setup or preserve more state
- punishment too severe for early game -> soften cost during learning phases
- nothing learned from failure -> increase legibility or give comparative feedback

## Response structure

Use this structure unless the user asks for something else:

### Audit Target
- ...

### Failure Loop Summary
- ...

### Loss, Learning, and Retention
- ...

### Re-entry Friction
- ...

### Emotional Effect
- ...

### Failure Loop Type
- ...

### Recommendations
1. ...
2. ...
3. ...

### Minimal Fix
- ...

## Fast mode

Use this quick pass when speed matters:
- What happens right after failure?
- What does the player lose?
- What do they learn?
- How fast can they make a better next attempt?
- What one change would most improve retry willingness?

## Usage notes

This audit is especially useful for:
- boss retries
- roguelite runs
- puzzle resets
- stealth mission failure
- onboarding deaths
- challenge events
- progression gates
- harsh economy setbacks
- difficult action-combat loops

Common patterns to watch for:
- many games punish more than they teach
- retry friction is often more damaging than raw difficulty
- harsh failure can work if clarity and re-entry speed are strong
- meta-progression can rescue a hard failure loop, but cannot fully compensate for opaque failure
- if the player dreads the retry more than the challenge itself, the loop is probably broken

## Working principle

Failure should create a better next attempt, not just a worse mood.

Use this skill to test whether the design turns defeat into momentum or just burns player trust and energy.