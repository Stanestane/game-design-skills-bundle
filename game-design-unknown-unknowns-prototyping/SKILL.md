---
name: game-design-unknown-unknowns-prototyping
description: Detect unknown unknowns in game design and decide what to prototype before committing to production. Use when a feature concept feels promising but underdefined, when the team disagrees about the real design problem, when a mechanic seems interesting but the source of interest is unclear, when a concept risks premature production commitment, or when the team needs to determine what should be prototyped, in what order, and why.
---

# Game Design Unknown Unknowns Prototyping

Use prototyping to discover what actually needs to be learned.

This skill helps map uncertainty, identify likely blind spots, frame prototype questions, choose the cheapest useful prototype type, sequence tests, and define stop criteria. Keep the work practical and decision-oriented. Do not prototype to mimic production. Prototype to expose uncertainty.

## Core principle

**Preproduction handles known unknowns. Prototyping explores unknown unknowns.**

That distinction matters.
- **Known unknowns** are questions the team already knows to ask.
- **Unknown unknowns** are hidden design problems, emergent opportunities, and unexpected interactions that only become visible through testing.

Therefore:
- do not prototype to mimic production
- prototype to expose uncertainty
- prototype to discover what the game might actually be

## Knowledge quadrants

Use these four buckets to classify the state of understanding around a concept.

### 1. Known knowns
Things the team is already confident about.

### 2. Known unknowns
Things the team already knows it needs to answer.

### 3. Unknown knowns
Things the team implicitly knows but has not surfaced.

### 4. Unknown unknowns suspects
Things the team cannot yet name directly, but can infer are likely hiding in the concept.

Read `references/quadrants-and-hiding-places.md` when you need examples of each quadrant or a list of common hiding places for unknown unknowns.

## What to produce

Generate a prototyping plan with these outputs:

1. **Concept framing** - what the team thinks the idea is, and where it is still foggy
2. **Uncertainty map** - what is known, suspected, and unexplored
3. **Prototype questions** - what must be learned through making and testing
4. **Prototype sequence** - what order to test things in, and how each test informs the next
5. **Stop criteria** - when to stop exploring and move toward preproduction or production framing
6. **Decision record** - what was learned, what died, and what stronger direction emerged

## Process

### 1. Frame the design space

Clarify the current idea and its uncertainty surface.

Ask:
- What is the idea as currently understood?
- What part is conceptually exciting?
- What part is still vague?
- Which part is likely illusion rather than substance?
- Which assumptions are carrying the concept?
- What are we calling the feature today, and is that label prematurely narrowing thinking?

Write:
- **Current concept**
- **Why it seems promising**
- **Why it is still unclear**
- **Assumptions carrying the concept**

### 2. Build an uncertainty map

Map the concept using the four quadrants.

Use this format:

| Quadrant | Items |
|---|---|
| Known knowns | ... |
| Known unknowns | ... |
| Unknown knowns | ... |
| Unknown unknowns suspects | ... |

Important note: the last row is deliberately phrased as **unknown unknowns suspects**. True unknown unknowns cannot be listed directly. They can only be inferred from where hidden uncertainty is likely to live.

### 3. Convert fog into prototype questions

Turn uncertainty into learning objectives.

Rule: a prototype question should describe what must be learned, not what must be built.

Good prototype questions often sound like:
- Can players understand X without explanation?
- Does X create a stronger feeling of Y?
- What breaks first when X is layered with Z?
- Does X reduce friction or merely relocate it?
- Is the fun in A, or in the choice around A?
- What emergent behavior appears when players optimize X?
- What new problem appears after the obvious problem is removed?

Read `references/prototype-question-patterns.md` when you want more examples of strong versus weak prototype questions.

Write:
- **Prototype questions**

### 4. Identify the right prototype type

Choose the cheapest artifact that can expose the uncertainty.

Do not default to a playable digital prototype. Choose the medium based on the unknown.

