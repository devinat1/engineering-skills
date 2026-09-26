---
name: reorder
description: Reorganize an entire Graphite PR stack when its structure no longer makes sense, or handle a bounded handoff from absorb for changes needing new branches or reordering. Also use for whole-stack preparation in pre-pr-review.
---

# Reorder: organize the stack

This skill replaces `graphite`; Graphite remains the CLI. Reorder owns explicit
placement, branch creation, splits, combinations, parent changes, and restacking.
Follow [the shared stack-change policy](CHANGE-POLICY.md) once per run. Feature
implementation, review, and publication belong to other workflows.

Choose the entry mode: direct `/reorder` and pre-pr-review preparation use
**Whole stack**; an absorb handoff uses **From absorb**, never whole-stack by default.

## Whole stack

Inspect the selected stack and in-scope local changes using the shared policy.
Show a short priority menu informed by those changes and ask the user to select
any combination, without ranking:

- **Clear PR purpose** — each branch tells one coherent design story.
- **Small review diffs** — narrowly scoped, easy-to-review branches.
- **Foundation-first order** — reusable or stable changes lower in the stack.
- **Fewest PRs / least churn** — a compact stack with minimal reshuffling.

Use those priorities to assemble concrete layout options and let Jev select via
the shared policy. Keep an already coherent stack unchanged when it best fits.
Existing commits and branch boundaries may be split, combined, reordered, or
recreated within the selected stack.

After the priority answer, show the selected layout briefly and apply it
immediately. Do not ask for a second approval of the layout or local rewrite;
invoking this workflow authorizes that execution unless the user or higher-priority
instructions restrict it. Leave superseded branches/worktrees in place: cleanup
is not part of the fast path and requires a separate explicit request.

## From absorb

Use the bounded handoff in
[absorb's Call reorder when needed](../absorb/SKILL.md#call-reorder-when-needed).
Require its scope, input identity, and authorization; missing handoff information
is a blocker, not permission to switch modes. Reuse inspection, Jev choices, and
already-applied results; check only state changed since the handoff was prepared.

Use **fewest changes** and **clear branch ownership** as fixed priorities; skip
the priority menu and a second approval prompt. Preserve existing branch purposes
and committed group boundaries. Apply handed-off owners directly when absorb's
line-history heuristic could not place their changes. For `no_fit` or required
new grouping/order decisions, offer bounded layouts to Jev in one batch:

- Explicit amendments to existing owners.
- Focused new branches for incoming changes with no existing owner.
- Required parent/order changes and descendant restacking for those dependencies.

Proceed under absorb's standing authorization. If integration requires redesigning
existing committed groups or branch purposes, return the blocker and request a
direct `/reorder`. Missing implementation stays pending rather than prompting a
feature fix. No branch/worktree deletion or unrelated restructuring is covered.
Do not call `absorb` back; return results to its current run.

## Apply and return

Use installed Graphite amend/create/move/restack operations to realize the selected
layout, isolating pending/out-of-scope changes as the shared policy requires.
Batch independent operations when practical and restack affected descendants only
as required, rather than after every edit. Reuse known command syntax and Jev
choices; newly required decisions follow the shared policy, not an approval loop.

For review fixes within an already selected whole-stack layout, reuse its
priorities and authorization. Place implemented fixes without restarting the
interview; ask Jev only for new grouping/placement decisions. Routine completed
diffs outside that review workflow belong to absorb.

Finish with the shared final check. Return the entry mode, resulting branch
sequence/parents, applied changes, and pending reasons in one concise result.
Leave cleanup and publication unperformed; this skill never mutates remotes.
