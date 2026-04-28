---
name: game-design-granular-player-motivation-audit
description: Audit a game, feature, progression system, social system, live-ops loop, monetization surface, or onboarding flow through a granular player motivation taxonomy. Use when evaluating which player motivation archetypes a design strongly serves, neglects, or actively repels; when comparing a concept against segments such as Steady Advancers, Curious Solvers, Competitive Achievers, Imaginative Creators, Strategic Leaders, Immersed Storywriters, Reward Seekers, Passionate Belongers, and Category Enthusiasts; when translating player research into practical design recommendations; or when you need a more nuanced alternative to a simple Bartle-style motivation read.
---

# Game Design Granular Player Motivation Audit

Audit a design by asking which granular motivation segments it serves, excludes, overloads, or misunderstands.

Use this skill to evaluate how a game, feature, flow, or system lands across a detailed player motivation taxonomy. Treat the archetypes as **motivational lenses**, not rigid human categories.

## Core principle

A feature does not need to serve every motivation profile equally.

The real question is whether the pattern is **intentional, healthy, and appropriate** for the feature's role in the product. A narrow feature can be good. An accidentally narrow feature, or one that pretends to be broad while serving only one motivation profile, usually creates confusion, coldness, or churn.

This taxonomy is especially useful because it gives you two layers at once:
- **motivation themes** explaining what psychological needs the design activates
- **archetypes** predicting who will respond well, who will feel indifferent, and who may be alienated

## Start with the source notes

Before auditing, read `references/granular-taxonomy-notes.md`.

That file contains the source-faithful motivation list, archetype definitions, distinct motivations, anti-motivations, and interpretation rules extracted from the document.

## Motivation themes in this taxonomy

Use these 10 themes as the causal layer underneath the archetypes:

1. **Personal Achievement**
2. **In-Game Achievement**
3. **Cognitive**
4. **Emotional Immersion**
5. **Creation + Exploration**
6. **Affiliation**
7. **Independence**
8. **Status + Rank**
9. **Leadership + Power**
10. **Rewards**

When auditing, ask both:
- **Which archetypes does this design serve?**
- **Which underlying motivation themes are doing the work?**

## Archetypes

Audit across these nine archetypes:

- **Steady Advancer** - wants simple, legible progress and short-burst accomplishment
- **Curious Solver** - wants cognitive stimulation, learning, and mental sharpness
- **Competitive Achiever** - wants rank, skill proof, comparison, and bragging rights
- **Imaginative Creator** - wants expression, control, creation, nurturing, and freeform exploration
- **Strategic Leader** - wants smart play, leadership, team success, prestige, and mastery through coordination
- **Immersed Storywriter** - wants absorption, narrative meaning, emotional connection, and lived identity in a world
- **Reward Seeker** - wants prizes, payouts, currencies, bonuses, and tangible wins
- **Passionate Belonger** - wants friendship, fit, support, team identity, and social belonging
- **Category Enthusiast** - a residual segment defined more by attachment to a game category than by a strong cross-category motivation profile; treat with caution and do not overgeneralize from it

## Use the doc, not generic intuition

Do not flatten these archetypes into generic player stereotypes.

Important distinctions from the source document:
- **Competitive Achiever** is not the same as **Strategic Leader**. The former centers on earned superiority, rank, and bragging rights; the latter layers in leadership, tactical planning, teaching others, and team success.
- **Imaginative Creator** is not the same as **Immersed Storywriter**. The former seeks authorship, control, nurture, and expression; the latter seeks absorption, emotional connection, and living inside a meaningful world.
- **Passionate Belonger** is not just "Socializer." They are motivated less by abstract sociability and more by fitting in, support, being part of a team, and belonging to something bigger.
- **Reward Seeker** can produce misleading engagement signals. Frequent claiming and ritualized reward harvesting may indicate reward dependence more than broad emotional appeal.
- **Category Enthusiast** is explicitly a caution segment. The source note says you cannot reliably design for or market to them as a clean cross-category segment.

## What to produce

Generate:
1. **Audit target** - what is being reviewed and what it is supposed to do
2. **Motivation-theme reading** - which of the 10 themes the design activates
3. **Archetype-by-archetype reading** - how each player lens experiences the design
4. **Segment profile** - which archetypes are strongly served, weakly served, or actively frustrated
5. **Mismatch diagnosis** - where the design overcommits, neglects, or creates motivational conflict
6. **Recommendations** - what to strengthen, soften, separate, or clarify

## Process

### 1. Define the audit target
Clarify:
- what is being audited
- what the feature or system is supposed to achieve
- whether it is core, optional, onboarding, progression, live-ops, social, or monetization
- who the intended audience seems to be
- whether the design needs broad appeal or is allowed to be niche

Write:
- **Design being audited**
- **Intended job**
- **Audience hypothesis**
- **Breadth requirement**

### 2. Identify the active motivation themes
First map the design to the 10 themes.

