---
name: game-design-player-values-mapper
description: Infer a player's underlying values and motivational priorities from behavior, then translate those into design implications. Use when designing personalization, segmentation, dynamic guidance, live-ops targeting, adaptive missions, re-engagement strategies, or feature prioritization; when behavior suggests that what players actually care about differs from what the design assumes; or when a team needs a behavior-first player profile rather than a demographic or archetype-only model.
---

# Game Design Player Values Mapper

Map observed player behavior to likely underlying value priorities, then use that map to infer what kinds of goals, rewards, content, or framing are most likely to resonate.

Use this skill when the team needs to understand not just what players do, but what those choices imply about what they care about.

## Core principle

Behavior is not random. It is preference made visible.

Players reveal their values through repetition, avoidance, investment, and attention. The goal is not to assign a rigid personality label, but to infer the motivational structure most likely driving current behavior and use that to improve design alignment.

## What to produce

Generate:
1. **Observed behavior summary** - what the player consistently does, ignores, and invests in
2. **Value map** - likely dominant, secondary, and weak values
3. **Confidence notes** - how strong or ambiguous each inference is
4. **Tensions or contradictions** - where behavior suggests mixed motives or blocked values
5. **Design implications** - what systems, content, messaging, goals, or monetization surfaces are likely aligned or misaligned
6. **Segment hypothesis** - what kind of player pattern this most resembles in practical design terms
7. **Recommendations** - what to emphasize, reframe, personalize, or stop pushing

## Value framework

Map behavior to these value dimensions:

- **Efficiency / Optimization**
- **Progression / Growth**
- **Aesthetics / Expression**
- **Collection / Completion**
- **Social Recognition / Status**
- **Experimentation / Discovery**
- **Narrative / Meaning**

You may add a clearly justified extra value if the case demands it, but do not bloat the framework casually.

## Process

### 1. Gather behavior signals

List concrete observed behaviors.

Possible sources:
- build patterns
- resource spending
- session frequency and duration
- event participation
- feature engagement
- purchase behavior
- social behavior
- what the player returns to repeatedly
- what the player ignores despite obvious rewards

Write:
- **Repeated behaviors**
- **Avoided behaviors**
- **Investment patterns**

### 2. Map behaviors to likely value signals

Translate behavior into value hypotheses.

Examples:
- min-maxing production chains -> Efficiency / Optimization
- constant upgrading and rushing unlocks -> Progression / Growth
- decorating, styling, curating loadouts -> Aesthetics / Expression
- chasing every item or badge -> Collection / Completion
- caring about ranks, cosmetics, visibility -> Social Recognition / Status
- trying odd builds or niche tools -> Experimentation / Discovery
- following lore, theme, faction identity, story arcs -> Narrative / Meaning

Important: many behaviors can map to more than one value. Do not overclaim certainty.

### 3. Weight the value profile

Do not force fake precision. The goal is a useful profile, not pseudo-scientific certainty.

Assign rough weight levels such as:
- High
- Medium
- Low

Or if needed:
- Dominant
- Secondary
- Weak
- Absent

Also note confidence:
- high confidence
- medium confidence
- low confidence

Use this format:

| Value | Weight | Confidence | Evidence |
|---|---|---|---|
| ... | ... | ... | ... |

### 4. Detect tensions and blocked values

Look for contradictions.

Examples:
- optimization-driven player engaging with decoration only because progression forces it
- status-seeking player avoiding competition because the failure cost feels humiliating
- progression-oriented player not spending because they distrust the offer structure
- discovery-oriented player repeating safe loops because experimentation is too punished

Ask:
- is this a real mixed-value profile?
- or is one value being blocked by system design?

### 5. Infer likely design alignment

Answer:
- what currently motivates this player most?
- what kinds of content or objectives will likely land well?
- what incentives are probably weak for this player?
- where is the game asking for a value the player does not strongly hold?
- what part of the experience is likely causing silent disengagement?
- what messaging, reward framing, or mission framing is most likely to resonate?

### 6. Form a practical segment hypothesis

Translate the value map into a practical design-facing player pattern.

Examples:
- efficiency-first optimizer
- completionist collector with moderate status drive
- expressive builder with weak progression urgency
- growth-focused grinder with low experimentation tolerance
- discovery-oriented tinkerer blocked by punishment

This is not meant to replace deeper persona work. It is a compact operational summary that helps teams act.

### 7. Recommend design actions

Translate the value map into actions such as:
- personalize mission framing
- surface a different kind of goal
- target events/offers more intelligently
- reduce pressure toward misaligned systems
- give better tools to the dominant value type
- redesign progression framing for the current segment
- change how rewards are explained, not just what rewards are given
- stop over-serving a secondary value while neglecting the dominant one

## Response structure

### Observed Behavior Summary
- ...

### Player Value Map
| Value | Weight | Confidence | Evidence |
|---|---|---|---|
| ... | ... | ... | ... |

### Dominant Values
- ...

### Secondary Values
- ...

### Tensions / Contradictions
- ...

### Segment Hypothesis
- ...

### Design Implications
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode

Use this quick pass when speed matters:
- what does the player repeatedly choose?
- what do they ignore?
- what does that imply they value?
- what is the strongest mismatch between the player's values and the game's current asks?
- what practical segment hypothesis best describes this player?
- what should the design emphasize or stop emphasizing for this player?

## Working principle

A player rarely says their values directly.
They leak them constantly through what they pursue, what they skip, and what they are willing to suffer for.
