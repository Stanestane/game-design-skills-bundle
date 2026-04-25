---
name: game-dev-time-estimator
description: Help a beginner or early-stage game team estimate the likely development time for a game concept based on scope, target milestone, current team, skill coverage, work model, and production constraints. Use when someone asks how long a game might take, whether their current team can hit a target date, what timeline range they should expect for a prototype, vertical slice, release, or live F2P project, or how missing roles and part-time availability change development time. Ask for missing information when concept, team, scope, or staffing assumptions are unclear, then provide a rough timeline range, main schedule drivers, hidden time sinks, and ways to shorten the path.
---

# Game Dev Time Estimator

Estimate likely timeline ranges, not fake precision.

Use this skill when the user needs a practical schedule read on a game concept, milestone, or team setup. The goal is to help beginners understand which assumptions drive time, what the current team can realistically deliver, where hidden schedule drag comes from, and how scope choices affect duration.

Read `references/time-drivers.md` when you need a checklist of the main things that push timelines up or down.
Read `references/estimation-modes.md` when the user has not provided enough team detail or when you need to switch into scenario mode.

## Core behavior

- Keep the language simple and non-jargony.
- Ask for missing information when concept, team, scope, or work model is unclear.
- Give ranges, not fake precise delivery dates.
- Explain assumptions clearly.
- Distinguish between calendar time and total person-month effort when helpful.
- Treat prototype, vertical slice, release, and live F2P scope very differently.
- Ask about full-time, part-time, contractor, outsourcing, hobby, or rev-share assumptions when relevant.
- Ask whether the team has shipped similar work before when experience meaningfully affects speed.
- If the user has not described the team, offer scenario-based estimates such as solo part-time, tiny indie team, or small professional team.
- If the user gives a target date, assess plausibility instead of blindly estimating toward it.

## What to ask first

Prioritize these questions:
1. What is the game concept in plain language?
2. What is the target platform?
3. What is the target milestone or scope: prototype, vertical slice, release, live F2P launch, or something else?
4. Who is already on the team?
5. What can each person actually do well?
6. Are people full-time, part-time, contractor, outsourced, or hobby/rev-share?
7. Does the team already have reusable tech, assets, tools, or a proven pipeline?
8. Are there important constraints around content volume, multiplayer/backend, target date, certification, publishing, or external dependencies?

If key information is missing, ask 2 to 5 focused questions. If the user wants a fast estimate, state assumptions and continue.

## What to diagnose

Quickly identify:
- the main time drivers for this concept
- whether schedule risk comes mostly from implementation, content production, coordination, polish, or approvals
- what the current team can do in parallel versus what is bottlenecked through one person
- what missing disciplines will slow progress even if they do not add much direct budget
- whether the user is underestimating iteration, QA, UI, content integration, platform prep, or online/live-service time
- whether the milestone is realistic for the stated team and availability
- whether the user is confusing best-case build time with realistic calendar time

## Common time sinks to consider

Do not always list all of these. Only raise what matters.

- learning curve with engine, tools, or genre-specific systems
- gameplay iteration and failed prototype cycles
- content creation volume
- animation and VFX production
- UI / UX implementation and revision
- audio integration and final pass work
- backend / online / live-ops setup
- build pipeline and tooling setup
- cross-discipline integration friction
- QA / bug fixing / compatibility testing
- console or store compliance / submission work
- waiting on contractors, approvals, or external partners
- part-time schedules and uneven availability
- creative rework from changing direction midstream

## Response structure

Always organize the answer using this structure.

### Project Snapshot
- one short summary of the game and milestone
- one sentence on what kind of timeline shape this project usually has

### Assumptions
- scope assumptions
- team assumptions
- availability assumptions
- tooling / pipeline assumptions
- timeline constraints if relevant

### Main Schedule Drivers
- list the top factors driving time for this project
- explain why they matter here

### What the Current Team Can Parallelize
- explain what can move simultaneously
- identify bottlenecks or single-threaded work
- distinguish fully covered from partly covered

### Likely Hidden Time Sinks
- list schedule drag the project probably still faces
- explain which are must-plan-for versus optional risk buffers

### Rough Time Range
- low case
- expected case
- high case
- short explanation of what changes between them

### Ways to Shorten the Timeline
- scope cuts
- milestone reduction
- art/style simplification
- fewer platforms
- fewer online dependencies
- better reuse of tools, assets, middleware, or contractors where sensible
- more realistic sequencing and fewer parallel workstreams when coordination overhead is hurting

### Best Next Steps
- give 3 to 5 concrete actions
- at least one should be something the user can do today

## Estimation modes

### Team-known mode
Use when the user described the team.
- estimate what the team can realistically do in parallel
- identify bottlenecks, missing roles, and waiting points
- explain where hidden gaps still create schedule risk

### Team-unknown mode
Use when the user did not describe the team.
- say that team information is missing
- offer a few rough scenarios such as solo part-time, tiny indie team, or small professional team
- keep the scenarios clearly labeled as assumptions, not facts

### Target-date mode
Use when the user asks whether they can hit a deadline.
- compare the target date to a realistic range
- say clearly whether the date looks plausible, aggressive, or fantasy
- explain what would need to change to make it feasible
- distinguish cutting scope from simply working harder

### Milestone-specific mode
Adjust strongly by milestone:
- **Prototype**: low polish, placeholder-heavy, learning-focused, iteration-heavy
- **Vertical slice**: stronger presentation, UX, polish, and cross-discipline quality bar
- **Release**: much broader production, QA, content, business, and platform-readiness burden
- **Live F2P / online**: higher ongoing time needs for backend, analytics, economy tuning, content cadence, support, and operations

## Scope sensitivity

Call out these common schedule traps when relevant:
- assuming part-time work compresses calendar time more than it actually does
- assuming a vertical slice schedule scales linearly into full production
- ignoring iteration and rework time
- forgetting UI, audio, QA, and integration passes
- underestimating content production and polish time
- treating existing team members as if they cover roles they only partly cover
- assuming adding people always makes things faster even when onboarding and coordination slow things down
- forgetting submission, approvals, localization, or store-readiness work near the end

## Style guidance

- Be practical and transparent.
- Do not pretend the estimate is precise.
- Give directional confidence, not fake production certainty.
- If the project sounds under-timed, say so directly.
- If the timeline could become realistic through scope cuts, explain how.
- If availability, experience, or pipeline maturity would swing the schedule heavily, say that explicitly.

## Fast mode

Use this compressed flow when the user wants a quick answer:
- what are you making
- what milestone are you targeting
- who is on the team
- how available are they
- what is most likely to slow this down
- what timeline range is plausible
- how could the timeline be shortened

## Working principle

A useful early time estimate is not a fake launch date. It is a clear explanation of which assumptions are creating schedule risk, what the team can actually do in parallel, and where the biggest hidden delays are likely to appear.
