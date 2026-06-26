---
name: game-design-leaderboard-builder
description: Design a complete leaderboard system from scratch for a game, feature, or competitive mode. Covers group structure, league ladder, round cadence, reward brackets, score design, group composition, and top-of-ladder sustainability. Use when starting a new competitive feature, when a basic leaderboard needs a full redesign, or when a team needs a concrete leaderboard specification to build from. Always asks intake questions before designing — and offers sensible defaults if the designer doesn't have answers yet.
---

# Game Design Leaderboard Builder

Design a complete leaderboard system grounded in the game's context, player base, economy, and production constraints.

This skill asks eight intake questions before producing anything. Each question has a suggested default — accept it if you don't know the answer yet, or override it with specifics. The more precise the inputs, the more precisely calibrated the design.

## Core principle

A leaderboard is not a feature you bolt on — it is a metagame you design. Its structure determines how many goals players have, how long they stay engaged, and whether the competition feels fair and meaningful or frustrating and pointless. Get the inputs right before designing anything.

---

## Phase 1: Intake — ask these questions before proceeding

Present all eight questions. For each, offer the default assumption if the user does not provide an answer. Accept partial answers — use defaults for whatever is missing and flag those assumptions clearly in the output.

---

### Q1 — What is the score, and how fast does it change?

What metric are players competing on? How quickly can it change — can it shift meaningfully in a single play session, or does it accumulate slowly over days or weeks?

**Why this matters:** A slow-changing or lifetime-accumulated score produces a stagnant leaderboard regardless of how well the rest of the structure is designed. This is the most critical input.

**Default assumption if unknown:**
> Session-based score that can change meaningfully in a single play session. Score resets at the start of each competition round. Assumed moderate velocity — a committed player can move 10-20 positions per active session.

---

### Q2 — How large is your active player pool?

How many players will be actively competing in a single competition window? (Active = played at least once during the round.)

**Why this matters:** Pool size determines whether you need group segmentation, how many tiers the league ladder needs, and the pyramid shape of the whole structure.

**Default assumption if unknown:**
> 10,000 active competing players — a mid-size feature launch or a moderately successful mobile F2P title at a stable point in its lifecycle.

---

### Q3 — What is the desired competition round length?

How long does one competition round last before scores reset and standings are settled?

**Why this matters:** Round length affects urgency, the scoring velocity requirement, the reset-acceptance by players, and how often reward brackets pay out.

**Default assumption if unknown:**
> 7 days (weekly). The most tested and widely accepted cadence for mobile/F2P. Long enough to feel like a meaningful campaign; short enough to feel urgent.

---

### Q4 — What is the game context?

Genre, platform, and typical session length. What kind of game is this leaderboard sitting inside?

**Why this matters:** Session length affects what group size feels natural. Genre affects what competition feels fair. Platform affects notification and re-engagement patterns tied to the leaderboard cadence.

**Default assumption if unknown:**
> Mobile F2P. Sessions of 5–15 minutes. Daily play expected from active players. Core loop repeatable within a single session.

---

### Q5 — What rewards can you offer?

What prizes are available to distribute to bracket winners at the end of each round? Do you have meaningful differentiation between brackets, or is the reward pool limited?

**Why this matters:** The reward bracket structure only works if the rewards are worth competing for. The design of brackets depends entirely on what you can actually offer. If rewards are weak, the design must lean harder on intrinsic prestige.

**Default assumption if unknown:**
> Soft currency (moderate amount) for all rewarded positions. Exclusive cosmetic or rare content for top bracket. Diminishing but meaningful value down through mid-tier brackets. Consolation prize (small soft currency) for the bottom reward bracket. Nothing for players outside all brackets.

---

### Q6 — What is your player mix?

Roughly, what is the spread from casual to competitive players? Are there significant spenders (whales) who could dominate groups if mixed with free players?

**Why this matters:** Random group composition with a large spending gap produces whale-dominated leaderboards where most players have no real chance. Knowing the mix determines whether and how to segment groups.

**Default assumption if unknown:**
> Standard F2P bell curve: approximately 60% casual (low engagement, low or no spend), 30% mid-tier (regular engagement, occasional spend), 10% competitive or paying (high engagement, meaningful spend). Meaningful whale population present but small.

---

### Q7 — What is your complexity budget?

How much development complexity can this leaderboard system absorb? A full league ladder with promotion, demotion, and group management is significantly more complex than a flat group-based leaderboard.

**Why this matters:** The right design for a small team with a constrained roadmap is different from the right design for a live service with engineering capacity to build a multi-tier system.

**Options:**
- **Simple** — flat groups, no leagues, no promotion/demotion. One round structure, repeat.
- **Standard** — flat groups with league ladder (3–5 tiers), promotion/demotion between tiers.
- **Full** — complete league pyramid, dynamic group composition, full reward differentiation per league tier.

**Default assumption if unknown:**
> Standard — league ladder with 4–5 tiers recommended. This is the minimum structure that generates full goal density across all time horizons. If Simple is required, flag the goal density tradeoff explicitly.

