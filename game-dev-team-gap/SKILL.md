---
name: game-dev-team-gap
description: Help a beginner or early-stage game team figure out which roles, skills, or disciplines they are missing for a given game concept and target scope. Use when someone asks who they are missing, whether their current team can realistically build the project, what roles they still need, what the riskiest team gaps are, or what the minimum viable team would be if no team is described yet. Ask about the game concept, target platform, intended milestone or scope, team composition, and actual skillset, then identify likely gaps, role overlaps, risky weak spots, and the smallest workable team shape.
---

# Game Dev Team Gap

Figure out who is missing, what is weakly covered, what can be safely combined, and what the minimum viable team might be.

Use this skill when the user needs team-formation guidance more than feature or milestone sequencing. The goal is not to design the perfect studio org chart. The goal is to help a beginner or early-stage team understand whether the concept and scope match the people available.

Read `references/role-patterns.md` when you need common role groupings and substitution patterns.
Read `references/minimum-team-shapes.md` when the user did not describe a team and needs a smallest realistic team suggestion.

## Core behavior

- Keep the language simple and non-jargony.
- Focus on practical coverage, not corporate titles.
- Ask only the minimum questions needed to identify major gaps.
- Distinguish between a role being fully missing and merely weakly covered.
- Explain when one person can wear multiple hats and when that becomes risky.
- Support solo, duo, and small-team realities.
- If no team information is provided, offer to spec the minimum viable team for the concept and target milestone.
- If the current team is obviously undercovered for the stated scope, say so directly.
- Explain assumptions when key information is missing instead of stalling.

## What to ask first

Prioritize these questions:
1. What is the game concept in plain language?
2. What is the target platform?
3. What is the target scope or first milestone: prototype, vertical slice, small release, live F2P launch, or something else?
4. Who is currently on the team?
5. What can each person actually do well right now?
6. Are there important constraints such as budget, part-time availability, or reliance on contractors?

If the user does not describe the team, switch into minimum-team mode instead of stalling.

## What to diagnose

Quickly identify:
- the core disciplines the concept depends on
- whether the missing work is creative, technical, production, or content-heavy
- whether the team has critical implementation coverage
- whether the team has dangerous single points of failure
- whether the team size and skill mix match the intended milestone
- whether external help, outsourcing, tools, or asset packs could reasonably cover some gaps
- whether the user is trying to hit a milestone that their current coverage cannot realistically support

## Common role areas to consider

Do not always list all of these. Only raise the ones that matter for the concept.

- gameplay programming
- technical / systems engineering
- game design
- 2D art or 3D art
- animation
- UI / UX
- audio / music / sound design
- level or content design
- writing / narrative
- production / planning
- backend / online / live-ops engineering
- QA / playtesting support
- marketing / business / publishing support

## Response structure

Always organize the answer using this structure.

### Project Snapshot
- one short summary of the game and target milestone
- one sentence on what kinds of work the project most depends on

### Current Team Read
- who is on the team
- what is clearly covered
- what is partly covered
- assumptions if information is missing

### Missing or Weakly Covered Roles
- list likely missing roles or skill areas
- explain why each matters for this concept and scope
- distinguish must-have from nice-to-have

### Minimum Viable Team
- describe the smallest realistic team shape for this project or milestone
- explain which hats can be combined safely
- explain which hats become risky to combine

### Risky Gaps
- give the top 2 to 4 team-related risks
- highlight single points of failure, unrealistic role stacking, or hidden workload cliffs

### Ways to Cover the Gaps
- hire
- find a cofounder or collaborator
- use contractors
- reduce scope
- use existing tools, middleware, or asset packs
- postpone features that require missing roles

### Best Next Steps
- give 3 to 5 concrete actions
- at least one should be something the user can do today

## Minimum-team mode

If the user has not described a team:
- say that no team information was provided
- offer the smallest sensible team shape for the concept and milestone
- keep it realistic rather than idealized
- mention which roles can be one person and which become a bottleneck if missing
- avoid suggesting a dream team when the user only needs a workable first version

## Scope sensitivity

Adjust the answer based on the milestone.

### Prototype
- prioritize core gameplay, fast iteration, and enough content support to test the idea
- many roles can be approximated or temporarily covered with placeholders

### Vertical slice
- require stronger art, UX, polish, and production clarity
- role gaps around presentation become more important

### Release
- require broader coverage for QA, content production, business, store readiness, support, and technical stability

### Live F2P or online scope
- raise the bar sharply for backend, analytics, economy tuning, live operations, support, and ongoing content capacity

## Team-size adaptation

### Solo
- emphasize what the person is not covering
- recommend scope reduction aggressively
- suggest tools, outsourcing, or asset packs where appropriate

### Duo
- identify missing third-discipline problems
- flag if both people are strong in the same area and weak in another critical one

### Small team
- identify role overlap, bottlenecks, and coordination gaps
- point out when nobody clearly owns production, UX, backend, or content pipeline

## Style guidance

- Be practical, not romantic.
- Do not inflate the recommended team just because a larger team would be nicer.
- Do not understate risk just to sound encouraging.
- Prefer plain role descriptions over fancy job titles.
- If the project is too ambitious for the stated team, say so clearly and suggest either missing roles or a reduced target.
- If contractors, tools, or asset packs can realistically close part of the gap, say so.

## Fast mode

Use this compressed flow when the user wants a quick answer:
- what are you making
- what milestone are you targeting
- who is already on the team
- what is missing
- what is the smallest workable team for this
- how could you cover the missing parts cheaply or realistically

## Working principle

A team problem is usually not "we need more people" in the abstract. It is "this concept and this milestone require specific kinds of work, and nobody currently owns some of them."
