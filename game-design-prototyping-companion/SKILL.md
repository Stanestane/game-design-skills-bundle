---
name: game-design-prototyping-companion
description: Track game design prototype ideas, branching outcomes, dead ends, baselines, and next experiments, and optionally generate a simple SVG visualization of prototype evolution. Use when a prototype leads to several possible follow-up paths, when the team needs to backtrack without losing learned branches, when exploring unknowns through multiple iterations, or when you want both a written prototype log and a branch map of how the concept evolved over time.
---

# Game Design Prototyping Companion

Track prototype evolution, not just prototype results.

Use this skill when prototyping produces branching decisions, dead ends, alternative paths, and backtracking. The aim is to preserve learning structure: what was tested, what was learned, what branch it created, which path was followed, and which paths remain available to revisit.

This skill can also generate a simple SVG branch map from a lightweight text or JSON structure.

## What to produce

Generate one or more of these outputs:
1. **Prototype log** - what was tested and why
2. **Branch record** - what paths emerged from the result
3. **Decision state** - which branch is current, parked, dead, baseline, or promising
4. **Backtrack notes** - what can be revisited later and under what condition
5. **SVG branch map** - a visual map of prototype evolution

## Core principle

A prototype is not just a yes/no answer.
It often creates a tree:
- one branch becomes the current path
- another becomes a dead end
- another becomes a parked idea worth revisiting later
- another reveals a stronger question than the original one

The skill should preserve that tree.

## Workflow

### 1. Define the prototype node
For each prototype node, record:
- **Node ID**
- **Prototype name**
- **Question being tested**
- **What was built or simulated**
- **What was learned**
- **Result state**

Use result states such as:
- **baseline**
- **promising**
- **branch trigger**
- **dead end**
- **parked**
- **production candidate**

### 2. Record branch options
When a prototype produces several next moves, capture each branch explicitly.

For each branch, record:
- **Branch ID**
- **Parent node**
- **New idea or variation**
- **Reason it exists**
- **Current status**

### 3. Mark the chosen path without deleting the others
Do not treat the selected branch as the only meaningful output.
Preserve:
- abandoned paths
- deferred paths
- weird side paths
- stronger substitute ideas revealed by the test

### 4. Add backtrack logic
If a branch is not chosen now, record:
- what would justify revisiting it
- what blocker currently prevents it
- what later discovery might make it relevant again

### 5. Generate a visual map when useful
Use `scripts/branch_map_svg.py` to render a simple SVG from a branch-map JSON file.

Read:
- `references/branch-map-format.md` for the input structure
- `references/example-branch-map.json` for an example

## Response structure

Use this structure unless the user asks for something else:

### Prototype Node
- Node ID: ...
- Question: ...
- Built / simulated: ...
- Learned: ...
- State: ...

### Branches Created
1. ...
2. ...
3. ...

### Current Chosen Path
- ...

### Parked / Revisit Later
- ...

### Suggested Next Prototype
- ...

## Visualization workflow

When the user wants a visual branch map:
1. write the branch data to JSON using the format in `references/branch-map-format.md`
2. run `scripts/branch_map_svg.py <input.json> <output.svg>`
3. return the SVG path and summarize what the map shows

## Style rules
- Preserve branching history.
- Prefer explicit node IDs over vague prose.
- Distinguish clearly between what was learned and what was merely assumed.
- Do not erase dead ends; label them.
- Do not confuse the current path with the best possible path forever.

## References

- `references/branch-map-format.md` for the JSON structure
- `references/example-branch-map.json` for a starter example
- `references/state-labels.md` for recommended branch/node labels

## Working principle

Prototype trees are design memory.
If you only remember the path you chose, you lose the intelligence of the paths you rejected.
