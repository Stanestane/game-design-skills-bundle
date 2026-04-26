---
name: game-design-thinking-fast-and-slow-audit
description: Audit a game, feature, combat system, economy loop, onboarding flow, puzzle, UI, or design proposal through the lens of fast versus slow thinking inspired by Thinking, Fast and Slow. Use when evaluating whether a design relies on rapid intuitive judgment or deliberate analytical reasoning, whether the intended mode matches the actual demand, where cognitive overload or under-stimulation appears, or how badly the design handles shifts between instinctive and reflective play.
---

# Game Design Thinking Fast and Slow Audit

Audit a design by asking what kind of thinking it demands from the player, when, and whether that demand is appropriate.

Use this skill when a proposal sounds good in the abstract but may be mismatched to the kind of cognition it actually requires. The goal is to identify where the design leans on fast, intuitive, low-deliberation processing versus slow, analytical, effortful reasoning, and where the transition between those modes becomes awkward, exhausting, misleading, or strategically dead.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

Players do not think in one uniform way.

Some situations ask for:
- rapid pattern recognition
- instinctive response
- snap prioritization
- fluent repetition

Other situations ask for:
- deliberate comparison
- explicit planning
- rule-based reasoning
- careful tradeoff evaluation

Neither mode is automatically better. The important questions are:
- which mode the design is asking for
- whether that suits the fantasy and pacing
- whether the player is being supported properly
- whether the handoff between modes is clean

## Fast and slow lenses

### Fast-mode thinking
Typical qualities:
- intuitive
- automatic
- rapid
- pattern-based
- low-deliberation
- emotionally immediate

In game terms, this often appears in:
- action combat
- dodging, aiming, timing, rhythm
- snap tactical prioritization
- recognition of familiar board states
- habitual session actions
- high-tempo moment-to-moment play

### Slow-mode thinking
Typical qualities:
- reflective
- effortful
- explicit
- comparative
- planning-heavy
- cognitively expensive

In game terms, this often appears in:
- deckbuilding and loadout decisions
- long-horizon economy planning
- puzzle decomposition
- route planning
- team composition
- optimization and meta decisions

## What to produce

Generate:
1. **Thinking-mode profile** - whether the design primarily demands fast thinking, slow thinking, or a layered mix
2. **Mode-fit diagnosis** - whether the required thinking mode matches the fantasy, pacing, and audience
3. **Transition diagnosis** - where the design shifts between fast and slow modes, and whether those handoffs work
4. **Cognitive risk map** - where the design creates overload, confusion, autopilot deadness, or false depth
5. **Design actions** - what to simplify, deepen, pace differently, surface more clearly, or separate

## Process

### 1. Define the audit target
Clarify:
- what exact game, feature, loop, or proposal is being audited
- whether the audit is for minute-to-minute play, meta systems, onboarding, or the full experience
- what player segment matters most

Write:
- **Audit target**
- **Scope**
- **Primary player segment**

### 2. Identify the dominant thinking demand
Ask:
- what does the player have to notice, decide, remember, and prioritize?
- how much time do they have to do it?
- are they reacting from fluency or stopping to reason explicitly?
- what mistakes come from speed versus what mistakes come from misunderstanding?

Classify the dominant demand as:
- mostly fast-mode
- mostly slow-mode
- mixed, with one dominant
- deeply hybrid

### 3. Map where each mode appears
Break the experience into phases or layers such as:
- onboarding
- moment-to-moment play
- build/loadout decisions
- economy or progression planning
- social/coordination layer
- end-of-run reflection

For each phase, identify:
- **Thinking mode demanded**
- **Why that mode is required**
- **Whether the player has enough support**

Use this format:

| Phase or system | Thinking mode | Demand level | Notes |
|---|---|---|---|
| ... | Fast / Slow / Mixed | Low / Med / High | ... |

