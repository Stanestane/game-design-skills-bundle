---
name: game-design-premium-pass-audit
description: Audit an existing or proposed premium pass (battle pass, season pass) for value proposition integrity, progression health, free track balance, reward pacing, engagement loop quality, and economy impact. Use when evaluating a pass before launch, diagnosing why a pass is underperforming, reviewing a competitor's pass design, or stress-testing a proposed structure before committing to production.
---

# Game Design Premium Pass Audit

Audit a premium pass as a complete monetization and engagement system — not just a reward list, but a time-bounded contract between the player and the game. The pass makes a promise: pay this price, invest this time, and receive this value. The audit evaluates whether that promise is honest, achievable, and motivating for the right reasons.

## Core principle

A premium pass that players feel obligated to complete is not the same as one they want to complete. Obligation drives short-term revenue and long-term churn. The audit's job is to find where the design relies on compulsion instead of desire — and where genuine value is being left on the table.

---

## What to produce

1. **Audit target** — what is being reviewed and its context
2. **Value proposition audit** — does the price feel worth it?
3. **Progression velocity audit** — can the right players realistically complete it?
4. **Free track audit** — does the free track earn its place?
5. **Reward pacing audit** — when and how do good rewards land?
6. **Engagement loop audit** — how does the pass create and sustain sessions?
7. **Economy impact audit** — what does the pass inject into and extract from the game economy?
8. **Failure pattern diagnosis** — which named anti-patterns are present?
9. **Recommendations** — prioritised, specific, actionable

---

## Process

### 1. Define the audit target

Clarify:
- Game title, genre, platform, and monetization model
- Pass name and current season (if live) or design stage
- Price point and the currency it is sold in
- Season duration
- Number of tiers on the free and premium tracks
- Reward types available (cosmetics, currency, gameplay items, XP boosts, etc.)
- Whether this is the first pass or part of an ongoing series

If details are incomplete, note assumptions and flag them.

---

### 2. Value proposition audit

The core question: does what the player gets justify what they pay?

Ask:
- What is the price in local currency or premium currency?
- What is the most valuable item on the premium track, and is it available anywhere else?
- Does the pass return premium currency? If so, how much relative to its cost?
- What is the total notional value of all premium rewards (using in-game price equivalents where available)?
- Is the headline reward (the thing shown in marketing) gated behind completion, or available early?
- Are any rewards timed-exclusive, or could they return in a shop?

Evaluate:

**Currency return ratio** — if the pass costs 1,000 premium currency and returns 600, it is a 60% return. Below 50% is extractive. Above 80% approaches "pays for itself" territory. Flag both extremes.

**Exclusivity value** — passes where all rewards will eventually appear elsewhere have weak value propositions. Passes where the premium track contains permanently exclusive items have strong ones.

**Perceived value vs. real value** — a pass full of XP boosts and low-value consumables may have high notional value but low perceived value. Cosmetics and exclusive content punch above their economic weight.

---

**Discount ratio** (for passes priced in real money or convertible premium currency)

Calculate the effective discount the pass offers against buying the same content individually:

1. Sum the retail value of every premium track reward — use the in-game shop price for each item where available. For items only obtainable through the pass (no direct price reference), estimate using comparable items of similar type and rarity. For premium currency rewards, convert at the base purchase rate (the worst rate for the player — this is the rate an informed player would use). Flag any rewards that cannot be valued and note they are excluded.
2. Divide total retail value by the pass price to get the **value multiplier**: total retail value ÷ pass price = Nx value.
3. Express as a **discount percentage**: 1 − (pass price ÷ total retail value) × 100 = X% discount.

Interpret:
- **Below 30% discount** (less than 1.4x value) — weak; players are paying near-retail for convenience of bundling. Likely to generate negative sentiment once community spreadsheets the math.
- **30–60% discount** (1.4–2.5x value) — adequate; players feel they are getting a deal, but it is not remarkable.
- **60–80% discount** (2.5–5x value) — strong; clear perceived value, typical of well-designed passes. Players feel rewarded for purchasing.
- **Above 80% discount** (5x+ value) — exceptional or inflated; verify that item valuations are realistic and not padded with low-utility content priced artificially high.

