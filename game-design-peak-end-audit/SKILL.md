---
name: game-design-peak-end-audit
description: Audit a game, feature, session, level, event, onboarding flow, reward sequence, or return-player experience through the lens of the peak-end rule. Use when evaluating which moments players are most likely to remember, whether the emotional high points are strong enough, whether endings, exits, and completions leave the right aftertaste, or why an experience with decent average quality is still remembered as flat, frustrating, or unexpectedly great.
---

# Game Design Peak-End Audit

Audit a design by asking which moments dominate memory and whether the experience earns the memory it leaves behind.

Use this skill when the important question is not just how the experience feels moment to moment, but how players will remember it afterward. The goal is to identify the emotional peaks, the ending shape, and the aftertaste that determine whether a session, level, feature, event, or sequence is remembered as exciting, exhausting, disappointing, triumphant, or forgettable.

Read `references/family-conventions.md` when you want the shared style, prioritization, and diagnosis rules for this game-design skill family.
Read `references/output-patterns.md` when you want the preferred recommendation and minimal-fix structure.

## Core principle

Players do not remember an experience as an average of every second they lived through.

They disproportionately remember:
- the strongest emotional peaks
- the ending
- the story those moments imply afterward

That means a design with decent average quality can still be remembered badly if:
- its emotional peaks are weak
- its worst spike dominates memory
- its ending sours the whole experience

And a rougher experience can still land well if:
- its peak is strong and meaningful
- its ending resolves cleanly
- the memory closes with satisfaction, momentum, relief, or anticipation

## What to produce

Generate:
1. **Peak-end profile** - the strongest peaks, the ending shape, and the likely remembered summary
2. **Memory dominance diagnosis** - which moments will overshadow the rest of the experience
3. **Ending-quality diagnosis** - whether the closing moments strengthen or poison the memory
4. **Experience-shape risks** - where the design is setting itself up to be remembered for the wrong thing
5. **Design actions** - what to amplify, soften, reorder, frame, or close differently

## Process

### 1. Define the audit target
Clarify:
- what exact experience slice is being audited
- where it begins and ends from the player's point of view
- what player segment matters most

Write:
- **Audit target**
- **Experience window**
- **Primary player segment**

### 2. Map the emotional shape over time
Break the experience into phases and ask:
- where does emotional intensity rise?
- where does it sag?
- where does frustration spike?
- where does satisfaction spike?
- what is the final emotional note?

Do not settle for generic labels like "good pacing." Name the moments.

### 3. Identify positive and negative peaks
Look for the moments most likely to become the remembered highlight or remembered wound.

Examples:
- first big win
- dramatic comeback
- painful difficulty spike
- surprising reveal
- humiliating loss
- beautiful payoff moment
- reward opening high
- last-minute collapse

For each peak, ask:
- how intense is it?
- how clear is it?
- does it support the intended fantasy?
- is it the thing you actually want remembered?

### 4. Audit the ending
The ending may be:
- session close
- boss resolution
- reward-claim sequence
- level completion
- event wrap-up
- return-to-hub state
- defeat screen and immediate aftermath

Ask:
- what emotion does the player leave with?
- does the ending frame the previous experience positively or negatively?
- does it create closure, momentum, relief, excitement, emptiness, or irritation?
- does it respect the effort that preceded it?

### 5. Determine the likely remembered story
Translate the shape into the sentence the player is likely to remember later.

Examples:
- "That run had one incredible clutch ending"
- "The fight was fine, but the ending reward felt pathetic"
- "That event was mostly chores and then it just sort of stopped"
- "The level was hard, but the payoff made it worth it"

If the remembered sentence is bad, average quality elsewhere may not save the experience.

### 6. Diagnose peak-end failure patterns
Look for:
- strong negative spike dominating weak positives
- flat experience with no memorable high
- rewarding middle but deflating ending
- emotionally strong ending attached to a fantasy mismatch
- punishing final note after meaningful progress
- reward ceremony too weak for the effort invested
- admin or UI sludge contaminating the exit

### 7. Check segment differences
Ask whether:
- new players experience the worst peak where veterans experience the best one
- one audience sees relief while another sees boredom
- the ending hits differently depending on skill, investment, or outcome state

### 8. Convert findings into design changes
For each issue, specify:
- **Peak-end problem**
- **Why it will dominate memory**
- **Suggested change**
- **Expected effect on remembered experience**

Examples:
- strengthen the success payoff -> improves remembered value of the whole sequence
- remove admin friction at the end -> prevents sour aftertaste
- soften one brutal late spike -> stops the whole feature being remembered as hostile
- reorder the reward reveal -> lets the ending carry more emotional weight

## Response structure

Use this structure unless the user asks for something else:

### Audit Target
- ...

### Peak-End Profile
- ...

### Positive Peaks
- ...

### Negative Peaks
- ...

### Ending Quality
- ...

### Likely Remembered Story
- ...

### Recommendations
1. ...
2. ...
3. ...

### Minimal Fix
- ...

## Fast mode

Use this quick pass when speed matters:
- What is the strongest moment?
- What is the worst moment?
- What is the final emotional note?
- Which of those will dominate memory?
- What one change would most improve the remembered aftertaste?

## Usage notes

This audit is especially useful for:
- onboarding and first-session retention
- boss fights and level endings
- event wrap-ups
- reward ceremonies and chest openings
- return-player flows
- session exits and stop points
- defeat aftermaths
- premium or high-effort experiences where memory quality really matters

Common patterns to watch for:
- many systems are fine in aggregate but remembered badly because the ending is weak
- a single ugly late frustration spike can poison an otherwise decent feature
- reward structure often over-focuses on average yield and under-focuses on emotional ending quality
- if the strongest remembered moment is the wrong one, the design has a memory-shape problem
- closure and anticipation are both valid endings, but aimlessness is not

## Working principle

The experience players remember is often not the one designers think they shipped.

Use this skill to identify which moments actually own the memory and whether that memory helps or hurts the design.