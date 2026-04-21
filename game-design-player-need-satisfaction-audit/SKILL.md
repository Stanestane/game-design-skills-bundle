---
name: game-design-player-need-satisfaction-audit
description: Audit a game, feature, live-ops system, onboarding flow, progression loop, social feature, monetization flow, or return loop for player need satisfaction using Self-Determination Theory and the PENS lens. Use when evaluating whether a design is actually fun beyond surface KPIs, diagnosing weak retention or shallow engagement, comparing variants, identifying where a system denies autonomy, competence, or relatedness, or understanding whether a game feels emotionally nourishing or quietly depleting.
---

# Game Design Player Need Satisfaction Audit

Audit a design by asking whether it satisfies core psychological needs rather than merely driving activity.

Use this skill to examine whether a game, feature, or live-ops system supports autonomy, competence, and relatedness, and where it may be denying those needs instead. Keep the analysis practical and design-facing. Treat fun as need satisfaction rather than as a vague entertainment label.

## Core principle

People do not play games only because they are interactive or rewarding. They play because games satisfy core psychological needs. A feature can have solid metrics, clean progression, and monetization hooks, yet still feel emotionally weak if it fails to satisfy these needs.

## Need lenses

### 1. Autonomy
The need to feel like a causal agent of one's own actions.

In game terms: meaningful choice, ownership, self-directed action, strategic freedom, and perceived control.

### 2. Competence
The need to feel effective, capable, and progressively more skillful.

In game terms: clear goals, understandable feedback, mastery, successful execution, improvement, and meaningful progress.

### 3. Relatedness
The need to feel socially connected, embedded, recognized, compared, valued, or bonded with others.

In game terms: cooperation, rivalry, status visibility, shared progress, belonging, social ritual, and social meaning.

### 4. Benevolence (optional)
Use this supplementary lens when the design includes helping, gifting, nurturing, stewardship, caretaking, or contribution to others.

## What to produce

Generate an audit with these outputs:

1. **Need satisfaction profile** - how strongly the design satisfies autonomy, competence, and relatedness
2. **Need denial profile** - where the design frustrates or blocks those needs
3. **Mechanism map** - which systems create or reduce satisfaction
4. **Risk diagnosis** - where the design is emotionally hollow, coercive, or overly one-dimensional
5. **Improvement recommendations** - targeted design changes to improve need satisfaction

## Process

### 1. Define the audit target

Clarify exactly what is being audited.

Possible targets:
- full game
- core loop
- new feature
- onboarding
- event structure
- social system
- monetization flow
- return loop
- session opener

Write:
- **Audit target**
- **Player context**
- **Why this audit matters**

### 2. Map intended player experience

Describe what the design is supposed to make the player feel and do.

This step prevents theory from floating free of the actual experience.

Ask:
- What is the intended player fantasy?
- What actions define the loop?
- What are players choosing?
- What are they trying to master?
- Where are they encountering other people, directly or indirectly?
- What does success look like from the player's perspective?

Write:
- **Intended player experience**
- **Core actions**
- **Sources of progress**
- **Sources of social meaning**

### 3. Audit autonomy

Ask whether the design helps the player feel like an active agent rather than a passenger.

Signs of autonomy satisfaction:
- meaningful choices, not fake choices
- multiple valid paths or priorities
- flexible pacing or self-directed goals
- player expression of preference or playstyle
- guidance that supports choice rather than replacing it
- actions that feel intentional and consequential
- constraints that are understandable rather than arbitrary

Signs of autonomy denial:
- overly forced funnels
- constant interruption or coercion
- fake choice with one obviously correct option
- rigid pacing with little ownership
- recommendation systems that feel bossy
- decisions that do not materially matter
- excessive timers or blockers with no agency-preserving response

Ask:
- What meaningful choices does the player make?
- Can the player set their own short-term priorities?
- Does guidance preserve agency or replace it?
- Are there multiple viable ways to progress?
- Does the player feel ownership over success?
- Where does the system make the player feel trapped, railroaded, or manipulated?

Use this format:

| Autonomy Dimension | Evidence of Satisfaction | Evidence of Denial | Severity |
|---|---|---|---|

### 4. Audit competence

Ask whether the design helps the player feel effective, improving, and capable.

Signs of competence satisfaction:
- clear goals and immediate feedback
- understandable cause and effect
- actions produce visible results
- progression is legible
- player skill or understanding improves outcomes
- challenge is meaningful but not chaotic
- the system teaches without humiliating

Signs of competence denial:
- noisy or ambiguous feedback
- success feels random or disconnected from decisions
- actions fail for opaque reasons
- no sense of improvement or mastery
- friction overwhelms learning
- players cannot tell what good play looks like
- systems produce repeated confusion, blocked states, or dead-end effort

Ask:
- Does the player understand what they are trying to achieve?
- Is the result of action legible and satisfying?
- Can the player improve through practice, strategy, or understanding?
- Is there a clear bridge between effort and result?
- Are failure states fair and interpretable?
- Where does the design create frustration without learning?

Use this format:

| Competence Dimension | Evidence of Satisfaction | Evidence of Denial | Severity |
|---|---|---|---|

### 5. Audit relatedness

Ask whether the design makes the player feel socially connected, situated, or recognized.

