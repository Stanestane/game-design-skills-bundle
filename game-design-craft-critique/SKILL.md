---
name: game-design-craft-critique
description: Critically analyze an existing, shipped, third-party or competitor game for craft lessons, using a layered method (adapted from Raph Koster's "How I Analyze a Game") that separates a game's systems from its surface experience, guesses the intent behind each layer, and checks whether those intents actually line up. Use this whenever the user wants to study a released game, competitor title, or reference game in depth -- not just describe it, but understand why it's built the way it is and what to steal from it. Trigger on requests like "analyze [game]", "break down how [game] works", "what can we learn from [game]", "why does [game] feel so good/bad", or "study this competitor game." This is a game-study tool aimed at OTHER people's games, distinct from the feature-pitch and own-design audits elsewhere in this bundle -- though it also works as a systems-vs-experience alignment gut check on your own game once both layers exist enough to compare.
---

# Craft Critique (Koster Method)

Most game criticism only touches one layer: is it fun, does the story work, is the
combat satisfying. This method deliberately separates the layers first and compares
them at the end, because the most useful craft lessons live in whether the layers
agree with each other, not in any one layer alone. A game can have a hollow mismatch
between big narrative ambition and a shallow, generic system underneath it, or the
opposite: mechanically ambitious work wrapped in thin, forgettable flavor text.
Neither is visible if you only look at one layer.

Read the whole workflow before starting — the order matters. Set aside personal
enjoyment of the game until the final step; judging fun early contaminates every
layer that follows with a feeling you haven't yet traced back to its source.

## When this is (and isn't) the right tool

This is for studying a specific existing, playable game — released, in early access,
or at minimum a public demo/trailer with enough detail to reason about. It is not for
auditing the user's own in-development pitch or feature spec against a psychological
framework — for that, point to the narrower audits in this bundle instead (Fogg,
Bartle, flow, fairness, etc.), which this skill can also call on as sub-tools (see
Step 2 and Step 5).

If the user names a game but gives no real detail about it, gather what you actually
know or can find (mechanics, systems, structure) before analyzing — don't fabricate
specifics about a game you don't have grounded information on.

## Workflow

### 1. Strip the game to its skeleton

Before anything else, set aside the fiction and the feeling. Describe the actual
moment-to-moment loop in the driest possible terms — what button does what, what
piece moves where, what the player is literally doing with their hands, with all
narrative wrapper removed. A stealth-horror game might turn out to be, underneath,
a resource-management puzzle about noise budgets. A found-footage walking sim might
turn out to be a search-and-inventory game about flipping objects over.

This is a deliberately reductive move, not a value judgment — the point is to see
the mechanic clearly before the fiction's charisma colors your read of it.

### 2. Read the systems

With the skeleton exposed, look at what the systems actually allow:

- What's the possibility space — how many meaningfully different ways can a player
  move through this system, and how much does that space open up over time?
- What choices carry real consequence, versus choices that are cosmetic?
- Can the system be exploited or solved in a way that breaks its intended tension?
- Does player skill matter, and if so, at what — reaction time, planning, pattern
  recognition, resource math?
- Does the system teach the player anything as they go, building a mental model that
  pays off later, or does it stay flat?

If this game is central enough to the user's own work to be worth the extra rigor,
this step can call on `game-design-core-loop-extractor` to pull out the actual
repeated action/feedback/reward loop formally, rather than eyeballing it here.

### 3. Guess what the systems are *for*

Ask what the designer was likely trying to accomplish at this systemic level — and
treat it explicitly as a guess, stated with your reasoning, not a claim of certainty.
Most systems are built around one or more of a small set of common goals:

- keeping the player playing (retention mechanics, session hooks)
- getting the player to pay (monetization surfaces, friction that sells relief)
- keeping the player's attention on the fictional experience rather than the
  mechanical one (the system recedes so the story/world can carry the moment)
- making the player feel powerful

These four are common and not a knock against a game — plenty of great games do
only these, well. It's worth explicitly noting when a system reaches for something
rarer and more interesting: making players want to help each other, making players
suspicious of the rules as written, teaching a genuinely new way of thinking about a
category of problem, or rewarding things other than power — creativity, cooperation,
cleverness, restraint.

Say what signals led to the guess (what the system rewards, what it punishes, what
it makes frequent versus rare) rather than asserting intent as fact.

### 4. Judge the feel, separately from the fiction

Now assess how the player touches the system and how it touches back: input
responsiveness, control feel, feedback clarity, whether reward signals are legible,
whether the game teaches its own controls and systems well or assumes prior
knowledge. Stay close to "game feel" territory here — this is not yet about story or
art, just the raw loop of action and response.

This step produces a specific judgment: given what you decided the system's intent
was in Step 3, is the game succeeding or falling short at delivering on that intent
mechanically? Be concrete — point to a specific moment or mechanic, not a vibe.

### 5. Read the experience layer

Set the systems analysis aside for a moment and look at the surface: art direction,
music, writing, voice acting, visual storytelling, pacing of scenes. Judge this layer
by the standards of the other media it's borrowing from — hold the writing to the bar
of good prose, the art direction to the bar of film or illustration, not to a
lowered "pretty good, for a game" standard. This is where a game earns or loses
points on craft that has nothing to do with its systems.

If the theme, mood, or emotional identity of the game is worth capturing formally
(e.g. to build a reference board or brief from it), this is a natural point to hand
off to `game-design-emotional-canvas` or `moodboard-generator`.

### 6. Guess what the experience is *for*

Same move as Step 3, one layer up: what was the experience layer trying to make the
player feel, and is that intent even legible? A game whose emotional intent can't be
identified at all is a real failure at this layer, worth naming plainly rather than
working around.

Broadly, experiences tend to be either **impositional** — crafted to produce a
specific intended emotional arc in every player who engages with it as designed — or
**expressive** — built from techniques that let meaning emerge more open-endedly, at
the cost of being harder to benchmark against a single intended reaction. Name which
one this is reaching for; it changes what "success" even means for the rest of this
step.

If a sharper articulation of the intended player fantasy would help, this is a good
point to call `game-design-fantasy-extractor`.

### 7. Check whether the layers agree

This is the step that actually produces the useful insight, so don't rush it. Lay
out, side by side:

- what you decided the systems were trying to do (Step 3)
- what the systems actually teach/reward in practice (Step 2 and 4)
- what you decided the experience was trying to do (Step 6)
- what the experience actually communicates (Step 5)

Look for mismatches. A story reaching for real emotional weight sitting on top of a
generic, low-stakes power-fantasy system is a classic failure mode — the narrative
gestures at meaning the mechanics don't earn. The reverse also happens: mechanically
ambitious, tightly-tuned systems wrapped in flavor text so thin it undersells what
the player is actually accomplishing. The strongest craft — worth calling out
explicitly when you see it — is when a mechanical choice *is* the thematic point: a
tedious or punishing system that exists specifically because the fiction is about
tedium or punishment, so what looks like a mismatch on paper resolves into intentional
synergy once you see what it's doing.

Name the specific place where alignment or mismatch shows up — a scene, a system, a
moment — rather than delivering the verdict as an abstract summary.

### 8. Only now, talk about fun

Personal enjoyment is real but is not the analysis — it's a downstream, subjective
data point, and it's frequently uncorrelated with craft quality in either direction.
Close by predicting how well this game is likely to land *for the audience it seems
built for*, based on everything above, rather than scoring it against a universal
notion of fun. A game can be craft-excellent and still not be your thing, and a
sloppy, misaligned game can still be somebody's favorite.

## Output shape

Write the critique in the order above, as a short section per step (a few sentences
to a paragraph each — this is meant to be a working critique, not an essay). Close
with a synthesis paragraph built around Step 7's alignment check, since that's the
part a standard review skips. Avoid hedging every sentence, but do flag explicitly
which claims are confident reads (backed by an observable mechanic or line of
dialogue) versus genuine guesses about intent — the two shouldn't read the same on
the page.
