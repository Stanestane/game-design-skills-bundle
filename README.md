# Game Design Skills Bundle

A curated bundle of reusable game design skills for OpenClaw / ClawHub-style agent workflows.

This repository collects a set of practical design skills covering:
- emotional direction
- design decision workflows
- player motivation and need audits
- prototyping under uncertainty
- creative unblockers
- FTUE analysis
- pitch deck review

These skills are designed to be used either:
- as installed skill folders in an OpenClaw workspace, or
- as packaged `.skill` files from the `package-skills/` folder.

They now also include beginner-oriented planning skills for turning rough game concepts into sane first steps, team plans, and budget ranges, plus a project-adjacent collaboration skill for analyzing recurring conflict patterns on software teams.

## Repository structure

- `game-design-*/` - individual skill folders
- `package-skills/` - packaged distributable `.skill` files
- `game-design-skill-catalog.md` - compact local catalog/index

## Skills

### 0. game-dev-first-steps
**What it does:**
Helps beginners or early-stage indie teams turn a rough game idea into a practical starting plan, prototype strategy, or pitchable vertical-slice path.

**Use it when:**
- someone asks how to start making a game
- the concept sounds exciting but the order of work is fuzzy
- a solo dev, duo, or small team needs help scoping the first milestone
- the team needs advice on what to build now versus what to postpone

**Best for:**
Beginner-friendly concept scoping and early development sequencing.

**Example prompt:**
> I have an idea for a mobile game where you defend a train from bandits. I'm a solo developer. What should I figure out first, what should I prototype first, and what should I postpone if I want a pitchable vertical slice?

**Short blurb:**
A beginner-friendly skill that turns rough game ideas into practical first steps, sane milestone planning, and realistic build order advice.

---

### 0.5 game-dev-team-gap
**What it does:**
Helps a beginner or early-stage team figure out which roles and skill areas are missing, weakly covered, or dangerously overloaded for a specific game concept and target milestone.

**Use it when:**
- someone asks who is missing from the team
- a concept seems larger than the current team can safely handle
- a solo dev, duo, or small team needs to understand its weakest coverage
- no team has been described yet and the user wants the minimum viable team for the project

**Best for:**
Beginner-friendly role-gap diagnosis and minimum-team planning.

**Example prompt:**
> We want to make a small co-op survival game for PC and mobile-friendly art style. We have one programmer and one 2D artist. What roles are we missing, which gaps are dangerous, and what is the smallest realistic team for a pitchable vertical slice?

**Short blurb:**
A practical skill for identifying missing roles, weak coverage, and the smallest workable team for a game concept.

---

### 0.75 game-dev-budget-estimator
**What it does:**
Helps a beginner or early-stage team estimate likely budget ranges for a game concept based on scope, team coverage, milestone, work model, and geography.

**Use it when:**
- someone asks how much a game like this might cost
- the concept, team, and milestone are known but the budget picture is fuzzy
- the team wants to understand what is already covered internally versus what still costs real money
- no team has been described yet and the user wants scenario-based budget ranges

**Best for:**
Beginner-friendly budget framing, cost-driver diagnosis, and rough milestone-based game cost estimation.

**Example prompt:**
> We want to make a pitchable mobile F2P action game. We have one programmer in Serbia and one freelance 2D artist in Poland working part-time. What budget range should we expect for a vertical slice, what costs are already covered, and what hidden costs are we probably missing?

**Short blurb:**
A practical skill for turning a game concept, team, and scope into a rough budget range with transparent assumptions and cost drivers.

---

### 0.8 game-dev-time-estimator
**What it does:**
Helps a beginner or early-stage team estimate likely development time ranges for a game concept based on scope, team coverage, milestone, availability, and production constraints.

**Use it when:**
- someone asks how long a game like this might take
- the concept, team, and milestone are known but the schedule picture is fuzzy
- the team wants to know whether a target date is realistic
- no team has been described yet and the user wants scenario-based timeline ranges

