---
name: game-design-perceived-randomness-audit
description: Audit a game feature, combat system, loot table, reward loop, procedural system, chance mechanic, or uncertainty-driven design by how players are likely to perceive its randomness. Use when you need to evaluate whether a system will feel fair, streaky, rigged, sabotaging, manipulable, or skill-undermining; when players may misread independent events as patterned; or when randomness may sit too close to player action and create frustration. Analyze expectation gaps, gambler's-fallacy-style reactions, hidden pattern-seeking, input-versus-output randomness, perceived fairness, exploit risk, and ways to reshape presentation or mechanics.
---

# Game Design Perceived Randomness Audit

Audit not just the math of randomness, but the psychology of how players will read it.

Use this skill when the core question is not only "is this random system balanced?" but also "what story will players tell themselves about this randomness?" The goal is to catch places where independent events will be perceived as rigged patterns, where streaks will feel malicious, where uncertainty undermines competence, or where the game could use presentation or structure to make randomness feel fairer and more legible.

Read `references/perception-patterns.md` when you need the key psychology behind randomness perception.
Read `references/audit-checklist.md` when you need a compact checklist of design risks and mitigation levers.

## Core behavior

- Keep the analysis practical, not statistical-for-its-own-sake.
- Audit player perception, not only formal probability.
- Distinguish actual randomness from perceived randomness.
- Identify where players will imagine patterns, sabotage, or "the game knows what I need and withholds it" behavior.
- Check whether randomness happens before the decision or between the decision and the outcome.
- Treat randomness that interferes directly with player action as more dangerous than randomness that shapes the environment.
- Look for streak pain, expectation mismatch, control illusions, and competence damage.
- Recommend concrete fixes in system design, UX, communication, and presentation.

## What to ask first

Prioritize these questions:
1. What is the feature or random system?
2. What outcomes are random?
3. What does the player know before acting, and what is hidden until after acting?
4. What player action is this randomness attached to?
5. What does the player usually want in the moment when the random outcome occurs?
6. How often does the randomness happen, and how visible are streaks?
7. Is the system meant to feel exciting, fair, learnable, punishing, suspenseful, or skill-testing?
8. Are there safeguards, pity rules, weighted drops, rerolls, previews, or player-choice layers already present?

If information is missing, infer cautiously and state the assumption.

## What to diagnose

Quickly identify:
- whether the player is likely to assume hidden patterns in independent outcomes
- whether gambler's-fallacy-style expectations will make the system feel unfair after streaks
- whether players will expect conditional fairness such as "I have not gotten X lately so I should get it soon"
- whether randomness is input randomness, output randomness, or an unhealthy blur of both
- whether the system damages the feeling of competence by making deliberate actions resolve unpredictably
- whether players can meaningfully react to uncertainty using skill
- whether the presentation helps players understand the randomness or makes it feel rigged
- whether the mitigation method creates exploit risk or false promises

## Response structure

Always organize the answer using this structure.

### System Read
- describe the random system in plain language
- state what is actually random and what is not

### Player Expectation Read
- explain what players are likely to expect from the system
- identify likely mistaken assumptions about balance, streak correction, fairness, or hidden intent

### Perceived Fairness Risk
- explain when the system is likely to feel fair, unfair, rigged, streaky, or malicious
- highlight the most likely frustration story players will tell themselves

### Randomness Placement
- identify whether this is mostly input randomness or output randomness
- explain whether randomness happens before the player chooses or after the player commits
- say whether that placement supports or undermines skill expression

### Competence and Agency Read
- explain whether players can adapt to the uncertainty with skill
- identify where randomness is likely to invalidate intentional play
- note whether the system feels like a challenge to respond to or a sabotage of action

### Risk Diagnosis
- give the top 2 to 5 perception risks
- include streak pain, hidden-intent suspicion, exploitability, or expectation mismatch where relevant

### Recommendation
- recommend specific design, UX, or messaging changes
- separate must-fix from optional polish when useful

## Common risk patterns

Raise these when relevant:
- truly independent drops being perceived as "due"
- players believing the game withholds exactly what they currently need
- random combat resolution making skillful decisions feel invalidated
- pity systems that help fairness but become exploitable if too legible
- procedural/input randomness producing wildly different challenge levels with too little response time
- opaque weighting creating conspiracy theories
- visible streaks without framing, smoothing, or counterweights
- systems that are mathematically fair over long runs but emotionally awful in short runs

## Useful mitigation levers

Only recommend what fits the design intent.

- move randomness earlier so the player reacts to it rather than being blindsided by it
- reduce output randomness on high-stakes actions
- add soft streak smoothing or pity protection
- batch outcomes into more even distributions when fairness matters more than pure entropy
- provide player choice among random options
- expose clearer odds or stronger telegraphing
- separate excitement randomness from core skill resolution
- use presentation to give the player a clearer sense of authorship or controlled reveal
- shift reward pools by context carefully, while watching for exploit loops

## Strong use cases

This skill is especially useful for:
- loot drops and chest rewards
- gacha, pity, and streak-protection systems
- crit chance, hit chance, dodge, and proc systems
- random combat resolution
- procedural encounter or room generation
- event reward pools
- roguelike runs with variable offer quality
- randomness-heavy retention loops
- any design where players say the system feels rigged

## Weaker use cases

This skill is less useful for:
- systems with no meaningful uncertainty
- purely economic balance review without a perception question
- broad game critique where randomness is not a major issue

## Style guidance

- Be concrete.
- Do not hide behind statistics if the player-facing feeling is bad.
- Do not assume mathematically fair means experientially fair.
- If a system is perception-safe even though players may still complain sometimes, say that too.
- If the right fix is presentation rather than probability tuning, say so.
- If the right fix is to remove randomness from a player action entirely, say so directly.

## Fast mode

Use this compressed flow when the user wants a quick answer:
- what is random here
- what will players assume about that randomness
- will it feel fair or rigged
- is the randomness before or after player choice
- does it support skill or sabotage action
- what should change first

## Working principle

Players do not experience randomness as raw probability tables. They experience it as felt fairness, perceived intent, streak memory, and the degree to which their choices still seem to matter.
