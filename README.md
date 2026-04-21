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
- as packaged `.skill` files from the `packaged-skills/` folder.

## Repository structure

- `game-design-*/` - individual skill folders
- `packaged-skills/` - packaged distributable `.skill` files
- `game-design-skill-catalog.md` - compact local catalog/index

## Skills

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

## Publishing / pitch support

### 15. game-design-pitch-deck-audit
**What it does:**
Audits a game pitch deck for structure, clarity, persuasiveness, readability, business-case completeness, and publisher-fit.

**Use it when:**
- preparing a deck for publishers or funders
- checking whether the deck answers who / what / why / when / budget / opportunity
- polishing a deck before sending it asynchronously

**Best for:**
Pitch-deck review and publishing-readiness feedback.

---

### 16. design-red-team-audit
**What it does:**
Performs an adversarial design pre-mortem that assumes a feature, system, pitch, or roadmap idea fails, then identifies the most credible mechanisms of failure.

**Use it when:**
- a concept sounds persuasive on paper and you want to pressure-test it
- you want a hostile-but-constructive critique before production
- you need to expose weak assumptions, rollout risks, MVP traps, or misleading metrics

**Best for:**
Pre-mortems, risk exposure, and hard design challenge sessions.

---

## How to use

### In OpenClaw
Place the skill folders in your workspace `skills/` directory.

### As packaged files
Use the `.skill` archives from `packaged-skills/` for sharing or installation.

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
- stale discussion -> `game-design-creative-unblocker`
- unclear prototype needs -> `game-design-unknown-unknowns-prototyping`
- upcoming publisher conversation -> `game-design-pitch-deck-audit`
