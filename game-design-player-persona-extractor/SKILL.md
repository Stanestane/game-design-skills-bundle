---
name: game-design-player-persona-extractor
description: Extract the ideal player persona and anti-persona for a game, feature, loop, or progression structure based on the design itself. Use when a team can describe mechanics but cannot clearly articulate who the design is truly for, which player motivations and tolerances it suits, which players it will alienate, or how audience fit should shape design decisions. Focus on behavioral and motivational personas first, and optionally add demographic or market-fit hypotheses when the user explicitly asks for that layer.
---

# Game Design Player Persona Extractor

Extract who a design is actually built for.

Use this skill when a team can describe systems, loops, and mechanics, but not the kind of player who will love them, tolerate them, or bounce off them. The job is not to invent a fake marketing avatar. The job is to infer the player profile implied by the design.

Focus on behavior, motivation, tolerance, learning style, and emotional appetite. Avoid demographic fluff unless the user explicitly asks for it.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.
Read `references/demographic-research-notes.md` when the user explicitly wants demographic support, market validation, or publisher-facing audience framing.

## Core principle

A game becomes sharper when it serves a specific kind of player extremely well instead of vaguely trying to work for everyone.

A useful persona does three things:
- identifies who the design delights
- identifies who the design frustrates or excludes
- implies concrete design choices

If the resulting persona could fit almost any game, it is too weak to matter.

## What to produce

Generate:
1. **Ideal player persona** - the player this design best serves
2. **Anti-persona** - the player most likely to reject or churn from it
3. **Behavior profile** - how the player approaches play, learning, and decisions
4. **Emotional profile** - what they want to feel and what breaks the deal
5. **Design implications** - what the design must emphasize, protect, and avoid for this audience
6. **Optional demographic layer** - only when explicitly requested, add likely demographic or market-fit hypotheses that support the behavior-first persona rather than replacing it
7. **Optional market audience summary** - when requested for pitch, publishing, or strategy use, convert the persona into a concise audience-facing summary with demographic overlap, comparable-title signals, and confidence notes

## Process

### 1. Define the extraction target
Clarify:
- what exact game, feature, or loop is being analyzed
- whether the persona is for the whole product or only one experience slice
- what known constraints already shape audience fit

Write:
- **Extraction target**
- **Scope**
- **Known constraints**

### 2. Read the design for behavioral signals
Look at features such as:
- difficulty level
- randomness level
- pacing and session length
- agency level
- punishment severity
- progression structure
- strategic depth
- repetition tolerance
- required patience, experimentation, or precision

Ask:
- What kind of player will enjoy making these decisions repeatedly?
- What kind of frustration is this design asking the player to tolerate?
- Does it reward mastery, experimentation, social play, expression, optimization, calm routine, or high tension?

### 3. Infer the core motivation profile
Common motivation buckets include:
- mastery and skill growth
- experimentation and discovery
- optimization and efficiency
- competition and status
- expression and creativity
- narrative curiosity
- collection and completion
- comfort, ritual, and low-pressure progress

State which motivations the design strongly serves and which it serves poorly.

### 4. Infer the tolerance profile
Judge what the implied player can comfortably tolerate in terms of:
- difficulty
- repetition
- randomness
- ambiguity
- failure frequency
- delayed rewards
- long sessions or short bursts
- social friction
- optimization pressure

This often reveals the anti-persona more clearly than the positive persona does.

### 5. Describe the play style and learning style
Clarify how the ideal player tends to behave:
- cautious or impulsive
- planner or improviser
- systems learner or fantasy chaser
- repetition-based learner or novelty seeker
- optimizer or role-player
- solo-focused or socially motivated

Write this as behavior, not vague adjectives.

### 6. Define emotional expectations
Ask:
- What does this player want to feel regularly?
- What kind of tension is enjoyable to them?
- What kind of frustration will they accept?
- What kind of frustration will feel like betrayal?

### 7. Define the anti-persona
State clearly who this is not for and why.

Avoid generic anti-personas like "people who do not like games." Instead name the specific mismatch:
- wants predictable progression but design thrives on variance
- wants low-pressure comfort but loop demands intense optimization
- wants expressive freedom but systems narrow into one dominant path

### 8. Convert the persona into design implications
For each important persona trait, specify:
- **Trait or expectation**
- **What the design must do**
- **What the design should avoid**

Examples:
- experimental learner -> outcomes must be legible enough to support testing
- high variance tolerance -> randomness must still feel interpretable
- low repetition tolerance -> loop needs novelty density
- mastery-driven audience -> failure must teach, not merely punish

### 9. Add the optional demographic layer only when asked
Use this step only if the user explicitly wants demographic data, audience hypotheses, or market-facing persona framing.

