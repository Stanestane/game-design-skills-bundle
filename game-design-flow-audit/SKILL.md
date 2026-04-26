---
name: game-design-flow-audit
description: Audit a game, feature, level sequence, combat loop, progression curve, onboarding path, event structure, or return-player journey through the lens of Flow theory. Use when evaluating whether challenge and skill stay aligned over time, diagnosing boredom, anxiety, frustration spikes, difficulty cliffs, dead zones, or pacing drift, or identifying where a design stops feeling absorbing and starts feeling exhausting or empty.
---

# Game Design Flow Audit

Audit a design by asking whether it keeps players in a productive state of engagement over time.

Use this skill to evaluate whether challenge rises in step with player skill, where the experience becomes boring or overwhelming, and which moments break the player's sense of momentum. Focus on temporal experience and pacing, not static difficulty labels.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

Flow emerges when challenge and player skill stay in meaningful tension and grow together over time.

Typical failure shapes:
- **Challenge above skill** -> anxiety, confusion, frustration
- **Skill above challenge** -> boredom, autopilot, disengagement
- **No visible skill growth** -> stagnation, flatness, drop-off

A flow audit is not just about whether the game is hard. It is about whether the game keeps giving the player something they can meaningfully rise to.

## What to produce

Generate:
1. **Flow curve summary** - the overall engagement shape over time
2. **Phase breakdown** - where the player is in flow, boredom, or anxiety
3. **Breakpoints** - the exact moments where flow is likely to break
4. **Skill-versus-challenge diagnosis** - what is misaligned and why
5. **Design actions** - specific changes to restore momentum and absorption

## Process

### 1. Define the audit target
Clarify:
- what part of the experience is being audited
- what player segment matters most
- what time window matters most

Write:
- **Audit target**
- **Player segment**
- **Relevant timeline**

### 2. Map the experience over time
Break the target into phases such as:
- first 30 seconds
- first 5 minutes
- first session
- early mastery
- midgame
- endgame
- return-player re-entry

For each phase, identify:
- what the player is trying to do
- what the game asks of them
- what counts as success
- how much support exists

### 3. Identify the required skill axes
Separate the skill demands into useful buckets such as:
- mechanical execution
- tactical judgment
- strategic planning
- system comprehension
- attention management
- social coordination

Ask:
- What does the player actually need to be good at here?
- Which skills are newly introduced, tested, or combined?
- Which skills are ignored or overemphasized?

### 4. Judge challenge versus skill in each phase
For every phase, evaluate:
- current challenge level
- expected player skill level
- resulting flow state

Use this format:

| Phase | Key challenge | Expected player skill | Likely state |
|---|---|---|---|
| ... | ... | ... | Flow / Boredom / Anxiety |

### 5. Identify breakpoints and transition failures
Look for moments where:
- the game asks for mastery before teaching
- difficulty spikes without warning
- complexity stacks too quickly
- the loop becomes repetitive without new pressure
- rewards stall while demands rise
- the player loses sight of goals or progress

Name the specific handoff or step where flow breaks, not just the general area.

### 6. Evaluate pacing and learning support
Assess whether the design:
- introduces one meaningful complexity at a time
- gives feedback fast enough to support learning
- varies challenge without becoming chaotic
- creates enough novelty to prevent boredom
- allows recovery after failure
- respects differences between new, intermediate, and expert players

### 7. Convert findings into design changes
For each issue, specify:
- **Breakpoint**
- **Why flow breaks there**
- **Suggested change**
- **Expected effect on the curve**

Examples:
- reduce early enemy density -> lowers anxiety spike
- delay second-system introduction -> reduces overload
- add optional mastery pressure later -> reduces boredom plateau
- improve re-entry summary -> restores flow for returning players

## Response structure

Use this structure unless the user asks for something else:

### Audit Target
- ...

### Flow Curve Summary
- ...

### Phase Breakdown
- ...

### Critical Breakpoints
- ...

### Skill vs Challenge Analysis
- ...

### Segment Sensitivity
- ...

### Recommendations
1. ...
2. ...
3. ...

### Minimal Fix
- ...

## Fast mode

Use this quick pass when speed matters:
- Where is the player likely bored?
- Where are they likely overwhelmed?
- What is the first major flow break?
- Which skill is under-supported?
- What one change would most improve challenge-skill alignment?

## Usage notes

This audit is especially useful for:
- FTUE and onboarding
- first combat sequences
- midgame pacing drift
- live event structures
- difficulty progression
- mission sequencing
- roguelite run structure
- endgame mastery loops
- return-player catch-up experiences

Common patterns to watch for:
- early spikes create churn before skill identity forms
- flat midgames create low-energy retention even with decent progression
- too much support can prevent anxiety but still create boredom
- raw stat inflation often breaks flow worse than richer decision-making does
- the same challenge can produce flow for experts and anxiety for newcomers

## Working principle

Players stay absorbed when the game keeps saying, "you can stretch a bit further."

Use this skill when a design feels off in motion: too flat, too spiky, too tiring, or just mysteriously less compelling than it should be.