### 4. Check fit between mode and fantasy
Ask:
- does the cognitive demand support the intended fantasy?
- is the game claiming flow, mastery, panic, elegance, command, coziness, or brilliance?
- does the required thinking mode reinforce that promise or betray it?

Examples:
- a fantasy of fluid sword mastery should not constantly hard-stop into spreadsheet reasoning
- a fantasy of careful grand strategy should not bury important choices inside twitch pressure
- a cozy planning game can tolerate slow thought, but not exhausting ambiguity

### 5. Diagnose fast-mode failure patterns
Look for:
- reaction demands too fast for the available clarity
- hidden information inside high-speed play
- too many simultaneous priorities
- snap judgments punished by information the player could not reasonably process
- UI that slows recognition instead of supporting it
- panic without readable action value

### 6. Diagnose slow-mode failure patterns
Look for:
- analysis burden too high for the payoff
- false complexity with obvious dominant answers
- too many variables to compare meaningfully
- long planning phases that are cognitively costly but emotionally flat
- systems that imply deep strategy but resolve shallowly
- excessive memory burden or bookkeeping

### 7. Diagnose transition failures between modes
This is often where designs get ugly.

Look for:
- abrupt switches from high-speed execution to deep planning without recovery time
- long slow-mode interruptions that kill fast-mode momentum
- fast-mode punishment for choices made in poorly supported slow-mode spaces
- slow-mode systems whose consequences only appear in frantic real-time moments
- a requirement to do deep reasoning under time pressure when the interface does not support it

Ask:
- where does the player shift modes?
- is the shift clean, intentional, and well-signaled?
- does the game give enough time, framing, and UI support for the new mode?

### 8. Identify audience mismatch and expertise effects
Ask:
- does this design feel intuitive to experts but exhausting to new players?
- does it ask casual players for tournament-level reasoning?
- does it flatten expert depth into autopilot?
- does the intended audience actually want this blend of cognition?

A system can be good for one audience and terrible for another because of thinking-mode mismatch alone.

### 9. Convert findings into design changes
For each major issue, specify:
- **Thinking-mode problem**
- **Why it hurts the experience**
- **Suggested change**
- **Expected effect**

Examples:
- reduce simultaneous fast-mode demands -> improves readability and decision confidence
- move some choices out of real-time pressure -> supports better slow-mode reasoning
- compress false-complexity planning layers -> preserves depth while reducing fatigue
- add clearer state framing before mode shifts -> reduces cognitive whiplash

## Response structure

Use this structure unless the user asks for something else:

### Audit Target
- ...

### Thinking-Mode Profile
- ...

### Fast-Mode Demands
- ...

### Slow-Mode Demands
- ...

### Transition and Handoff Issues
- ...

### Audience and Expertise Fit
- ...

### Recommendations
1. ...
2. ...
3. ...

### Minimal Fix
- ...

## Fast mode

Use this quick pass when speed matters:
- Is this mainly asking for instinctive play or analytical play?
- Does that fit the fantasy and pacing?
- Where is the worst mismatch?
- Where does the player switch modes?
- What one change would most improve the cognitive fit?

## Usage notes

This audit is especially useful for:
- action/strategy hybrids
- real-time systems with heavy pre-planning
- economy layers attached to fast gameplay
- onboarding for cognitively demanding games
- puzzles embedded inside otherwise reactive experiences
- proposal reviews where the cognitive demand is still fuzzy
- UI-heavy systems that may be hiding slow thought inside supposed fast play

Common patterns to watch for:
- many proposals accidentally ask for more slow thinking than their fantasy can sustain
- some designs confuse time pressure with depth
- some planning layers create the appearance of strategy without meaningful choice
- many frustrating systems are really bad handoffs between fast and slow modes
- expert fluency can hide a beginner-facing cognitive disaster

## Working principle

A strong design does not just ask the player to think. It asks them to think in the right way, at the right time, with the right support.

Use this skill to identify whether the proposal's cognitive demands are elegant, mismatched, exhausting, or fake-deep.