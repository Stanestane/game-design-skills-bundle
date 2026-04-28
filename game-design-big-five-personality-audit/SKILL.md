---
name: game-design-big-five-personality-audit
description: "Audit a game, feature, progression system, social system, live-ops loop, onboarding flow, monetization surface, or multiplayer space through the lens of the Big Five personality traits (OCEAN): Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Use when evaluating which personality-style preferences a design feels comfortable for, which kinds of players it energizes or exhausts, how much structure, novelty, social intensity, conflict, or emotional pressure it creates, or when you need a personality-fit lens that is different from archetype or motivation-segment frameworks."
---

# Game Design Big Five Personality Audit

Audit a design by asking which OCEAN trait expressions it feels comfortable for, rewards, strains, or quietly repels.

Use this skill to evaluate how a game, feature, flow, or system fits different **personality-style preferences** using the Big Five: **Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism**.

Treat these as **fit lenses**, not diagnostic labels.

## Core principle

This is not about pretending a game can be reverse-engineered into a clinical personality test.

The useful question is simpler:
- what kind of novelty appetite does this design reward?
- what kind of structure tolerance does it demand?
- what level of social intensity does it assume?
- how cooperative or adversarial does it feel?
- how emotionally rough, stressful, or safe is it?

Those questions map surprisingly well onto OCEAN-style differences.

## Start with the reference notes

Before auditing, read `references/big-five-notes.md`.

That file contains the trait summaries, game-design interpretation rules, and anti-pattern warnings for using OCEAN responsibly.

## What to produce

Generate:
1. **Audit target** - what is being reviewed and what it is supposed to do
2. **Trait-fit readout** - how the design lands for each Big Five trait dimension
3. **Comfort and strain profile** - who is likely to feel naturally at home versus overloaded or alienated
4. **Cross-trait tensions** - where serving one trait expression harms another
5. **Design implications** - what the design is really asking players to tolerate or enjoy
6. **Recommendations** - what to strengthen, soften, separate, or clarify

## Process

### 1. Define the audit target
Clarify:
- what is being audited
- what role it plays in the product
- whether it is core, optional, onboarding, progression, monetization, social, competitive, or endgame
- whether the design needs broad accessibility or can be narrow and demanding

Write:
- **Design being audited**
- **Intended job**
- **Scope**
- **Breadth requirement**

### 2. Audit for Openness
Treat this as the novelty, curiosity, ambiguity, and imagination lens.

Ask:
- Does the design reward curiosity, experimentation, or unusual combinations?
- Is there room for self-expression, aesthetic appreciation, or discovery?
- Does it support multiple paths, interpretations, or play styles?
- Does it punish deviation from the obvious route?
- Is novelty meaningful, or just noisy and confusing?

Look for:
- discovery
- emergent interactions
- expressive customization
- aesthetic richness
- non-obvious strategies
- mystery and experimentation

Interpretation:
- **High-openness fit** usually means the design feels rich, curious, and rewarding to explore
- **Lower-openness fit** usually means the design is more familiar, explicit, stable, and convention-friendly

### 3. Audit for Conscientiousness
Treat this as the structure, planning, discipline, and completion lens.

Ask:
- Does the design reward planning, consistency, optimization, and order?
- Are goals, tasks, and systems legible enough to support disciplined play?
- Does the design create satisfying structure or oppressive maintenance burden?
- Are checklists and routines rewarding or exhausting?
- How much does the experience punish inconsistency or sloppy play?

Look for:
- routine loops
- optimization pressure
- collection/completion structures
- schedules and timers
- ordered progression
- maintenance burden

Interpretation:
- **High-conscientiousness fit** often means the design rewards planning and follow-through
- **Lower-conscientiousness fit** often means the design is more improvisational, loose, forgiving, or anti-obligation

### 4. Audit for Extraversion
Treat this as the social intensity, energy, visibility, and stimulation lens.

Ask:
- Does the design come alive around other people?
- Does it reward visibility, talkativeness, presence, or leadership?
- Is there a lot of social energy, noise, or activity?
- Does it over-demand participation from players who would rather engage quietly or solo?
- Can introversion-style players engage meaningfully without feeling socially crowded?

Look for:
- multiplayer dependence
- group rituals
- chat and voice usage
- social visibility
- team roles
- high-arousal action

Interpretation:
- **High-extraversion fit** often means lively, visible, socially energizing play
- **Lower-extraversion fit** often means quieter autonomy, optional social contact, or asynchronous sociality