If the pass is priced in premium currency rather than real money, convert the pass price to real money at the base currency bundle rate before running this calculation.

---

**Breakeven tier** (from the player's perspective)

The breakeven tier is the tier at which the cumulative retail value of rewards received equals or exceeds the cost of the pass. This is the point at which a player who stops playing has already received their money's worth.

Calculate:
1. Assign a retail value to each premium track reward (same methodology as discount ratio above).
2. Build a cumulative value curve: tier 1 total, tier 2 total, tier 3 total, and so on.
3. Identify the tier where cumulative value first meets or exceeds the pass price — this is the **breakeven tier**.
4. Express as a percentage of total tiers: breakeven tier ÷ total tiers × 100.

Interpret:
- **Breakeven in the first 20% of tiers** — very generous; purchase anxiety is minimal and player goodwill is high. Risk: players who complete early may feel the remaining pass has no pull.
- **Breakeven in tiers 20–40%** — healthy; players feel they earned their money back quickly enough to feel safe, with meaningful content still ahead.
- **Breakeven in tiers 40–60%** — acceptable but slightly uncomfortable; players who quit mid-season will feel mild regret about the purchase.
- **Breakeven in tiers 60–80%** — aggressive; a significant portion of purchasers will never reach breakeven. Likely to generate negative community perception once discovered.
- **Breakeven in the final 20% of tiers, or never** — extractive; the pass is priced above the value of content most players will realistically access. High refund and negative review risk.

Note whether the breakeven tier aligns with the progression velocity: if the breakeven tier requires more sessions than a casual player can reasonably complete, flag the mismatch explicitly — the pass is pricing in content the casual buyer will never access.

---

Label the overall value proposition finding:
- **Strong** — clear value, price feels proportionate, currency return meaningful, breakeven accessible
- **Adequate** — value is defensible but thin; some players will feel short-changed
- **Weak** — price is hard to justify from the reward list; likely to generate negative sentiment
- **Extractive** — rewards are low-value, currency return is poor, breakeven is out of reach for most buyers

---

### 3. Progression velocity audit

The core question: can the player realistically complete the pass within the season?

Ask:
- How many total XP (or equivalent progression points) are required to reach the final tier?
- How many tiers does the pass have?
- What are the XP sources available: daily missions, weekly missions, match/session XP, bonus events?
- What is the expected XP per session for a casual player (1–3 sessions/week), regular player (4–5 sessions/week), and dedicated player (daily)?
- Is there a maximum XP cap per day or week?
- Are there paid tier skips? At what cost?

Calculate:
- **Sessions required to complete** for each player type
- **Days of play required** at each engagement level
- **Completion rate estimate**: what % of pass purchasers likely complete all tiers?

Evaluate:
- **Casual reachability**: if a casual player (2–3 sessions/week) cannot reach the final premium tier within the season, flag it. Many players will feel they "wasted" their purchase.
- **Healthy velocity**: a well-tuned pass is completable for a regular player with moderate effort, but requires dedication from a casual player. The sweet spot puts final-tier completion at around 60–70% of the season's total available playtime.
- **Skip economics**: if tier skips cost more in total than the pass itself, it signals the pass was designed to capture skip revenue rather than pass revenue. Flag this as a structural monetization conflict.

Label the finding:
- **Achievable** — regular and dedicated players complete comfortably; casual players can finish with consistent effort
- **Stretched** — regular players can complete; casual players will struggle and likely feel burned
- **Gated** — even regular players face a significant grind; completion requires near-daily play
- **Whale-targeted** — completion is only realistic through purchased tier skips

---

### 4. Free track audit

The core question: does the free track have genuine value, or is it a sales funnel dressed as a feature?

Ask:
- How many tiers are on the free track?
- What reward types appear on the free track?
- Are there any headline rewards available for free, or only low-value fillers?
- Does the free track feel like a complete experience, or a deliberate preview of what players are missing?
- Is the free track progression the same XP curve as the premium track?

Evaluate:
- A free track that generates **genuine satisfaction** builds goodwill and acts as a long-term funnel for pass purchases. Players who feel the free track respects their time are more likely to buy a future pass.
- A free track that exists **purely to display what you're missing** is manipulative and breeds resentment. It is a short-term conversion tool with long-term reputation cost.
- The **free track should contain at least one reward that non-paying players feel good about receiving** — a cosmetic, a meaningful currency amount, or a piece of content with real utility.

Label the finding:
- **Generous** — free track delivers real value; non-payers feel respected
- **Fair** — free track is thin but honest; expectations are set correctly
- **Deceptive** — free track exists primarily to create FOMO; non-payers feel excluded rather than rewarded
- **Absent** — no meaningful free track; the pass is a pure paywall

---

### 5. Reward pacing audit

The core question: do rewards land at the right moments to sustain motivation throughout the season?

Ask:
- Where are the highest-value rewards positioned in the tier sequence?
- Are there reward dead zones — long stretches of low-value filler that players must grind through?
- Is there a "hero reward" (the most desirable item) positioned at the final tier or earlier?
- How does reward density change across the season — are early tiers more rewarding than late ones?
- Are milestone rewards clearly signposted, or buried in an undifferentiated reward list?

Evaluate the pacing curve shape:
- **Front-loaded** — strong early rewards build habit and reduce refund requests; risk is players disengage after collecting what they wanted
- **Back-loaded** — hero reward at the end drives completion behaviour; risk is early dropout if mid-tier rewards feel weak
- **Even distribution** — consistent reward cadence; sustainable but can feel predictable and fail to create excitement spikes
- **Reward deserts** — long stretches of low-value rewards are the most common pacing failure and a direct cause of mid-season disengagement

Identify and flag reward deserts: any sequence of five or more tiers where no item would meaningfully motivate a player to continue.

---

### 6. Engagement loop audit

The core question: does the pass create sessions, or merely reward sessions that would have happened anyway?

Ask:
- What mission or challenge structures drive pass XP? Daily, weekly, or both?
- Are missions designed around the game's core loop, or do they create artificial play patterns (e.g., "use this weapon you don't enjoy")?
- Is there a check-in incentive — a reason to open the game specifically because of the pass?
- Does the pass communicate urgency at the right moments (approaching tier thresholds, approaching season end)?
- Is there a mid-season catch-up mechanism for players who fall behind?
- What happens at season end — grace period, carry-over, instant completion offer?

Evaluate:
- **Session creation vs. session capture**: a well-designed pass gives players a specific reason to open the game today. A poorly designed one just rewards time already spent.
- **Mission design quality**: missions that align with what players already enjoy doing feel like bonuses. Missions that force artificial play patterns generate friction and resentment.
- **Urgency calibration**: urgency should build naturally as the season progresses — felt as excitement, not panic. If urgency is present from the first week, it signals the XP velocity is too slow.
- **Catch-up design**: passes with no catch-up mechanism punish life events (travel, illness, busy periods) and convert lapsed players into churned ones.

---

### 7. Economy impact audit

The core question: what does this pass do to the game's broader economy?

Ask:
- How much premium currency does the pass cost?
- How much premium currency does the pass return?
- How much soft currency, hard currency, or other economic resources are distributed through pass rewards?
- Does the pass compete with the in-game shop, or complement it?
- What is the total resource injection from one pass season across the active player base?
- Is this the game's primary monetization vehicle or one of several?

Evaluate:
- **Currency return sustainability**: if the pass fully pays for itself in premium currency, it is a strong player-friendly signal but may cannibalise direct premium currency sales. If it returns nothing, it is extractive. The healthy middle ground returns 40–70% of its cost.
- **Inflation risk**: passes that distribute large quantities of soft currency or progression-accelerating resources can devalue other content and compress the sense of progression elsewhere in the game. Flag if pass rewards include significant quantities of resources that are otherwise earned through core gameplay.
- **Shop competition**: if the pass offers cosmetics at lower effective cost than the direct shop, it may depress shop revenue. If the pass and shop are clearly differentiated (exclusive vs. available), they coexist healthily.
- **Monetization stack**: identify whether the pass sits alongside loot boxes, direct purchase, or subscription. Passes that add to an already complex monetization stack increase player cognitive load and resentment risk.

---

### 8. Diagnose failure patterns

Name and describe each present anti-pattern:

- **FOMO trap** — the pass is designed around what players will lose if they don't engage daily, not what they gain by playing. Anxiety-driven sessions, not fun-driven ones.
- **Treadmill grind** — XP velocity requires near-daily play to complete. Players feel obligated rather than motivated. The pass becomes a second job.
- **Value desert** — the free track is so thin that non-paying players feel the game is holding content hostage. Builds resentment rather than purchase intent.
- **Pay-to-skip culture** — tier skips are priced and positioned as the intended completion path, not an emergency option. Signals that the progression was designed to be sold, not played.
- **Currency mirage** — the pass "pays for itself" but only in premium currency that can only be spent on the next pass. Creates the illusion of value while locking players into a closed loop.
- **Completion anxiety** — players who bought the pass are aware they will not complete it. The pass generates guilt rather than enjoyment. Common when velocity is miscalibrated or life gets in the way.
- **Content drought** — the season extends beyond the lifespan of interesting content. Players complete the pass early and disengage; the remaining season feels like an empty obligation.
- **Hero hostage** — the most desirable reward is placed at or near the final tier, explicitly to force completion grinding. Creates resentment when players realise the design intent.
- **Reward homogeneity** — all rewards are the same type (e.g., all cosmetics, all currencies) with no variety. Fails to serve different player motivation profiles across the season.
- **Whale neglect** — the pass is calibrated for the average player, leaving highest-value customers with nothing additional to purchase or pursue. Fails to capture the spending ceiling.

---

### 9. Convert findings into recommendations

For each significant issue:
- **Issue** — what is wrong
- **Why it hurts** — specific player experience or metric impact
- **Fix direction** — what structural change addresses it
- **Priority** — Critical / Important / Polish

---

## Response structure

### Audit Target
- Game, pass name, season, price, duration, tier count

### Value Proposition
- Verdict: Strong / Adequate / Weak / Extractive
- Currency return ratio: [X]%
- Discount ratio: [X]% discount ([N]x value multiplier)
- Breakeven tier: tier [N] of [M] ([X]% through the pass) — [generous / healthy / acceptable / aggressive / extractive]
- Breakeven vs. casual completion: [does a casual player reach breakeven before the season ends?]
- Key findings: ...

### Progression Velocity
- Verdict: Achievable / Stretched / Gated / Whale-targeted
- Sessions to complete by player type: ...
- Key findings: ...

### Free Track
- Verdict: Generous / Fair / Deceptive / Absent
- Key findings: ...

### Reward Pacing
- Curve shape: Front-loaded / Even / Back-loaded / Deserted
- Reward deserts identified: ...
- Key findings: ...

### Engagement Loop
- Session creation vs. capture: ...
- Mission design quality: ...
- Key findings: ...

### Economy Impact
- Currency return ratio: ...
- Inflation risk: ...
- Shop interaction: ...

### Failure Patterns Present
- [List each with brief description]

### Recommendations
1. [Critical] ...
2. [Important] ...
3. [Polish] ...

---

## Fast mode

If the user provides a quick description and wants a rapid read, ask only:
- What is the price (real money or premium currency) and what does the premium track include?
- How long is the season and how many tiers?
- What would the rewards cost if bought individually from the shop?
- Can a player who plays 3–4 sessions a week complete it?
- What is the most valuable thing on the free track?
- Does the pass return any premium currency?

Use these to calculate the discount ratio and breakeven tier as part of the fast output.

Produce a condensed audit covering value, velocity, and the two or three most significant failure patterns present.

---

## Working principle

A premium pass that players resent completing is worse than no pass at all. The audit's job is to find where the design is relying on obligation instead of desire — and to name it clearly enough that the team can fix it before it ships.
