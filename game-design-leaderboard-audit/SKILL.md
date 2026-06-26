---
name: game-design-leaderboard-audit
description: Audit an existing leaderboard or competitive ranking system in a game for stagnation risk, scale problems, goal density, motivation quality, reward bracket design, group composition fairness, and top-of-ladder sustainability. Use when evaluating a leaderboard that feels flat, unfair, or disengaging; when reviewing a competitive feature before launch; or when diagnosing why a leaderboard isn't driving expected engagement or retention.
---

# Game Design Leaderboard Audit

Audit a leaderboard or competitive ranking system as a metagame feature — not just as a list, but as a system that generates goals, competition, and emotional investment for the majority of players.

Use this skill to evaluate whether a leaderboard is actually doing its job. A leaderboard that only matters to the top 10 players has failed. The audit focuses on seven dimensions: stagnation, scale, goal density, motivation, reward brackets, group composition, and the top-of-ladder problem.

## Core principle

A leaderboard is the start of a metagame. Its quality is not measured by whether it ranks players — it is measured by whether it generates meaningful, emotionally resonant competition for the majority of the player base, from the player at the very top to the player sitting in the middle of a group of 100.

## What to produce

Generate:
1. **Audit target** — what is being reviewed and what context it sits in
2. **Stagnation audit** — whether the leaderboard feels alive or frozen
3. **Scale audit** — whether the numbers are human-meaningful
4. **Goal density audit** — how many distinct goals the structure generates
5. **Motivation audit** — the quality and balance of intrinsic vs. extrinsic motivation
6. **Reward bracket audit** — coverage, fairness, and value calibration
7. **Group composition audit** — fairness and competitive integrity
8. **Top-of-ladder audit** — what happens when a player reaches the ceiling
9. **Failure patterns** — named anti-patterns present in the design
10. **Recommendations** — prioritized, specific, actionable

## Process

### 1. Define the audit target

Clarify:
- What game, feature, or competitive system is being audited
- What the score or ranking metric is
- Whether this is a global list, a group-based system, or a league ladder
- What the competition round length is (if any)
- What rewards or consequences are attached to standings
- What stage the design is at: concept, in production, live

If details are incomplete, note what is assumed and flag it.

### 2. Stagnation audit

The most damaging leaderboard failure is invisibility — a board nobody checks because nothing ever moves.

Ask:
- What is the score, and how frequently does it change?
- Can the score change meaningfully during a single play session?
- Does the score reset at any point, or is it purely cumulative?
- Could a player who starts today ever catch a veteran at the same skill level?
- How long would it take to move one position at the median rank?

Look for:
- Lifetime-accumulated scores with no reset (permanent head-start advantage)
- Scores that change only once per day or slower
- Score granularity too coarse to show movement (e.g., everyone stuck at round numbers)
- No mechanism for new players to enter competitive positions

Label the finding:
- **Healthy** — score changes multiple times per session; leaderboard visibly shifts
- **Borderline** — score changes daily; some movement is visible over a week
- **Stagnant** — score changes slowly or reflects lifetime play; board rarely shifts
- **Dead** — lifetime score, no reset, veterans permanently untouchable

### 3. Scale audit

Ask:
- How many players are ranked in a single visible leaderboard?
- What position would a median-skill new player typically occupy?
- Are the position numbers emotionally meaningful? (Position 156,342 is not.)
- Does the leaderboard show the player's own position relative to others nearby?
- Is the competition scope global, regional, or grouped?

Look for:
- Global leaderboards with tens of thousands of entries
- Position numbers too large to parse emotionally
- No visible neighborhood (the players just above and below the viewer)
- Leaderboard that only highlights top 10 while ignoring everyone else

Evaluate: does the player feel like they are in a real, contestable race — or watching a scoreboard from a distance?

### 4. Goal density audit

A well-designed leaderboard generates multiple simultaneous goals at different time scales. Evaluate whether this structure provides all three tiers:

**Immediate goal** — overtake the player directly above me (next session)
**Short-term goal** — climb several places or reach the next reward bracket (this week)
**Medium-term goal** — earn promotion to the next league (this round)
**Long-term aspirational goal** — reach the top of the ladder (months)

Ask:
- Does the structure create all four goal tiers naturally?
- Is the immediate goal always visible and achievable for a player of average commitment?
- Is the long-term goal aspirational without feeling impossible?
- Does the reward bracket design create additional intermediate goals between the goal tiers?
- Are demotion stakes generating meaningful tension at the bottom of the leaderboard?

Use this format:

| Goal tier | Present | Strength | Main gap |
|---|---|---|---|
| Immediate (overtake neighbor) | Yes / No | ... | ... |
| Short-term (climb / reach bracket) | Yes / No | ... | ... |
| Medium-term (promotion) | Yes / No | ... | ... |
| Long-term aspirational (top of ladder) | Yes / No | ... | ... |

