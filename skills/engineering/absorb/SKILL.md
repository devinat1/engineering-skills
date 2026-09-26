---
name: absorb
description: Automatically absorb a completed coding diff into the current Graphite stack with minimal changes, or run on /absorb. Delegate changes that need new branches or reordering to reorder; leave only genuinely blocked groups pending.
---

# Absorb: minimal-change integration

Run automatically once after a logical coding change and its required validation,
before handback; also run on explicit `/absorb`. Individual file edits and these
skills' own Git operations do not retrigger it. Respect instructions to defer
absorption or leave work uncommitted. Skip automatic runs outside a configured
Graphite repository; report setup blockers rather than initializing one.

Automatic runs include only the completed task's diff. Explicit `/absorb` includes
the current checkout's staged, unstaged, and untracked changes unless the user
limits scope. Preserve unrelated pre-existing or concurrent work; uncertain task
ownership stays pending. A clean checkout is a no-op.

Preserve existing branch purposes and organization. Standing approval covers
Jev-selected absorption and a bounded `reorder` handoff for this diff, not whole-stack
redesign or cleanup. `absorb` owns the `gt absorb` fast path; `reorder` owns all
non-absorb placement, branch creation, and structural reordering.

## Check and absorb

Read and follow [the shared stack-change policy](../reorder/CHANGE-POLICY.md)
for one inspection pass, batched Jev choices, execution, and a final check. Reuse
current task context; do not invoke whole-stack reorder just to inspect.

Stage only isolated groups with Jev-selected existing owners, then run one
`gt absorb --dry-run` for those groups. Run `gt absorb` where each intact group's
dry-run placement matches its owner. Hand off mismatched or partly absorbable
groups intact; remove them from the staged absorb input first. New files and
other known-unabsorbable groups can go directly to the handoff.

## Call reorder when needed

Invoke the installed `reorder` skill in its **From absorb** mode for groups that:

- have no fitting existing branch (`no_fit`);
- are unabsorbable or have dry-run destinations that differ from selected owners,
  including new files and other changes Graphite's line-history heuristic misses;
- require splitting mixed changes, a new branch, or dependency-driven reordering.

Do not implement an amend/create/reorder fallback inside `absorb`. Pass the
checkout/stack, exact remaining groups, Jev choices and their evidence/options,
dependencies, pending/excluded changes, already-applied results, and the bounded
authorization below. Reuse this context instead of restarting inspection or Jev
checks. Never send already-absorbed content back as an uncommitted input.

The handoff authorizes only the minimum local changes needed to place this diff:
explicit amendment to its owner, focused new branches, required parent/order
changes, and necessary descendant restacking. Preserve existing branch purposes
and committed group boundaries. No branch/worktree cleanup, whole-stack redesign,
or unrelated restructuring is authorized. If broader work is necessary, report
the exact blocker and ask for `/reorder`; do not broaden the handoff implicitly.

Missing implementation and dependent groups stay pending. Continue independent
placeable groups unless the shared policy requires stopping the run. After reorder
returns, reuse its final checks and report one combined result. Reorder returns
to absorb; there is no recursive handoff or retry loop.