**Best for:**
Beginner-friendly schedule framing, time-driver diagnosis, and rough milestone-based development-time estimation.

**Example prompt:**
> We want to make a PC co-op survival prototype. We have one programmer full-time and one 3D artist part-time. How long would a prototype or vertical slice likely take, what will bottleneck us, and is 5 months realistic?

**Short blurb:**
A practical skill for turning a game concept, team, and scope into a rough development timeline with transparent assumptions and schedule risks.

---

### 0.9 game-design-fogg-behavior-audit
**What it does:**
Audits a game feature, flow, onboarding step, retention mechanic, or monetization prompt using the Fogg Behavior Model: Motivation, Ability, Prompt.

**Use it when:**
- a feature seems valuable on paper but players are not using it
- you want to diagnose whether a behavior is failing because of low motivation, low ability, or a bad prompt
- you need a focused audit of onboarding, event participation, reward claims, retention mechanics, or monetization nudges
- you want a practical feature-adoption critique instead of a broad design essay

**Best for:**
Behavior-focused feature audits, adoption diagnosis, and prompt/friction analysis.

**Example prompt:**
> Audit this daily event flow with the Fogg Behavior Model. The goal is to get players to enter the event once per day, but adoption is weak. Tell me whether motivation, ability, or prompt is the main bottleneck.

**Short blurb:**
A practical audit skill for diagnosing whether a feature actually drives the intended player behavior.

---

### 1. game-design-emotional-canvas
**What it does:**
Defines the emotional core, atmosphere, tone, and vibe of a game, feature, event, world area, or content theme.

**Use it when:**
- a concept feels emotionally vague
- you want a moodboard-ready emotional direction
- you need to clarify what players should feel
- art, audio, narrative, and design need emotional alignment

**Best for:**
High-level emotional identity work.

---

### 2. game-design-grow-design
**What it does:**
Applies the GROW model (Goal, Reality, Options, Will) to game design decision-making.

**Use it when:**
- a team is stuck in circular feature discussions
- a design problem needs more structure
- you need clearer tradeoffs and next steps
- a feature pitch is muddy and process-heavy thinking would help

**Best for:**
Structured feature and roadmap conversations.

---

### 3. game-design-player-motivation-audit
**What it does:**
Audits what kinds of motivation a game or feature creates using an SDT-inspired motivation spectrum.

**Use it when:**
- a system feels sticky but suspiciously hollow
- you want to understand whether behavior is driven by rewards, pressure, identity, or intrinsic fun
- you are reviewing live-ops, progression, battle passes, or social systems

**Best for:**
Diagnosing the motivational quality of engagement.

---

### 4. game-design-player-need-satisfaction-audit
**What it does:**
Audits whether a design satisfies or frustrates autonomy, competence, and relatedness.

**Use it when:**
- a feature retains players but may feel quietly depleting
- you want to understand whether the experience is psychologically nourishing
- onboarding, progression, or social systems feel flat or coercive

**Best for:**
Psychological need diagnosis and quality-of-experience audits.

---

### 5. game-design-unknown-unknowns-prototyping
**What it does:**
Maps uncertainty and helps decide what to prototype, in what order, and why.

**Use it when:**
- a concept seems promising but underdefined
- the team does not know what the real design question is yet
- a prototype risks becoming production theater instead of a learning tool

**Best for:**
Preproduction and uncertainty-driven prototyping.

---

## Beginner planning / first-step strategy

### 6. game-dev-first-steps
**What it does:**
Turns a rough game idea into a practical starting plan by asking about team size, skill mix, platform, scope, and first milestone, then recommending what to build first, what to postpone, and how to avoid early overscope.

**Use it when:**
- someone asks "how do I start making this?"
- a beginner needs help deciding what to build first
- a solo dev, duo, or small team needs a sane first milestone
- a concept should be reduced into a prototype or pitchable vertical slice plan