Prototype types:
- **Experience prototype** - for feel, rhythm, pacing, emotional response
- **Interaction prototype** - for UI comprehension, decision speed, readability, input behavior
- **Systems prototype** - for simulation, economy, balance, loop interaction
- **Content pipeline prototype** - for production feasibility
- **Wizard-of-Oz or fake-backend prototype** - for testing behavior before full implementation

Use this format:

| Prototype Question | Best Prototype Type | Fidelity Needed | Why |
|---|---|---|---|

Read `references/prototype-types.md` when you need examples of what each type is best at exposing.

### 5. Sequence prototypes as a branching map

Order prototypes so each one clarifies the next one.

A prototype should do at least one of the following:
- kill an idea
- stabilize a baseline
- reveal a stronger direction
- expose a deeper question

Track prototype nodes using these state labels:
- **Dead end** - discard, but capture the lesson
- **Baseline** - stable enough to build on
- **Branch trigger** - revealed a new avenue worth testing
- **Production candidate** - sufficiently understood to move forward

Use this format:

| Prototype Node | Intended Learning | Result | Next Branch | State |
|---|---|---|---|---|

### 6. Detect hidden prototype needs

Ask what is not being prototyped because the team is overfocused on the visible feature.

Diagnostic prompts:
- Are we prototyping the visible feature instead of the invisible feeling?
- Are we testing implementation shape before testing player value?
- Are we arguing over solutions before defining the discovery question?
- Are we trying to answer multiple uncertainties with one bloated prototype?
- Are we protecting the original concept instead of letting the prototype challenge it?
- What would we test if we assumed the current pitch is wrong?
- Which part of the concept is most likely to transform into something else during prototyping?

Read `references/anti-patterns.md` for common prototyping failure modes and how to spot them.

### 7. Specify stop criteria

Define when to stop exploring and move into preproduction or production framing.

Stop when there is enough clarity on:
- core player interaction
- source of fun or value
- major design risks
- baseline UX understanding
- technical feasibility envelope
- a production-worthy direction

Do not wait for:
- complete certainty
- every edge case
- every tuning question answered
- every alternate branch explored

Write:
- **Stop criteria met when**
- **Still not clear enough if**

### 8. Produce a prototype brief

For each prototype, write a compact brief that ties the work to a decision.

Use this format:

**Prototype name**:  
**What this is trying to learn**:  
**Why this matters now**:  
**What is deliberately out of scope**:  
**Prototype type**:  
**Minimum fidelity needed**:  
**Success signal**:  
**Failure signal**:  
**Possible branches after test**:  

This keeps prototypes from becoming vague experiments with no decision consequence.

## Response structure

Use this structure unless the user asks for something else:

### Concept Framing
- ...

### Uncertainty Map
- Known knowns: ...
- Known unknowns: ...
- Unknown knowns: ...
- Unknown unknowns suspects: ...

### What Needs to Be Prototyped
1. ...
2. ...
3. ...

### Prototype Plan
- Prototype A: ...
- Prototype B: ...
- Prototype C: ...

### Stop Criteria
- ...

### Recommendation
- ...

## Fast mode

Use this quick pass when speed matters:
- What part of this idea is actually unclear?
- What might we be wrong about?
- What is the cheapest prototype that would expose that?
- What would we learn that changes the decision?
- What would tell us to stop prototyping and move on?

## Usage notes

This skill is especially useful for:
- new feature concepts with unclear player value
- UI layers that aggregate multiple demands or systems
- event structures that may shift player behavior in unexpected ways
- economy and production features where readability and pressure interact
- hybrid features that may become a different feature category once tested
- retention features where real value may emerge from cadence rather than content

When useful, combine this skill with a more explicit decision framework such as GROW:
- **Goal** defines the intended outcome
- **Reality** identifies current constraints
- **Unknown-unknowns prototyping** identifies what still must be discovered
- **Options / Will** can then be grounded in actual learning instead of speculation

## Working principle

**Prototyping is not the path to a product. It is the path to understanding what you are actually making.**

Do not ask only, "How do we build this?"
Ask first, "What do we not yet understand well enough to build responsibly?"