Keep the logic in this order:
1. extract the behavioral persona first
2. infer which demographic clusters are most likely to overlap with that persona
3. if needed, use current market or genre data to test whether those demographic guesses are plausible

Demographics should support the behavioral read, not drive it.

When asked for this layer:
- clearly label it as **hypothesis**, **market signal**, or **supporting demographic fit**, not as certainty
- prefer ranges and segments over fake precision
- distinguish between **likely demographic overlap** and **required target audience**
- if external market validation is useful, search for recent player-demographic data for the genre, platform, region, or adjacent titles
- note when the available data is broad market data rather than title-specific evidence

Useful demographic dimensions may include:
- age bands
- platform skew
- region
- play frequency
- spending profile
- genre familiarity
- solo versus social preference

Avoid garbage personas like:
- "25-year-old male who likes fun"
- fabricated lifestyle backstory with no design relevance
- demographic claims that contradict the behavior profile

If evidence is weak, say so directly.

### 10. Use web research mode when the user wants validation
Use web research mode when the user asks for demographic validation, audience evidence, market support, or current player data.

In web research mode:
- search for recent data first, preferably within the last 2 to 4 years when possible
- prioritize reputable sources such as platform-holder reports, publisher reports, ESA, Newzoo, Statista-style summaries if clearly cited, GDC talks, Steam or console ecosystem reports, and credible market analyses
- prefer genre-, platform-, or region-specific data over broad "all gamers" data when the design is niche
- separate hard evidence from inference
- cite what the evidence actually supports rather than stretching it

Useful web-research questions:
- what demographics over-index in this genre?
- what platform and age skew is reported for comparable play patterns?
- what monetization or session-length patterns are common in this audience?
- what regional differences matter?

When evidence is mixed, show the tension instead of pretending one clean answer exists.

### 11. Use title-comparison mode when comparable games matter
Use title-comparison mode when the user asks for comp titles, adjacent audience fit, genre neighbors, or evidence from similar games.

In title-comparison mode:
- identify 2 to 5 comparable titles, not a giant dump
- choose comps based on audience behavior, play pattern, and fantasy, not just surface theme
- explain why each title is a useful comparison
- infer likely audience overlap from those comps carefully
- note where a comp is commercially useful but behaviorally misleading

For each comparison, prefer:
- **Comparable title**
- **Why it overlaps**
- **Likely shared audience traits**
- **Important difference**

### 12. Use market-audience summary mode for pitch decks and publisher-facing work
Use this mode when the user wants a concise audience summary for pitch decks, publishing conversations, strategy docs, or greenlight materials.

In market-audience summary mode:
- compress the behavior-first persona into a short, decision-useful audience summary
- include the strongest likely demographic overlap only if it helps the audience case
- mention comparable titles if they strengthen the argument
- state confidence level and major uncertainty
- avoid pretending the persona itself is validated market truth unless actual evidence was reviewed

A good market-audience summary should answer:
- who this game is mainly for
- why that audience is a fit
- what adjacent audiences may also convert
- what audience mismatches or commercial risks are most important

## Response structure

Use this structure unless the user asks for something else:

### Extraction Target
- ...

### Ideal Player Persona
- ...

### Core Motivations
- ...

### Tolerance Profile
- ...

### Play Style and Learning Style
- ...

### Emotional Expectations
- ...

### Anti-Persona
- ...

### Design Implications
1. ...
2. ...
3. ...

### Optional Demographic Layer
- Likely demographic overlap: ...
- Confidence: ...
- Supporting signal or market evidence: ...

### Optional Comparable Titles
- ...

### Optional Market Audience Summary
- ...

## Fast mode

Use this quick pass when speed matters:
- Who is this game perfect for?
- What frustration are they willing to tolerate?
- What kind of player will hate this?
- What one design choice matters most for the ideal audience?
- If demographic output was requested, what demographic overlap is plausible and how confident are we?
- If market framing was requested, which comparable titles and audience signals best support the case?

## Usage notes

This extractor is especially useful for:
- early concept definition
- pillar clarification
- feature targeting
- tuning difficulty and punishment
- checking audience fit after prototypes
- aligning design, product, and marketing language
- preparing audience sections for pitch decks and publisher conversations
- creating behavior-first audience summaries supported by market evidence

Common patterns to watch for:
- many teams describe mechanics first and audience second, which hides conflicts
- a design can accidentally target incompatible personas at once
- personas built from demographics are usually too weak to guide design
- demographics are useful as a supporting layer, not as the foundation of the persona
- the anti-persona is often more useful than the persona for clarifying tradeoffs
- if everyone sounds like a fit, the design target is still foggy

## Working principle

A design always chooses its player, even when the team refuses to admit it.

Use this skill to make that choice visible and actionable.