**Best for:**
Beginner-friendly scoping, build-order advice, and early production strategy.

---

## GROW-derived workflow family

These skills split the broader GROW-style decision process into smaller, sharper workflows.

### 6. game-design-goal-framing
**What it does:**
Turns a vague feature idea into a clear design goal with purpose, fit, success criteria, and constraints.

**Use it when:**
- a feature sounds fine but nobody can explain what it is really for
- success criteria are unclear
- the team is jumping into implementation too early

**Best for:**
Clarifying purpose before ideation or production.

---

### 7. game-design-option-generation
**What it does:**
Generates multiple credible solution paths before the team commits to one.

**Use it when:**
- one answer is dominating too early
- you want several plausible approaches with tradeoffs
- the solution space feels artificially narrow

**Best for:**
Expanding design options before prioritization.

---

### 8. game-design-five-options
**What it does:**
Forces explicit comparison across at least five candidate directions.

**Use it when:**
- there are already several ideas on the table
- the team needs structured comparison
- you want to avoid premature convergence

**Best for:**
Tactical option comparison.

---

### 9. game-design-roadblock-reframing
**What it does:**
Reframes a blocked design problem by isolating the obstacle, imagining it removed, and deriving workaround paths.

**Use it when:**
- the team keeps saying “we can’t because…”
- one blocker is dominating all thinking
- a feature feels trapped by a specific limitation

**Best for:**
Getting unstuck from design deadlock.

---

### 10. game-design-ideal-outcome-backcasting
**What it does:**
Starts from the ideal player-facing result and works backward to the conditions and steps needed to reach it.

**Use it when:**
- the end-state is easier to imagine than the path forward
- the team knows the destination vibe but not the design sequence
- you want to align a feature around a stronger final vision

**Best for:**
Vision-led design planning.

---

### 11. game-design-transformative-reuse
**What it does:**
Finds ways to adapt, recombine, extend, or retune existing systems instead of inventing from scratch.

**Use it when:**
- you want leverage over novelty
- live systems already exist and should be reused intelligently
- the team needs lower-risk innovation

**Best for:**
Production-aware feature design and reuse strategy.

---

### 12. game-design-feature-prioritization
**What it does:**
Compares options by impact, cost, fit, timing, and risk to decide what should happen now versus later.

**Use it when:**
- several candidate features compete for attention
- ideation is done and prioritization is needed
- roadmap discussions need a more explicit decision frame

**Best for:**
Choosing the strongest next move.

---

## Creative disruption

### 13. game-design-creative-unblocker
**What it does:**
Uses oblique prompts, sideways reframing, and playful provocations to break creative block.

**Use it when:**
- a feature feels stale
- discussions are looping
- every option feels equally dead
- the team needs strange but useful creative motion

**Best for:**
Creative detours and design unblock sessions.

---

## FTUE / onboarding

### 14. game-design-ftue-hero-journey-audit
**What it does:**
Audits FTUE and onboarding flows through the Hero’s Journey lens.

**Use it when:**
- the opening experience feels too tutorial-like and not emotionally engaging
- you want to audit call-to-adventure, mentor guidance, and threshold crossing
- you want a more narrative-emotional reading of onboarding quality

**Best for:**
FTUE, onboarding, and first-session retention review.

---

## Session structure / retention

### 15. game-design-goal-density-and-immediacy-audit
**What it does:**
Audits a game, feature, or metagame layer for goal density, goal immediacy, short/mid/long-term goal spread, safe session closure, and return triggers.

**Use it when:**
- players return and do not know what to do next
- a game feels aimless, overwhelming, or brittle across session lengths
- you want to evaluate how well the design fits fragmented player time
- you need a structured breakdown of short-term, mid-term, and long-term goals

**Best for:**
Session structure, return-player experience, and retention-oriented goal design.

---

## Publishing / pitch support

