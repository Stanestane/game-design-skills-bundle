---
name: game-design-skill-shipping
description: Create, polish, package, install, document, commit, push, and publish game-design skills for the game-design-skills-bundle workflow. Use when the user wants a new game-design skill added to the standard pipeline, wants an existing game-design skill updated consistently across workspace and repo, or wants the usual shipping steps handled without restating them; uncompressed copy in workspace, uncompressed copy in the Documents repo, packaged .skill in package-skills, README/catalog updates, git commit/push, and ClawHub publish.
---

# Game Design Skill Shipping

Use this skill to run the standard production pipeline for game-design skills so the user does not have to repeat the ritual every time.

This skill is specifically for the local bundle workflow centered on:
- workspace skills folder
- `C:\Users\Big Dell\Documents\game-design-skills-bundle`
- repo `package-skills/`
- ClawHub publishing

## Core principle

Treat skill work as a shipping pipeline, not just writing a SKILL.md file.

A finished game-design skill is usually expected to exist in four places/states:
1. **Workspace, uncompressed** - for immediate local use
2. **Repo, uncompressed** - as the canonical editable source in the bundle repo
3. **Repo, packaged** - as a `.skill` in `package-skills/`
4. **Published** - pushed to Git and published to ClawHub

## Default assumptions

Unless the user says otherwise, assume all of the following:

- install the skill into workspace in **uncompressed** form
- keep the repo source in **uncompressed** form
- package the distributable `.skill` into the repo's `package-skills/` folder
- align naming with the repo family and neighboring skills
- update bundle docs when a new skill meaningfully changes the catalog
- commit and push repo changes
- publish the skill to ClawHub if auth is available

If any of these should be skipped, the user can say so. Otherwise, do the full pipeline.

## Naming rules

Normalize names before doing anything else.

- Use lowercase letters, digits, and hyphens only
- For game-design family skills, prefer the `game-design-*` prefix unless there is a strong reason not to
- For game-dev planning skills, prefer the `game-dev-*` prefix
- For cross-project or software-team skills, use a non-game-design prefix only when that is already the established family pattern
- Keep the folder name, skill name in frontmatter, package filename, and ClawHub slug aligned

If the draft skill starts with a weak or generic name, improve it before packaging.

## Workflow

### 1. Decide whether this is a new skill or an update

Classify the request as one of:
- **new skill**
- **iterate existing skill**
- **rename/reposition existing skill**
- **repair packaging/docs/publish state only**

Then find the closest neighboring skills in the repo to match tone, structure, and family naming.

### 2. Write or refine the skill in workspace first

Use the workspace copy as the working draft.

Expected location:
- `C:\Users\Big Dell\.openclaw\workspace\skills\<skill-name>`

Do this before repo mirroring so the local workspace stays immediately usable.

When refining the skill:
- match the tone and structure of neighboring game-design skills
- keep frontmatter description trigger-rich but clean
- prefer strong audit/workflow language over vague theory blurbs
- remove template leftovers, duplicate references, and placeholder text
- keep references only when they add real value

### 3. Mirror the finished uncompressed skill into the repo

Canonical repo:
- `C:\Users\Big Dell\Documents\game-design-skills-bundle`

Expected source location inside repo:
- `...\game-design-skills-bundle\<skill-name>`

If this is a rename, remove or replace the outdated repo folder so the repo does not drift into duplicate near-identical skills.

### 4. Align the skill with the family

Before packaging, compare it with adjacent skills and polish for consistency.

Check:
- title style
- frontmatter description style
- section ordering
- audit/workflow framing
- response structure
- use of "Core principle", "What to produce", "Process", "Response structure", "Fast mode", and "Working principle" where appropriate

Do not force every skill into identical structure, but make it feel like it belongs in the same shelf.

### 5. Update repo documentation

For a new skill, usually update:
- `README.md`
- `game-design-skill-catalog.md`

At minimum:
- add a short entry in the most relevant section
- add or update any "best starting points" or "suggested ways to combine them" references if the new skill fills a real gap

For a tiny iteration to an existing skill, only update docs if the use case changed meaningfully.

### 6. Package the skill into the repo package folder

Expected output folder:
- `C:\Users\Big Dell\Documents\game-design-skills-bundle\package-skills`

Package from the repo copy, not the workspace copy, so the published artifact reflects the canonical repo source.

If an old packaged version exists, replace it.

### 7. Validate cleanliness before shipping

Check for:
- duplicate reference files from earlier drafts
- stale filenames after renames
- old package artifacts with outdated names
- mismatched frontmatter `name`
- package filename not matching folder name
- repo docs pointing to the wrong slug or old title

Clean these up before committing.

### 8. Commit and push the repo

Unless the user says not to, commit and push after packaging.

Commit style:
- short, clear, concrete
- examples:
  - `Add game-design multiplayer feature audit skill`
  - `Update game-design goal framing skill`
  - `Rename and republish game-design skill shipping workflow`

Push to the repo's default tracked branch.

### 9. Publish to ClawHub

If ClawHub auth is available, publish the skill.

Default behavior:
- publish from the repo folder
- use aligned slug, display name, and semantic version
- provide a concise changelog

If the skill does not exist yet on ClawHub, publish as an initial release.
If it already exists, bump version appropriately.

## Suggested versioning heuristics

Use these defaults unless the user specifies a version:

- `1.0.0` for a first real public release
- patch bump for wording tweaks, doc polish, packaging cleanup, or minor reference improvements
- minor bump for meaningful workflow expansion, new sections, or stronger capability
- major bump only when the skill's behavior/shape changes drastically enough to break expectations

## Suggested order of operations

When asked to "make a skill" for this repo family, use this order by default:

1. choose/fix the final name
2. create or refine the workspace uncompressed version
3. polish against neighboring repo skills
4. mirror to repo uncompressed version
5. update README/catalog if needed
6. package into `package-skills/`
7. clean duplicates or stale artifacts
8. commit
9. push
10. publish to ClawHub
11. report what changed and where

## Response structure

When reporting completion, include:

### Shipped
- workspace path
- repo folder path
- packaged skill path
- docs updated
- git commit hash if committed
- whether push succeeded
- whether ClawHub publish succeeded

### Notes
- naming decisions
- skipped steps, if any
- any suggested follow-up cleanup

## Fast mode

Use this when the user clearly wants the standard workflow and not a long discussion:
- infer the final skill name
- build/refine it in workspace
- mirror to repo
- package it
- update docs if it is a new catalog-worthy addition
- commit/push
- publish to ClawHub
- return a compact shipping summary

## Working principle

The user should not have to remember the house process every time.

If the request is clearly about creating or updating a game-design skill for the bundle, assume the full shipping pipeline unless told otherwise.