---

### Q8 — Should groups be random, or matched?

When players are assigned to competition groups, should assignment be random or based on some form of matching (progression tier, activity level, spend band)?

**Why this matters:** Random grouping is simple but can produce consistently unfair matchups — new players against veterans, free players against heavy spenders. Matching increases fairness and competitive integrity but adds system complexity.

**Default assumption if unknown:**
> Broad-band progress matching — players grouped with others at a similar progression stage or activity level. Not strict skill matching (too complex), but enough to prevent total mismatches. Groups refreshed each round.

---

## Phase 2: Confirm inputs before designing

After receiving answers (or accepting defaults), briefly restate what was collected:

> **Confirmed inputs:**
> - Score: [summary]
> - Player pool: [number]
> - Round length: [duration]
> - Game context: [summary]
> - Rewards: [summary]
> - Player mix: [summary]
> - Complexity budget: [Simple / Standard / Full]
> - Group composition: [Random / Matched]
> - Assumptions used: [list any defaults applied]

Ask: "Does this look right? Say go to proceed, or correct anything first."

---

## Phase 3: Design the leaderboard system

Once inputs are confirmed, produce the full design across these seven components.

---

### Component 1: Group structure

Design the group size and total number of groups.

Calculate:
- Recommended group size (default target: 50–100 players per group; smaller = more intimate, more volatile; larger = more stable, less personal)
- Total groups needed: `ceil(player_pool / group_size)`
- Note whether group size needs adjustment given pool size (very small pools may not justify groups at all)

Explain why this group size is recommended for this specific context.

---

### Component 2: League ladder

Design the pyramid structure.

For Standard and Full complexity:

Calculate the pyramid:
- Number of leagues recommended (typically 4–6 for most game scales)
- Groups per league, working from the top down:
  - Top league: 1 group
  - Each league below: multiply groups by `round_size / promotions_per_group`
  - Continue until bottom league accounts for the full player pool
- Present as a table:

| League | Name suggestion | Groups | Players | Notes |
|---|---|---|---|---|
| 5 (Top) | ... | 1 | [group_size] | Top league — 1 group only |
| 4 | ... | [n] | [n × group_size] | |
| 3 | ... | [n] | [n × group_size] | |
| 2 | ... | [n] | [n × group_size] | |
| 1 (Entry) | ... | [n] | [n × group_size] | |

Suggest league names appropriate to the game's theme. Flag the naming scalability problem if more leagues are likely to be added in future.

For Simple complexity:
- Single tier, flat groups, no promotion/demotion
- Note the goal density tradeoff: only immediate and short-term goals exist; medium-term and long-term goals are absent

---

### Component 3: Promotion and demotion

Specify the rules for moving between leagues.

Design:
- Players promoted per group per round (recommended: top 10–15% of group — enough to feel achievable, rare enough to feel meaningful)
- Players demoted per group per round (recommended: bottom 15–20% — enough to create tension without punishing casual play)
- What happens to new players: recommended entry point (bottom league, or a placement round)
- What happens to players in the top league: no promotion possible — design for this explicitly (see Component 7)
- What happens to players in the bottom league: no demotion below floor — they stay, which may require separate handling

Example values for a group of 100:
- Promote: top 10 players (10%)
- Safe zone: places 11–80 (no movement)
- Demote: bottom 20 players (20%)

Flag sandbagging risk if top reward bracket aligns with promotion threshold — this incentivizes intentional underperformance before a round ends. Recommend mitigations if risk is present.

---

### Component 4: Round structure and reset policy

Define the full rhythm of one competition cycle.

Specify:
- Round length (from confirmed input)
- When scores reset (start of each new round; all players return to 0)
- What carries forward vs. resets: league position carries forward; score does not
- Recommended soft launch into a round: 48-hour grace period where groupings are set but standings are provisional (reduces sandbagging at the start)
- End-of-round sequence: freeze standings → calculate brackets → distribute rewards → apply promotions/demotions → form new groups → start next round

Address the reset acceptance problem: if scores reset fully each round, veteran players lose lifetime score advantage. Frame this positively in UX: "A new season begins — everyone starts fresh."

---

### Component 5: Reward brackets

Design the bracket structure for one group of the default size.

Recommended starting structure for a group of 100:

| Bracket | Positions | Players | Reward |
|---|---|---|---|
| Grand Prize | 1 | 1 | [top reward from confirmed input] |
| Major Prize | 2–5 | 4 | [strong reward] |
| Minor Prize | 6–20 | 15 | [moderate reward] |
| Consolation | 21–50 | 30 | [small reward] |
| Nothing | 51–100 | 50 | — |

Adjust bracket boundaries to fit the confirmed reward pool. If rewards are limited, compress the structure. If rewards are abundant, widen mid-tier brackets.

Evaluate coverage:
- 50% of the group receives something — healthy baseline
- 1% receives the top prize — maintains prestige
- Bottom 50% receives nothing — creates urgency to stay above the cut line