### 5. Motivation audit

Ask:
- What intrinsic motivation does the structure create? (pride, prestige, mastery, social competition)
- What extrinsic motivation does the structure create? (rewards, currencies, exclusive content)
- Is either type absent or over-dominant?
- Does the design feel like genuine competition, or does it feel like a chore with prizes?
- Could a player who receives no rewards still find the leaderboard engaging?
- Does the reward structure create pressure and anxiety, or anticipation and excitement?

Evaluate balance:
- **Intrinsic only** — sustainable for hardcore players, will fail to retain casual players
- **Extrinsic only** — drives short-term behavior, creates burnout and pay-to-win perception
- **Balanced** — leaderboard climbing feels worth doing for its own sake; rewards amplify rather than justify

### 6. Reward bracket audit

Ask:
- Are reward brackets defined? How many brackets exist?
- What percentage of players receive a meaningful reward?
- Is the consolation bracket wide enough to reward participation without trivializing achievement?
- Is the top bracket sufficiently rare and prestigious?
- Are mid-tier brackets spaced to create meaningful distinctions between them?
- What happens to players who finish outside all brackets — do they feel their effort was wasted?
- Are rewards appropriate to the effort required to reach each bracket?

Evaluate coverage:
- **Too narrow** — only top 3-5 players rewarded; the system ignores 95% of participants
- **Too wide** — everyone gets a reward; prestige collapses
- **Healthy** — meaningful rewards for top ~20-30%; consolation tier for ~30-50%; nothing for bottom ~20-30%

### 7. Group composition audit

Ask:
- How are players assigned to groups?
- Are new players mixed with long-term veterans?
- Are high spenders mixed with free players in the same group?
- Is there any skill or activity matching, or is grouping random?
- What happens if a highly active player is permanently dominant in their group?
- Are there mechanisms to refresh or rebalance groups?

Look for:
- **Whale-dominated groups** — one spender makes everyone else irrelevant; destroys motivation for the whole group
- **Sandbagging risk** — players deliberately losing to stay in a weaker league; reward structure incentivizes this
- **Static groups** — same players compete forever; competition becomes predictable and stale
- **No catch-up** — players with early-round leads become untouchable by mid-round; others disengage

### 8. Top-of-ladder audit

Ask:
- What happens to a player who reaches the top position in the top league?
- Does the game have an answer for elder players with nowhere left to climb?
- Is the top league expanding over time, or is it a fixed ceiling?
- Are naming conventions for league tiers scalable, or will they become absurd?
- What sustains engagement for the most competitive players after they have "won"?

Common failure shapes:
- **The empty summit** — player reaches the top, loses all leaderboard motivation
- **Name exhaustion** — Gold → Platinum → Diamond → Obsidian → what next?
- **Inflation** — the top league grows until prestige disappears
- **Reset shock** — periodic resets exist but were introduced after launch; veteran backlash

### 9. Diagnose failure patterns

Name and describe each present anti-pattern:

- **Stagnant board** — score moves too slowly; nobody checks the leaderboard
- **Scale blindness** — position numbers are too large to feel meaningful
- **Goal poverty** — the structure generates only one or two goals instead of a ladder of them
- **Reward desert** — most players finish a round with nothing; effort feels wasted
- **Reward flood** — everyone gets something; prestige disappears
- **Whale capture** — one dominant player destroys the competitive dynamic for the whole group
- **Global vanity board** — a list that is technically a leaderboard but creates no real competition
- **Empty summit** — no design answer for players who have reached the top
- **Chore motivation** — rewards justify participation; without them, no one would care
- **Sandbagging loop** — reward structure makes intentional losing rational

### 10. Convert findings into recommendations

For each significant issue:
- **Issue** — what is wrong
- **Why it hurts** — specific player experience or metric impact
- **Fix direction** — what structural change addresses it
- **Priority** — Critical / Important / Polish

## Response structure

### Audit Target
- ...

### Stagnation
- Verdict: Healthy / Borderline / Stagnant / Dead
- Findings: ...

### Scale
- ...

### Goal Density
- Table: ...
- Gaps: ...

### Motivation
- Intrinsic: ...
- Extrinsic: ...
- Balance verdict: ...

### Reward Brackets
- Coverage: Too narrow / Healthy / Too wide
- Issues: ...

### Group Composition
- ...

### Top-of-Ladder
- ...

### Failure Patterns
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode

If the user provides a quick description and wants a rapid read:
- Is the score fast-changing or lifetime-accumulated?
- Is this global or grouped? If global, how many players?
- Does it reward anyone below position 10?
- What happens to a player in the middle of the board — do they have something to play for?
- What happens to the player at the very top?

## Working principle

A leaderboard that only matters to the top ten players is a monument, not a feature. The audit's job is to find how many players the design is failing — and why.
