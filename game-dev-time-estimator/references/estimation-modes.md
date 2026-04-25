# Estimation Modes

Use this file when the user input is incomplete, when you need scenario framing, or when a deadline plausibility check is more useful than a generic estimate.

## 1. Team-known mode

Use when the user described the team with at least rough role and availability detail.

Focus on:
- what can happen in parallel
- which workstreams bottleneck through one person
- where missing coverage creates waiting time
- how experience level changes speed

Good output pattern:
- current team summary
- likely parallel work
- likely bottlenecks
- low / expected / high schedule range
- what would shorten the schedule

## 2. Team-unknown mode

Use when team information is missing.

Offer labeled scenarios such as:
- solo part-time beginner
- solo full-time experienced developer
- tiny indie team with mixed skills
- small professional team with solid coverage

Keep scenario names plain and clearly hypothetical.
Do not imply the user actually has that team.

## 3. Target-date mode

Use when the user asks something like:
- can we do this in 6 months?
- could this ship by next summer?
- is this realistic by Q4?

Approach:
1. estimate a realistic range first
2. compare the requested deadline against that range
3. label the deadline as plausible, aggressive, or unrealistic
4. explain what must change to make it plausible

Prefer language like:
- plausible if scope stays tight
- possible but aggressive
- unrealistic without major cuts
- fantasy unless the milestone is redefined

## 4. Milestone mode

Shift the estimate based on what the user is actually trying to reach.

### Prototype
- optimize for learning speed
- assume placeholder assets
- include iteration and failed experiments

### Vertical slice
- assume one polished representative slice
- raise the bar for UX, art consistency, and polish
- include more integration and presentation work

### Release
- include content breadth, QA, stability, business readiness, and endgame finishing work

### Live F2P / online
- include backend, telemetry, balancing cadence, support needs, and operational readiness

## 5. Confidence language

Use confidence language instead of pretending the estimate is exact.

Examples:
- high uncertainty because team details are missing
- moderate confidence if the team has shipped similar work
- low confidence because content scope is still undefined
- confidence would improve a lot after a prototype or feature list cut