Note: also design per-league reward differentiation if using a ladder. Higher leagues should receive more valuable rewards for equivalent bracket positions — this makes league promotion feel economically meaningful, not just prestigious.

Flag reward inflation risk if the same reward is distributed every week at the same rate — over time it may devalue. Recommend seasonal variation or rotating exclusive items.

---

### Component 6: Group composition approach

Specify how players are assigned to groups each round.

Based on confirmed input (Random or Matched):

**If Matched:**
- Define the matching dimension: progression tier, cumulative season score, activity band, or spend tier
- Describe how to segment the player pool into bands before group assignment
- Specify that group composition should be refreshed every round (no static groups)
- Handle edge cases: bands with too few players to form complete groups (merge adjacent bands)

**If Random:**
- Flag the fairness risk with any whale population present
- Recommend a minimum viable matching layer: at least exclude players with 5× higher round scores from mixing with entry-level players

Anti-sandbagging measures:
- Score floor: players cannot fall below their previous round's score by more than X% through inaction
- Late-round freeze: no demotion movement in the final 24 hours of a round (prevents last-minute sandbagging)

---

### Component 7: Top-of-ladder design

Address what happens when a player reaches and holds the top position.

Design one of the following approaches based on complexity budget and game context, and explain the tradeoff:

**Option A — Expanding ladder**
Add a new top league whenever the existing top league is full and promotion candidates exist. Name leagues with a scalable convention (numbered seasons, themed names drawn from a pre-defined list). Tradeoff: top league loses permanence over time.

**Option B — Periodic full reset**
Reset the entire league ladder periodically (e.g., each season). All players re-enter the bottom league and reclimb. Previous top position is commemorated but not held. Tradeoff: veterans lose status; must be designed in from the beginning to be accepted.

**Option C — Prestige layer**
Top-league players who have won accumulate a prestige score or title that exists outside the ladder. The ladder remains competitive; prestige is additive, not substitutive. Tradeoff: requires additional design and display work.

Recommend the most appropriate option given the confirmed complexity budget and player mix.

---

### Component 8: Goal density summary

Map the resulting design to the full goal hierarchy and verify coverage:

| Goal tier | Mechanism in this design | Assessment |
|---|---|---|
| Immediate — overtake the player above me | Visible neighbor scores in group | [present / absent / weak] |
| Short-term — reach the next reward bracket | Bracket thresholds within group | [present / absent / weak] |
| Medium-term — earn promotion | League promotion threshold | [present / absent / weak] |
| Long-term aspirational — reach the top | League ladder | [present / absent / weak] |
| Defensive — avoid demotion | Demotion zone | [present / absent / weak] |

If any tier is absent or weak, flag it and suggest how to address it.

---

### Component 9: Economy output summary

Summarize the resource flow this system will generate per round:

- Total players rewarded per round (across all groups and leagues): [calculated]
- Total rewards distributed per round by bracket tier: [table]
- Annualized reward output (at confirmed round cadence): [calculated]
- Flag if reward output appears high relative to what was described — potential inflation risk

---

### Component 10: Risk register

List the top risks in the proposed design and their mitigations:

| Risk | Likelihood | Mitigation |
|---|---|---|
| Sandbagging | Medium–High if rewards are large | Late-round score freeze; score floor |
| Whale group dominance | Medium if no matching | Spend-band separation in group assignment |
| Top-league stagnation | High over 6+ months | Choose and implement top-of-ladder strategy from Component 7 |
| Reward inflation | Medium over time | Rotate exclusive content; seasonal reward variation |
| Reset backlash | Medium if introduced post-launch | Communicate as "season system" from day one |
| Low participation in early rounds | Medium for new features | Seed initial groups manually or use provisional standings |

---

## Response structure

### Confirmed Inputs
- ...
- Assumptions applied: ...

### Group Structure
- Group size: ...
- Total groups: ...

### League Ladder
- Table: ...
- Naming approach: ...

### Promotion / Demotion
- Promote: top [n] players per group
- Demote: bottom [n] players per group
- Sandbagging risk: ...

### Round Structure
- Round length: ...
- Reset policy: ...

### Reward Brackets
- Table (per group of [n]): ...
- Per-league differentiation: ...

### Group Composition
- Approach: ...
- Anti-exploitation measures: ...

### Top-of-Ladder
- Recommended approach: ...
- Rationale: ...

### Goal Density Summary
- Table: ...

### Economy Output
- Rewards per round: ...
- Annualized: ...

### Risk Register
- Table: ...

### Designer Notes
- What to validate in playtesting: ...
- What to instrument for live data: ...

---

## Fast mode

If the user provides most answers upfront, skip the question phase and go straight to design — but list the assumptions used at the top of the output.

If the user provides almost nothing, ask all eight questions in a single clean list. Do not proceed until at least Q1 (score type) and Q2 (player pool) are answered or defaulted.

---

## Working principle

The goal is not to produce the most sophisticated leaderboard. It is to produce the right leaderboard for this game, this player base, and this team — one that generates maximum goal density within the confirmed constraints, and that a designer can hand directly to an engineer as a specification.