Ask:
- Does it create challenge, mastery, or accomplishment?
- Does it create collection, completion, or advancement pressure?
- Does it reward thinking, memory, learning, or problem-solving?
- Does it create emotional, narrative, or identity absorption?
- Does it support creation, customization, or exploration?
- Does it create belonging, support, or connection?
- Does it create freedom, alternate identity, or safe control?
- Does it create rank, comparison, or prestige?
- Does it create leadership, power, or command?
- Does it rely on prizes, payouts, bonuses, or extrinsic rewards?

Use this format:

| Motivation Theme | Strength (Low/Med/High) | Evidence | Likely Effect |
|---|---|---|---|
| Personal Achievement | ... | ... | ... |
| In-Game Achievement | ... | ... | ... |
| Cognitive | ... | ... | ... |
| Emotional Immersion | ... | ... | ... |
| Creation + Exploration | ... | ... | ... |
| Affiliation | ... | ... | ... |
| Independence | ... | ... | ... |
| Status + Rank | ... | ... | ... |
| Leadership + Power | ... | ... | ... |
| Rewards | ... | ... | ... |

### 3. Audit for Steady Advancers
Use the source assumptions:
- they want simple, straightforward progress
- they often treat games as limited me-time
- gaming is not a central identity
- heavy complexity, immersion, or competition often pushes them away

Ask:
- Is progress simple, legible, and satisfying in short sessions?
- Can players feel accomplishment without heavy cognitive load?
- Is the feature easy to resume while multitasking or returning casually?
- Does it avoid overcomplication, excessive immersion demands, or punishing friction?
- Would a busy player keep this installed, or delete it quickly?

Look for:
- visible next steps
- level-by-level progression
- short-burst payoff
- low-friction repetition
- reliability and familiarity

### 4. Audit for Curious Solvers
Use the source assumptions:
- they want to feel smart
- they like challenge, learning, and cognitive upkeep
- they may justify play because it feels mentally beneficial
- rewards, immersion, and power are relatively weak drivers

Ask:
- Does this provide meaningful thinking, learning, memory use, or problem-solving?
- Does challenge escalate in an interesting way?
- Is the player allowed to feel smart?
- Is the system mentally active rather than merely busy?
- Does the feature become richer with insight, not just repetition?

Look for:
- puzzles and strategic decisions
- pattern recognition
- escalating complexity
- testable hypotheses
- performance feedback
- friendly competition with known others

### 5. Audit for Competitive Achievers
Use the source assumptions:
- they want rank, superiority, and bragging rights
- they care about winning fairly
- they dislike pay-to-win contamination
- story matters only as context, not as emotional purpose

Ask:
- Does the design create rankings, visible superiority, or skill comparison?
- Can players prove they are better than others?
- Is the contest fair enough to feel earned?
- Does the feature create bragging rights without collapsing into pay-to-win sludge?
- Is the skill test sharp, legible, and respected?

Look for:
- ladders and ranks
- score attack
- direct competition
- mastery metrics
- visible performance comparison
- clear victory logic

### 6. Audit for Imaginative Creators
Use the source assumptions:
- they want authorship, expression, control, and nurturing
- they value freedom of choice as self-expression
- immersion often comes through building and curating, not only through plot
- status competition is actively unimportant

Ask:
- Does the design support self-expression, creation, care, or world ownership?
- Can players shape outcomes in a personally meaningful way?
- Does it allow exploration, customization, and freedom?
- Is there room for nurturing, curation, or building something that feels like theirs?
- Is the feature genuinely expressive, or only cosmetically decorative?

Look for:
- customization depth
- sandbox affordances
- personal spaces/worlds
- nurturing loops
- open-ended exploration
- ownership and curation

### 7. Audit for Strategic Leaders
Use the source assumptions:
- they are social, competitive, and cognitively engaged
- they want to outthink as well as outperform
- they value leadership, team success, prestige, and mastery
- they will form new relationships if it helps them compete well

Ask:
- Does the design reward planning, outthinking, coordination, or command?
- Can players lead others or teach others to improve team success?
- Does it create prestige through competence and group impact?
- Is there room for tactical research, optimization, or team composition decisions?
- Does the feature let strong players express leadership, not just raw execution skill?

Look for:
- team roles
- command surfaces
- tactical depth
- coordinated play
- leadership recognition
- strategic counterplay
- optimization communities

### 8. Audit for Immersed Storywriters
Use the source assumptions:
- they want emotional connection, freedom, and absorption
- they often see games as art or as meaningful worlds
- multiplayer is not usually the draw
- they care about coherent atmosphere, identity, and consequence

Ask:
- Does the design create emotional connection, narrative context, or world absorption?
- Can the player feel like part of a story or identity larger than themselves?
- Does the feature support exploration, consequence, atmosphere, or character attachment?
- Is there enough coherence to sustain immersion?
- Would the feature still feel meaningful without competition or reward wrappers?

Look for:
- narrative stakes
- atmospheric framing
- worldbuilding
- player identity fantasy
- emotional character ties
- choices with consequences
- exploratory texture and surprises