### 16. game-design-pitch-deck-audit
**What it does:**
Audits a game pitch deck for structure, clarity, persuasiveness, readability, business-case completeness, and publisher-fit.

**Use it when:**
- preparing a deck for publishers or funders
- checking whether the deck answers who / what / why / when / budget / opportunity
- polishing a deck before sending it asynchronously

**Best for:**
Pitch-deck review and publishing-readiness feedback.

---

### 17. design-red-team-audit
**What it does:**
Performs an adversarial design pre-mortem that assumes a feature, system, pitch, or roadmap idea fails, then identifies the most credible mechanisms of failure.

**Use it when:**
- a concept sounds persuasive on paper and you want to pressure-test it
- you want a hostile-but-constructive critique before production
- you need to expose weak assumptions, rollout risks, MVP traps, or misleading metrics

**Best for:**
Pre-mortems, risk exposure, and hard design challenge sessions.

---

### 18. game-design-prototyping-companion
**What it does:**
Tracks prototype branches, dead ends, parked ideas, and next experiments, and can support simple branch-map visualization workflows.

**Use it when:**
- a prototype creates multiple follow-up paths
- you want to preserve design learning across branches
- the team needs a structured record of what was tried, learned, chosen, or parked

**Best for:**
Prototype logging, branch tracking, and experiment continuity.

---

### 19. game-design-brainstorm-methods
**What it does:**
Applies named brainstorming methods such as SCAMPER, How Might We, Crazy 8s, Six Thinking Hats, Brainwriting 6-3-5, Worst Possible Idea, Lotus Blossom, forced connections, and morphological matrix to game design problems.

**Use it when:**
- the team wants method-driven ideation instead of generic brainstorming
- you need the right brainstorming framework for the problem
- you want ideation that ends in a shortlist or next move

**Best for:**
Structured ideation and facilitated brainstorming.

---

### 20. game-design-one-thing-to-remove
**What it does:**
Identifies the single highest-leverage thing to remove from a design in order to improve clarity, focus, pacing, emotional fit, or production sustainability.

**Use it when:**
- a feature feels bloated or overengineered
- a system has too much friction or redundant complexity
- you want a subtractive critique rather than another additive brainstorm

**Best for:**
Subtractive design audits and elegance-through-removal decisions.

---

### 21. game-design-novelty-spectrum-audit
**What it does:**
Evaluates a concept on the spectrum between too familiar and too novel using player expectations, mental models, and innovation pattern diagnosis.

**Use it when:**
- you want to know whether a concept is too derivative or too risky
- you need to assess familiarity anchors versus real novelty
- you want to classify innovation as incremental, recombinational, simplifying, or more radical

**Best for:**
Novelty positioning, concept differentiation, and expectation-risk analysis.

---

### 22. game-design-systematizing-empathizing-audit
**What it does:**
Positions a design on two axes — systematizing and empathizing — then infers likely player/persona appeal, likely rejection patterns, and the practical consequences of that positioning.

**Use it when:**
- you want to understand whether a design is logic-driven, emotionally player-attuned, or both
- you want to know what kind of player this design is really for
- you need a structural-emotional positioning read without assuming one quadrant is ideal

**Best for:**
Audience-fit diagnostics, structural-emotional positioning, and persona-oriented feature evaluation.

---

### 23. game-design-kpi-coverage-audit
**What it does:**
Audits whether a feature is being judged fairly by the KPI framework around it, especially when connective tissue, UX, QoL, enabling work, or sustainability value are being undervalued because they are hard to measure directly.

**Use it when:**
- a feature has obvious design value but weak direct KPI attribution
- the roadmap favors flashy self-contained systems over support work
- the team may be neglecting foundational improvements because they are hard to justify cleanly

**Best for:**
KPI blind-spot diagnosis, roadmap fairness, and support-feature justification.

---

### 24. game-design-prototype-intent-audit
**What it does:**
Audits whether a prototype is meant to sell the idea or reveal unknowns, and whether its scope actually matches that purpose.