Signs of relatedness satisfaction:
- meaningful club, guild, or social systems
- visible social comparison that feels motivating
- cooperation, gifting, helping, or mutual dependency
- rituals of return and shared participation
- recognition, identity, or status within a group
- ambient social presence, even if asynchronous
- emotional connection to characters, community, or shared world

Signs of relatedness denial:
- social systems are present but emotionally empty
- comparison is punishing rather than connective
- other players feel like abstract obstacles only
- no sense of belonging or shared culture
- social actions are transactional with no felt relationship
- players feel isolated even inside a nominally social feature

Ask:
- How does this design help the player feel part of a larger social matrix?
- What forms of recognition or comparison exist?
- Is there cooperation, competition, shared identity, or belonging?
- Are social features emotionally meaningful or just functional?
- Does the design create connection or merely visibility?
- Where does the feature feel socially sterile?

Use this format:

| Relatedness Dimension | Evidence of Satisfaction | Evidence of Denial | Severity |
|---|---|---|---|

### 6. Audit benevolence or contribution when relevant

Use this supplementary lens when the design lets players feel good by helping, nurturing, protecting, or contributing.

Relevant cases include:
- city care
- co-op support
- gifting
- club contribution
- stewardship systems
- pet or resident care
- restoration or rebuilding fantasies

Ask:
- Can the player improve something beyond themselves?
- Can they care for, help, or contribute to others?
- Does contribution feel meaningful or cosmetic?
- Is there emotional payoff in generosity or stewardship?

### 7. Build the need satisfaction profile

Summarize the overall shape of the experience.

Score each need from 1 to 5:
- **1** = strongly denied
- **2** = weak or inconsistent
- **3** = moderate
- **4** = strong
- **5** = central strength

Use this format:

| Need | Score | Why |
|---|---:|---|
| Autonomy | 1-5 | ... |
| Competence | 1-5 | ... |
| Relatedness | 1-5 | ... |
| Benevolence (optional) | 1-5 | ... |

Interpretation patterns:
- high autonomy, low competence -> expressive but confusing
- high competence, low autonomy -> polished but controlling
- high relatedness, low autonomy -> socially sticky but personally shallow
- high competence, low relatedness -> satisfying alone, weak community pull
- balanced strength across all three -> strongest candidate for durable engagement

### 8. Diagnose need denial and imbalance

Identify what is missing, what is overrepresented, and what failure shape is emerging.

Common failure shapes:

#### A. Spreadsheet fun
- competence signals are present
- autonomy is weak
- relatedness is weak
- the system is efficient but emotionally dry

#### B. Coercive retention
- progression exists
- constant nudging and timers deny autonomy
- competence is undermined by blockers
- players return from obligation rather than desire

#### C. Social shell
- clubs or leaderboards exist
- relatedness cues are visible but shallow
- there is little real belonging or identity

#### D. Pleasant but empty
- autonomy is present
- low challenge or poor feedback reduces competence
- interaction lacks a meaningful arc

#### E. High-pressure optimization trap
- competence exists for experts only
- autonomy narrows into one dominant strategy
- social comparison becomes discouraging

### 9. Convert findings into design actions

For each issue, specify:
- **Need affected**
- **Current problem**
- **Design cause**
- **Suggested change**
- **Expected emotional effect**

Examples:
- add more player-selectable priorities -> increases autonomy
- clarify action-result feedback -> increases competence
- add visible club contribution loops -> increases relatedness
- reduce forced interruptions -> reduces autonomy denial
- add progression bridges between systems -> strengthens competence and autonomy together

Use this format:

| Need | Problem | Suggested Change | Expected Effect |
|---|---|---|---|

### 10. Reuse the audit over time

Run this audit:
- during concepting
- after prototype reviews
- before greenlight
- after live launch
- when retention or sentiment drops
- when comparing AB variants

Do not treat this as a one-off theory exercise. It is most useful when repeatedly applied to major game systems.

## Response structure

Use this structure unless the user asks for something else:

### Audit Target
- ...

### Intended Player Experience
- ...

### Autonomy
- Strengths: ...
- Weaknesses: ...

### Competence
- Strengths: ...
- Weaknesses: ...

### Relatedness
- Strengths: ...
- Weaknesses: ...

### Need Satisfaction Profile
- Autonomy: ...
- Competence: ...
- Relatedness: ...

### Risk Diagnosis
- ...

### Recommendations
1. ...
2. ...
3. ...

## Fast mode

Use this quick pass when speed matters:
- Where does the player experience meaningful choice?
- Where do they feel effective and improving?
- Where do they feel connected to others?
- Where does the design deny one of those needs?
- Which need is strongest, and which is weakest?
- What one change would most improve the weakest need?

## Usage notes

This audit is especially useful for:
- session opener flows
- city request systems
- season passes and event track progression
- club systems and wars
- trains and deliveries
- city-building fantasy versus optimization friction
- monetization touchpoints that may erode autonomy
- guidance systems that may help competence while harming autonomy

Common patterns to watch for:
- too much instruction can improve competence but reduce autonomy
- timers and blockers can motivate return but also create autonomy denial
- social systems can create relatedness cues without true belonging
- event layers can create progress but overload competence if feedback is fragmented

## Working principle

A successful game does not merely retain players. It repeatedly satisfies core psychological needs.

Use this skill when a design is performing mechanically but you need to understand whether it is emotionally nourishing or quietly depleting.