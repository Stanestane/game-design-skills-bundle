---
name: game-design-grow-design
description: Evaluate game features, feature pitches, live-ops ideas, UX changes, economy changes, roadmap choices, retention initiatives, monetization initiatives, and ambiguous design problems using the GROW model: Goal, Reality, Options, Will. Use when a team needs structure, clearer decision-making, better option generation, explicit tradeoff analysis, or a concrete recommendation and next-step plan instead of circular discussion.
---

# Game Design GROW Design

Use the GROW model to turn vague game design conversations into a structured decision flow:

**Goal -> Reality -> Options -> Will**

Use this skill when a team has ideas, concerns, and opinions, but not enough shared structure to reach a decision. Keep the framework practical, explicit, and usable by teams that need help clarifying what they want, what is true right now, what they could do, and what they should commit to next.

## What to produce

Generate a structured decision pass with these outputs:

1. **Goal** - a concise statement of the intended outcome and success criteria
2. **Reality** - the current state, constraints, dependencies, and unknowns
3. **Options** - multiple credible paths, not just one preferred answer
4. **Will** - a recommendation, immediate next steps, and validation needs

## Process

### 1. Goal

Clarify what the team is trying to achieve.

Ask:
- What player problem does this solve?
- What player behavior should change?
- What business or product goal does this support?
- How should this fit existing game loops and systems?
- What does success look like in player terms?
- What does success look like in KPI terms?
- What are the quality constraints?
- What is the release window or decision horizon?

Use a SMART-style structure:
- **Specific** - clearly describe the feature intent
- **Measurable** - define KPIs or evaluation signals
- **Attainable** - keep the goal feasible within team and technical limits
- **Relevant** - connect the idea to game strategy and product priorities
- **Time-boxed** - align it to a release, milestone, or decision window

Write:
- **Goal statement**
- **Success criteria**
- **Key constraints**

Suggested format:

**Goal statement**  
We want to [player/business outcome] by introducing or changing [feature/system], measured by [metrics/signals], within [timeframe].

### 2. Reality

Describe what is true right now.

Build a grounded picture of the current situation.

Ask:
- What is the current player experience?
- What already exists that overlaps with this idea?
- Which systems would this touch?
- What infrastructure, tools, or content pipelines already exist?
- What are the open design questions?
- What resourcing constraints exist?
- What tech, UX, or economy limitations exist?
- What assumptions are currently unverified?
- Which comparable features already exist in this game or similar games?
- What data or prior learnings matter?

Useful categories:
- **Game state** - existing systems, loops, progression context
- **Player state** - motivations, friction, expectations
- **Business state** - targets, roadmap role, cannibalization risk
- **Production state** - scope, dependencies, tech constraints
- **Evidence state** - telemetry, benchmarks, prior experiments, team learnings

Write:
- **Current state**
- **Constraints**
- **Unknowns**
- **Dependencies**

Suggested format:

**Reality summary**  
Current state: ...  
Constraints: ...  
Unknowns: ...  
Dependencies: ...

### 3. Options

Generate multiple credible solution paths before recommending anything.

General rule: always produce several options, even when one path seems obvious.

#### Option-generation methods

Choose one or combine several:

**A. Five-options approach**
Use when several candidate solutions already exist.
- list at least 3-5 approaches
- define pros and cons for each
- compare expected impact and implementation cost
- identify the fastest testable version

**B. Obstacle approach**
Use when the team is blocked by one obvious problem.
- name the roadblock clearly
- imagine it removed
- describe the resulting design space
- derive workaround paths

**C. Ideal-outcome approach**
Use when direction is unclear but the end state is clear.
- describe the ideal player experience
- work backwards from that state
- identify enabling components and milestones

**D. Transformative approach**
Use when building on existing systems is likely better than inventing from scratch.
- identify reusable systems, UI, content pipelines, currencies, or loops
- ask what can be tuned, recombined, or extended
- prefer leverage over novelty where appropriate

**E. Thinking outside the box**
Use when the problem is understood but no satisfying approach exists.
- brainstorm without commitment
- deliberately include non-obvious approaches
- separate idea generation from evaluation

#### Evaluate each option

For each option, score:
- **Player value** (1-5)
- **Business value** (1-5)
- **Implementation cost** (1-5)
- **Risk / uncertainty** (1-5)
- **Strategic fit** (1-5)

Capture the main tradeoffs, not just the scores.

Suggested format:

| Option | Summary | Player Value | Business Value | Cost | Risk | Notes |
|---|---|---:|---:|---:|---:|---|
| A | ... | ... | ... | ... | ... | ... |
| B | ... | ... | ... | ... | ... | ... |

### 4. Will

Decide what should happen now.

Turn the discussion into a concrete action plan.

Ask:
- Which option is recommended and why?
- What is the smallest meaningful version?
- What should happen now versus later?
- What needs validation before full commitment?
- What is the roadmap position?
- What workstreams are required?
- What are the next decisions, owners, or documents needed?

Possible outputs:
- recommendation
- MVP or prototype scope
- backlog framing
- roadmap sequencing
- task breakdown
- test plan
- KPI follow-up plan

Write:
- **Recommendation**
- **Why this option**
- **Immediate next steps**
- **Validation needed**
- **Risks to monitor**

## Response structure

Use this structure unless the user asks for something else:

### Goal
- ...

### Reality
- ...

### Options
1. ...
2. ...
3. ...

### Will
- Recommended path: ...
- Near-term actions: ...
- Risks / assumptions: ...

## Fast mode

Use this condensed version for rapid feature triage:
- **Goal**: What outcome are we after?
- **Reality**: What constraints and dependencies matter?
- **Options**: What are 3 plausible solution paths?
- **Will**: Which one should we do now, and what is the first concrete step?

## Usage notes

This skill is especially useful for:
- new features
- feature revisions
- UX or economy changes
- roadmap choices
- retention initiatives
- monetization initiatives
- live-ops content or event structures
- ambiguous design problems that risk circular discussion

It is particularly suitable for teams that need extra structure, explicit tradeoff framing, and help converting a loose discussion into a decision path.

When relevant, combine this framework with:
- source-material lookup from update docs
- implementation reality from config files
- KPI or economy analysis from spreadsheets
- player-facing experience summaries

## Working principle

Use this framework to prevent two common failure modes:
1. jumping from vague ambition to implementation detail too early
2. cycling between ideas without committing to a decision path

The intent is not bureaucracy for its own sake. The intent is structured design judgment that helps uncertain teams move forward.