### 9. Audit for Reward Seekers
Use the source assumptions:
- they are primarily motivated by prizes and payout visibility
- frequent rewards and big-win fantasy matter more than depth
- they may ritualize claim behavior across games
- other motivation themes can be surprisingly weak

Ask:
- Is the feature clearly and frequently rewarding?
- Are the prizes, currencies, bonuses, or payout moments visible and motivating?
- Does the feature rely too much on reward wrappers to stay interesting?
- Could it encourage ritualized claim behavior more than genuine play?
- Is the reward cadence strong enough for this audience, and too strong for everyone else?

Look for:
- jackpots and payout moments
- daily bonuses
- reward ladders
- currency accumulation
- gacha or prize logic
- claim rituals

### 10. Audit for Passionate Belongers
Use the source assumptions:
- they care about fit, support, acceptance, team identity, and belonging to something larger
- they are not strongly motivated by bragging rights or superiority
- social warmth and participation matter more than dominance

Ask:
- Does the design support friendship, team identity, acceptance, and social fit?
- Are there reasons to help, join, coordinate, or feel part of a group?
- Does it create social warmth rather than only social competition?
- Can players build belonging through repeated interaction?
- Does the system make people feel included, or merely evaluated?

Look for:
- team play
- help/gifting loops
- guild or club identity
- communication tools
- shared rituals and events
- visible support structures
- collaborative ownership

### 11. Audit for Category Enthusiasts
Treat this segment carefully.

This is not a clean motivation cluster like the others. The source note is effectively a warning label.

Ask:
- Is this feature heavily reliant on category conventions or genre literacy?
- Would it mainly appeal to players already invested in the category?
- Is the appeal portable across audiences, or only compelling to existing fans?
- Are you designing for motivation, or just for people who already like this kind of product?

Look for:
- genre-native assumptions
- insider affordances
- fan-service or convention-heavy design
- weak appeal outside the category

### 12. Build the segment profile
For each archetype, rate the design as:
- **Strongly served**
- **Moderately served**
- **Weakly served**
- **Actively frustrated**

Use this format:

| Archetype | Rating | Why | Likely Response |
|---|---|---|---|
| Steady Advancer | ... | ... | ... |
| Curious Solver | ... | ... | ... |
| Competitive Achiever | ... | ... | ... |
| Imaginative Creator | ... | ... | ... |
| Strategic Leader | ... | ... | ... |
| Immersed Storywriter | ... | ... | ... |
| Reward Seeker | ... | ... | ... |
| Passionate Belonger | ... | ... | ... |
| Category Enthusiast | ... | ... | ... |

### 13. Diagnose mismatch and cross-segment friction
Ask:
- Is the feature clearly built for one archetype while pretending to be for everyone?
- Do reward structures damage immersion, fairness, or belonging?
- Does competition poison what should be a safe or creative space?
- Does simplicity help Steady Advancers while starving Curious Solvers or Strategic Leaders?
- Does category depth delight insiders while excluding broader audiences?
- Does the design accidentally conflict with an archetype's explicit anti-motivations?

Common mismatch patterns:
- **Checklist comfort** - smooth for Steady Advancers but dead for deeper motivations
- **Brainy shell** - intellectually signaled but mechanically shallow for Curious Solvers
- **Prestige poison** - rank/status pressure overwhelms players who wanted support, story, or expression
- **Sandbox without authorship** - promises creator fantasy but offers cosmetic busywork only
- **Teamwork without belonging** - multiplayer presence exists, but no real support or social warmth
- **Reward wrapper syndrome** - prizes carry a feature whose intrinsic value is weak
- **Genre capture** - feature is legible only to category insiders, reducing broader motivational reach
- **Anti-motivation collision** - a feature leans on exactly the drivers the intended audience does not care about

### 14. Convert findings into design actions
For each major issue, specify:
- **Archetype or theme affected**
- **Current issue**
- **Design cause**
- **Suggested change**
- **Expected effect**

Prioritize recommendations that:
- preserve the intended core audience
- reduce accidental exclusion
- remove false promises
- align feature structure with the motivations that truly drive it

## Response structure

### Audit Target
- ...

### Motivation Theme Profile
- ...

### Archetype Readout
- Steady Advancer: ...
- Curious Solver: ...
- Competitive Achiever: ...
- Imaginative Creator: ...
- Strategic Leader: ...
- Immersed Storywriter: ...
- Reward Seeker: ...
- Passionate Belonger: ...
- Category Enthusiast: ...

### Segment Profile
- ...

### Mismatch Diagnosis
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode
- Which 2 to 3 archetypes does this mainly serve?
- Which motivation themes are doing most of the work?
- Which archetype gets the least value?
- Which archetype could be actively repelled?
- Are you colliding with any explicit anti-motivations from the source doc?
- Is the narrowness intentional and acceptable?
- What one change would broaden appeal without weakening the core target?

## Working principle

A design should not be judged only by whether it motivates action.

Judge it by **who** it motivates, **why** it motivates them, **which motivations it accidentally rejects**, and whether that motivational profile fits the role the design is supposed to play.
