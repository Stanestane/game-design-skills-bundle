---
name: game-design-design-pillars-extractor
description: Extract 3 to 5 actionable design pillars from a game, feature, loop, or system based on what the design actually rewards and prioritizes. Use when a team can describe mechanics but cannot clearly articulate the principles those mechanics serve, when pillars are vague, generic, or contradictory, or when you need a sharper set of tradeoff-driven pillars that can guide decisions and cut features.
---

# Game Design Design Pillars Extractor

Extract the real pillars a design is built around, not the polite slogans attached to it.

Use this skill when a team has a pile of mechanics, references, and ambitions but no sharp articulation of what the design actually prioritizes. The goal is to reverse-engineer 3 to 5 actionable pillars from the game's systems, loops, and tradeoffs.

Good pillars are directional. They help decide what to keep, what to cut, and what kinds of changes are off-brand. Bad pillars are just nice words wearing capital letters.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

A meaningful design pillar does two things:
- names what the design is trying hard to deliver
- implies what the design is willing to sacrifice to deliver it

If a pillar does not create a constraint, it is not a pillar yet.

## What to produce

Generate:
1. **Extracted pillars** - 3 to 5 clear, testable pillars
2. **Support map** - which systems actually reinforce each pillar
3. **Conflict map** - where systems or candidate pillars push against each other
4. **Missing or weak dimensions** - important priorities that are undefined, accidental, or under-supported
5. **Decision guidance** - which pillars should dominate future choices

## Process

### 1. Define the extraction target
Clarify:
- what exact game, feature set, or loop is being analyzed
- whether the pillars are for the whole product or a subset
- whether you are extracting current pillars or intended pillars

Write:
- **Extraction target**
- **Scope**
- **Current versus intended state**

### 2. Map the dominant design behaviors
Look at:
- core loop
- repeat decisions
- reward structure
- punishment structure
- progression model
- randomness profile
- pacing
- agency level
- social or solo emphasis

Ask:
- What does the design repeatedly encourage the player to do?
- What kinds of decisions matter most?
- What behaviors are rewarded, tolerated, or ignored?

### 3. Infer the implicit priorities
Ask:
- What is this design optimizing for in practice?
- What is it willing to make harder, slower, riskier, narrower, or less accessible in order to preserve that?
- Which experiences seem central rather than incidental?

This is where you move from feature description to design intention.

### 4. Detect tradeoffs and contradictions
Look for places where:
- one system rewards patience while another rewards speed
- one feature pushes mastery while another floods the loop with noise
- one layer promises freedom while another funnels players into one dominant path
- a supposed pillar is not actually reinforced by gameplay

Do not hide contradictions. Surface them.

### 5. Synthesize 3 to 5 pillars
For each pillar, provide:
- **Name**
- **What it means**
- **What it prioritizes**
- **What it sacrifices**
- **Which systems support it**

Prefer short, sharp names that imply a stance, such as:
- Controlled Chaos
- Readable Mastery
- High-Risk Commitment
- Expressive Preparation
- Ruthless Momentum

Avoid vague filler such as:
- Fun
- Immersion
- Engagement
- Quality
- Innovation

### 6. Identify missing or weak pillars
Ask:
- Which important experience dimensions are currently accidental or under-defined?
- Which design goals are talked about but not structurally supported?
- Which player promises are present in language but absent in systems?

### 7. Turn the pillars into decision guidance
State:
- which pillar should win when tradeoffs appear
- which features do not support any pillar and should be challenged
- which future ideas fit or violate the extracted set

## Response structure

Use this structure unless the user asks for something else:

### Extraction Target
- ...

### Extracted Design Pillars
1. ...
2. ...
3. ...

For each pillar:
- Meaning: ...
- Prioritizes: ...
- Sacrifices: ...
- Supporting systems: ...

### Conflicts and Contradictions
- ...

### Missing or Weak Pillars
- ...

### Decision Guidance
1. ...
2. ...
3. ...

## Fast mode

Use this quick pass when speed matters:
- What does the design reward most consistently?
- What is it clearly willing to sacrifice?
- What three priorities best describe the actual game?
- Which feature does not belong?

## Usage notes

This extractor is especially useful for:
- early concept framing
- preproduction alignment
- pitch cleanup
- feature triage
- post-prototype coherence checks
- making design docs less hand-wavy

Common patterns to watch for:
- teams often confuse feature lists with pillars
- a pillar that cannot say "no" is not doing any work
- contradictory pillars usually reflect unresolved design conflict, not healthy nuance
- the strongest pillar should be obvious in repeated gameplay, not just in slide decks
- if every pillar sounds universally positive, they are probably too generic to guide decisions

## Working principle

Mechanics reveal priorities even when the team does not.

Use this skill to extract the principles the design is actually living by, then decide whether those principles are worth keeping.