### 5. Audit for Agreeableness
Treat this as the cooperation, trust, harmony, and interpersonal harshness lens.

Ask:
- Does the design reward helping, cooperation, support, or prosocial behavior?
- Does it create conflict, betrayal, humiliation, or harsh comparison?
- How safe does social interaction feel?
- Does the design assume players enjoy adversarial pressure?
- Are players encouraged to care for others, or to exploit them?

Look for:
- co-op
- gifting/helping
- supportive roles
- trust structures
- betrayal mechanics
- griefing potential
- dominance incentives

Interpretation:
- **High-agreeableness fit** often means warm, cooperative, low-cruelty design
- **Lower-agreeableness fit** may mean sharper rivalry, cutthroat play, or socially aggressive energy

### 6. Audit for Neuroticism
Treat this as the stress sensitivity, punishment tolerance, and emotional volatility lens.

Ask:
- How punishing, humiliating, uncertain, or stressful is the design?
- How much loss aversion, FOMO, or social evaluation pressure does it create?
- Are mistakes recoverable?
- Does failure teach calmly or slap the player emotionally?
- Does the design offer safety, reassurance, clarity, or soothing routines where needed?

Look for:
- punishment severity
- scarcity anxiety
- public failure exposure
- opaque systems
- recovery speed
- emotional safety nets
- comfort-loop potential

Interpretation:
- **Higher-neuroticism fit** usually requires more reassurance, predictability, and survivable failure
- **Lower-neuroticism fit** can tolerate harsher setbacks, ambiguity, and pressure without emotional collapse

### 7. Build the trait-fit profile
For each trait dimension, describe:
- who is more comfortable
- who is more strained
- what exact design property causes that fit or strain

Use this format:

| Trait | High-expression fit | Low-expression fit | Main evidence | Main risk |
|---|---|---|---|---|
| Openness | ... | ... | ... | ... |
| Conscientiousness | ... | ... | ... | ... |
| Extraversion | ... | ... | ... | ... |
| Agreeableness | ... | ... | ... | ... |
| Neuroticism | ... | ... | ... | ... |

### 8. Identify cross-trait tensions
Look for cases where serving one trait expression harms another.

Common tensions:
- **Novelty vs clarity** - openness-serving depth creates confusion for lower-openness players
- **Structure vs freedom** - conscientiousness-serving order suffocates players who want looser improvisation
- **Social energy vs quiet autonomy** - extraversion-serving visibility crowds lower-extraversion players
- **Competition vs harmony** - lower-agreeableness conflict energy poisons high-agreeableness comfort
- **Pressure vs safety** - low-neuroticism challenge intensity crushes high-neuroticism players

Ask:
- Which tension is intentional?
- Which tension is accidental?
- Does the feature need to choose a side, or should it separate modes more cleanly?

### 9. Convert the audit into design implications
Translate findings into practical design language.

Examples:
- if the design strongly favors high conscientiousness, ask whether maintenance burden is too high for broader audiences
- if the design strongly favors high openness, ask whether onboarding gives enough grounding for less exploratory players
- if the design strongly favors extraversion, ask whether solo or asynchronous alternatives exist
- if the design strongly favors low agreeableness, ask whether toxicity or social cruelty is becoming part of the product identity
- if the design strongly disfavors higher neuroticism, ask whether failure, ranking, or FOMO pressure is harsher than necessary

### 10. Recommend changes
For each major issue, specify:
- **Trait dimension affected**
- **Current issue**
- **Design cause**
- **Suggested change**
- **Expected effect**

Prefer recommendations that:
- preserve the intended audience
- reduce accidental exclusion
- separate incompatible needs when one system cannot serve both
- make emotional cost visible instead of pretending the design is universally comfortable

## Response structure

### Audit Target
- ...

### OCEAN Readout
- Openness: ...
- Conscientiousness: ...
- Extraversion: ...
- Agreeableness: ...
- Neuroticism: ...

### Trait-Fit Profile
- ...

### Cross-Trait Tensions
- ...

### Design Implications
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode
- What kind of novelty appetite does this design assume?
- How much structure and maintenance burden does it demand?
- How socially loud is it?
- How cooperative versus adversarial is it?
- How emotionally harsh or safe is it?
- Which trait expression is most strongly favored?
- Which trait expression is most likely to bounce?

## Working principle

Some games fail not because they are bad, but because they quietly assume the wrong kind of person will enjoy their pressure, noise, ambiguity, or obligations.

Use OCEAN to make those assumptions visible.
