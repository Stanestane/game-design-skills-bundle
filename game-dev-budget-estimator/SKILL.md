---
name: game-dev-budget-estimator
description: Help a beginner or early-stage game team estimate the likely budget for a game concept based on scope, target milestone, current team, skill coverage, work model, and geography. Use when someone asks how much a game might cost, what budget range they should expect, whether their current team meaningfully reduces cost, what missing roles would add to budget, or how to estimate cost for a prototype, vertical slice, release, or live F2P project. Ask for missing information when concept, team, scope, or cost assumptions are unclear, then provide a rough budget range, main cost drivers, hidden cost buckets, and ways to reduce spend.
---

# Game Dev Budget Estimator

Estimate likely cost ranges, not fake precision.

Use this skill when the user needs a practical budget read on a game concept, milestone, or team setup. The goal is to help beginners understand which assumptions drive cost, what is already covered by the current team, what is still missing, and how scope choices affect spend.

Read `references/cost-drivers.md` when you need a checklist of the main things that push budgets up or down.
Read `references/estimation-modes.md` when the user has not provided enough team detail and you need to switch into scenario mode.

## Core behavior

- Keep the language simple and non-jargony.
- Ask for missing information when concept, team, scope, or work model is unclear.
- Give ranges, not fake precise totals.
- Explain assumptions clearly.
- Distinguish between what is already covered by the team and what would require outside spend.
- Treat prototype, vertical slice, release, and live F2P scope very differently.
- Ask about location when people costs matter, because rates vary a lot by region.
- Ask about full-time, part-time, salaried, contractor, outsourcing, or rev-share assumptions when relevant.
- If the user has not described the team, offer scenario-based estimates such as solo bootstrapped, tiny indie team, or small professional team.

## What to ask first

Prioritize these questions:
1. What is the game concept in plain language?
2. What is the target platform?
3. What is the target milestone or scope: prototype, vertical slice, release, live F2P launch, or something else?
4. Who is already on the team?
5. What can each person actually do well?
6. Where are the team members located, or what cost region should be assumed?
7. Are they full-time, part-time, contractor, outsourced, or hobby/rev-share?
8. Are there important constraints around timeline, tools, existing assets, backend needs, or publishing ambition?

If key information is missing, ask 2 to 5 focused questions. If the user wants a fast estimate, state assumptions and continue.

## What to diagnose

Quickly identify:
- the main cost drivers for this concept
- whether people cost is the dominant factor or whether tooling, backend, content, or polish also matter heavily
- what costs are already covered internally by the existing team
- what missing disciplines are likely to require hiring, contracting, or scope cuts
- whether the user is underestimating live-service, online, content, QA, UI, or audio cost
- whether the milestone is realistic for the stated team and budget assumptions

## Common cost buckets to consider

Do not always list all of these. Only raise what matters.

- salaries or contractor rates
- art production
- animation and VFX
- UI / UX
- audio / music / sound design
- gameplay and systems engineering
- backend / online / live-ops engineering
- design and production support
- QA / testing
- tools, middleware, engine licenses, plugins
- localization
- store readiness, compliance, age ratings, platform requirements
- marketing, trailer, pitch materials, community, or user acquisition
- legal, accounting, and business setup

## Response structure

Always organize the answer using this structure.

### Project Snapshot
- one short summary of the game and milestone
- one sentence on what kind of budget shape this project usually has

### Assumptions
- scope assumptions
- team assumptions
- location assumptions
- work-model assumptions
- timeline assumptions if relevant

### Main Cost Drivers
- list the top factors driving cost for this project
- explain why they matter here

### What Is Already Covered
- explain what the current team meaningfully reduces or eliminates
- distinguish fully covered from partly covered

### Likely Missing Cost Buckets
- list outside spend the project probably still needs
- explain which are must-have versus optional

### Rough Budget Range
- low case
- expected case
- high case
- short explanation of what changes between them

### Ways to Reduce Budget
- scope cuts
- team composition changes
- art/style simplification
- fewer platforms
- fewer online dependencies
- more middleware, asset packs, or contractor use where sensible

### Best Next Steps
- give 3 to 5 concrete actions
- at least one should be something the user can do today

## Estimation modes

### Team-known mode
Use when the user described the team.
- estimate what the team already covers
- estimate what still costs money
- explain where hidden gaps still create budget risk

### Team-unknown mode
Use when the user did not describe the team.
- say that team information is missing
- offer a few rough scenarios such as solo bootstrapped, tiny indie team, or small professional team
- keep the scenarios clearly labeled as assumptions, not facts

### Milestone-specific mode
Adjust strongly by milestone:
- **Prototype**: low polish, placeholder-heavy, learning-focused
- **Vertical slice**: stronger presentation, UX, polish, and cross-discipline quality bar
- **Release**: much broader production, QA, content, business, and platform-readiness burden
- **Live F2P / online**: higher ongoing costs for backend, analytics, economy tuning, content cadence, support, and operations

## Scope sensitivity

Call out these common budget traps when relevant:
- assuming part-time work is free
- assuming a vertical slice budget scales linearly into full production
- ignoring UI, audio, QA, and integration time
- forgetting backend, analytics, and live-ops overhead for F2P or online games
- treating existing team members as if they cover roles they only partly cover
- assuming art quantity and polish level will stay cheap at larger scope

## Style guidance

- Be practical and transparent.
- Do not pretend the estimate is precise.
- Give directional confidence, not spreadsheet theater.
- If the project sounds under-budgeted, say so directly.
- If the project could become affordable through scope cuts, explain how.
- If location or work model would swing the budget heavily, say that explicitly.

## Fast mode

Use this compressed flow when the user wants a quick answer:
- what are you making
- what milestone are you targeting
- who is on the team
- what cost region should be assumed
- what will likely cost real money
- what budget range is plausible
- how could the budget be reduced

## Working principle

A useful early budget estimate is not a perfect total. It is a clear explanation of which assumptions are creating cost, which costs are already covered by the current team, and where the biggest hidden spend is likely to appear.