**Use it when:**
- a prototype plan feels vague or contradictory
- the team may be building a demo while claiming it is for learning
- precious prototype time is being spent on the wrong questions

**Best for:**
Prototype strategy, prototype-scoping, and demo-vs-learning clarity.

---

### 25. game-design-player-segment-perception-audit
**What it does:**
Audits how different player segments are likely to perceive a feature, update, or content drop, especially when the feature is aimed at one cohort but visible to many others.

**Use it when:**
- a feature is targeted at elder or niche players but broadly marketed
- you want to know how new, mid, and elder players will read the same update differently
- you need to catch disappointment caused by visibility-access mismatch

**Best for:**
Segment targeting, feature rollout messaging, and cross-cohort perception analysis.

---

## Example prompt pack for the 4 game-dev skills

Use the same concept across all four skills to get a beginner-friendly planning stack from first steps -> team gaps -> budget -> timeline.

### 1. game-dev-first-steps
> I want to make a small PC creature-battler with light base-building and asynchronous trading. We are two people: one programmer and one 2D artist. What should we build first, what should we postpone, and what should our smallest believable prototype be?

### 2. game-dev-team-gap
> We want to make a small PC creature-battler with light base-building and asynchronous trading. We are two people: one programmer and one 2D artist. What roles or skills are we missing for a prototype and later for a vertical slice?

### 3. game-dev-budget-estimator
> We want to make a small PC creature-battler with light base-building and asynchronous trading. We are two people: one programmer and one 2D artist, both part-time in Eastern Europe. What rough budget should we expect for a prototype and for a vertical slice, and what costs are probably not covered by our team?

### 4. game-dev-time-estimator
> We want to make a small PC creature-battler with light base-building and asynchronous trading. We are two people: one programmer and one 2D artist, both part-time. How long would a prototype and a vertical slice likely take, what would bottleneck us, and is 6 months realistic for the vertical slice?

### Fast comparison pack

Use these when you want to test skill boundaries quickly.

- **First steps:** What should we build first?
- **Team gap:** Who are we missing?
- **Budget:** What will this likely cost?
- **Time:** How long will this likely take?

## How to use

### In OpenClaw
Place the skill folders in your workspace `skills/` directory.

### As packaged files
Use the `.skill` archives from `package-skills/` for sharing or installation.

## Notes

- Some skills are **audit skills** (diagnose what is true, weak, missing, or risky).
- Some skills are **workflow skills** (help move from ambiguity to action).
- Some intentionally overlap a bit; that is by design. Different framing lenses are useful in different conversations.

## Best starting points

If you are not sure where to begin:
- vague concept -> `game-design-goal-framing`
- no good options yet -> `game-design-option-generation`
- emotionally flat idea -> `game-design-emotional-canvas`
- suspicious engagement loop -> `game-design-player-motivation-audit`
- weak onboarding -> `game-design-ftue-hero-journey-audit`
- unclear session structure -> `game-design-goal-density-and-immediacy-audit`
- stale discussion -> `game-design-creative-unblocker`
- unclear prototype needs -> `game-design-unknown-unknowns-prototyping`
- upcoming publisher conversation -> `game-design-pitch-deck-audit`
- need structured brainstorming methods -> `game-design-brainstorm-methods`
- suspect the best improvement is subtraction -> `game-design-one-thing-to-remove`
- not sure if the concept is too familiar or too novel -> `game-design-novelty-spectrum-audit`
- want to understand who the design emotionally/structurally appeals to -> `game-design-systematizing-empathizing-audit`
- suspect the KPI framing is undervaluing connective tissue or QoL work -> `game-design-kpi-coverage-audit`
- unclear whether a prototype is for selling or learning -> `game-design-prototype-intent-audit`
- worried different player cohorts will read the same feature differently -> `game-design-player-segment-perception-audit`
