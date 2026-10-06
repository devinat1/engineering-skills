---
name: pattern-gate
description: When preparing a build prompt, Build Brief, or implementation plan for code that adds structure, an API, a dependency, or control flow, include the pattern list in that artifact before presenting it. Trigger during preparation, not after the prompt or plan is approved. Also use on /pattern-gate, for user-supplied code, or when a new pattern is needed.
---

# Pattern gate

One pattern list covers the whole planned change. Approval of the build artifact containing that list is permission to edit, subject to any other active gates.

## When to run

Trigger as soon as an applicable build or change request is recognized, including code the user handed over verbatim. Load this skill before preparing the first build prompt, Build Brief, or implementation plan. Use initial read-only exploration and any required interview to identify the patterns.

Skip an edit that adds no structure, API, dependency, or control flow, such as a typo, a comment, or formatting.

Include the pattern list inside the first build artifact: `clarify`'s copy-paste prompt, `safeguard`'s Build Brief, or a direct implementation plan. Present the artifact and list together for approval. When the workflow only produces a prompt, include the list and approval requirement in that prompt and stop under that workflow's rules.

If a supplied prompt or plan lacks a pattern list, add it before requesting approval or starting edits. Mark unresolved pattern choices explicitly rather than inventing them; resolve those choices and obtain approval before using them.

Done when the first build artifact contains its pattern list and approval requirement. Implementation waits for explicit approval of both, not a separate routine pattern-review step after build approval.

## Pattern list

List every named design pattern, codebase convention, language feature, library, algorithm, and other technique the change will use, including conventions copied from the surrounding code.

Each item has three parts: the name, where it will show up, and why it is being used.

Include the list in the build artifact. For same-session implementation, wait until the user explicitly approves the artifact and its list.

## Unfamiliar terms

The user selects unfamiliar terms. Only those selections count.

For each selected term, explain in a few sentences what it means in this change, then save it at once with `memory_save`:

- `project`: `devinat1-personal`
- `type`: `pattern`
- `content`: the term, where, why, and the task

Skip the destination prompt and any Proposed-memory choice. This save is the exception to the memory-approval rule, and only for these flagged terms. Save because the user selected the term, even if they later revise that item off the list. If the save fails, stop and say so.

A flag or an explanation is not approval. The user may approve a list that still contains unfamiliar terms. The record is for a later `/learn` the user starts. It does not ban the pattern in this change.

## Revision

When the user withholds approval, they name which items to change. Revise the build artifact and its full list, then wait. Done when the user approves the revised artifact and list.

## After approval

Use the patterns on the approved list. When later work would use a pattern that was not on it, stop before using it. Show that item with the same name, where, and why, and wait for approval of the added item.
