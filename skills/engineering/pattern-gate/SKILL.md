---
name: pattern-gate
description: Before code that adds structure, an API, a dependency, or control flow — including user-supplied code — show one pattern list and wait for approval. Also use on /pattern-gate, or when implementation would use a pattern not on the approved list.
---

# Pattern gate

One pattern list covers the whole planned change. Approval of the plan containing that list is permission to edit.

## When to run

After initial read-only exploration, run when the change adds or applies structure, an API, a dependency, or control flow. That includes code the user handed over verbatim.

Skip an edit that adds none of those, such as a typo, a comment, or formatting.

For applicable changes, put the pattern list inside the implementation plan. Present the combined plan and list for approval before editing; do not make pattern approval a later step. If implementation requires a pattern not listed, add it to the plan and get approval before using it.

Done when the plan and its pattern list are approved before any edit.

## Pattern list

List every named design pattern, codebase convention, language feature, library, algorithm, and other technique the change will use, including conventions copied from the surrounding code.

Each item has three parts: the name, where it will show up, and why it is being used.

Include the list in the plan and wait. Done when the user explicitly approves the plan and its list.

## Unfamiliar terms

The user selects unfamiliar terms. Only those selections count.

For each selected term, explain in a few sentences what it means in this change, then save it at once with `memory_save`:

- `project`: `devinat1-personal`
- `type`: `pattern`
- `content`: the term, where, why, and the task

Skip the destination prompt and any Proposed-memory choice. This save is the exception to the memory-approval rule, and only for these flagged terms. Save because the user selected the term, even if they later revise that item off the list. If the save fails, stop and say so.

A flag or an explanation is not approval. The user may approve a list that still contains unfamiliar terms. The record is for a later `/learn` the user starts. It does not ban the pattern in this change.

## Revision

When the user withholds approval, they name which items to change. Revise the plan and its full list, then wait. Done when the user approves the revised plan and list.

## After approval

Use the patterns on the approved list. When later work would use a pattern that was not on it, stop before using it. Show that item with the same name, where, and why, and wait for approval of the added item.
