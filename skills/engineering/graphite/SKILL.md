---
name: graphite
description: Reshape implemented changes into a coherent, independently testable Graphite PR stack, with approval before rewriting.
disable-model-invocation: true
---

# Graphite: smart absorption

Make the stack tell the story of the intended design, not the chronology of
implementation. Each PR introduces one concrete, reviewable change that works
and can be tested with its ancestors applied, without any later PRs.

Use this workflow to split branch work or absorb implemented changes into an
existing stack, including staged, unstaged, and relevant untracked files. Feature
discovery and new feature implementation belong to other workflows; use their
results as input here.

## Inspect and propose

Read repository instructions and inspect Graphite relationships, Git history,
branch diffs, working changes, and available checks. Resolve the target stack
and trunk from the request and repository; ask if the target is ambiguous.
Account for every input change, distinguishing unrelated working files and
branches that must stay untouched. Inspect affected code and dependencies,
not just commit titles. Use the installed Graphite CLI help for commands.

Propose the PR sequence before any history or working-tree rewrite. For each PR,
show its purpose, the changes it owns, its dependencies, and how to test it.
Explain which existing PRs will be retained, split, combined, reordered, or
replaced, and where new PRs are needed. Wait for explicit approval.

Choose boundaries by logical ownership:
- Introduce the intended design in the earliest PR that needs it, rather than
  introducing code and refactoring it in a later PR.
- Redistribute changes across existing PRs instead of dumping them into one PR.
- Keep or add a focused PR when its changes have no coherent existing home.
- Let dependencies determine ordering; among equally coherent orders, place
  stable foundations lower to reduce churn.

## Rewrite after approval

Before mutation, preserve recoverable references for every affected branch and
record the original checkout, branch relationships, and local PR associations.
Snapshot staged, unstaged, and relevant untracked content with its original
state; verify the snapshot can be recovered before replacing working files.
Keep recovery instructions and workflow records under
`${AGENTIC_HOME:-$HOME/.agentic}/state/runs/graphite/<unique-run-id>/` and sensitive
files out of Git. Preserve unrelated work and never rewrite trunk.

Use Graphite to maintain the local stack as you rewrite. Approval authorizes
autonomous execution, including further splits, combinations, reordering, and
code adjustments needed for coherent, testable PRs. A revised sequence does not
need another approval checkpoint. Stop only for genuine blockers such as
unclear intended behavior, unsafe recovery, or unavailable required access.

Preserve intended behavior, including already-implemented new features. The
final tree need not be byte-identical: adapt code and tests where the revised
boundaries require it. This is not permission to add unrelated features or
silently drop input changes.

## Validate and hand back

Check each PR at its own tip with only its ancestors present. Run its focused
checks and repository-required checks as applicable, then validate the final
integrated stack and Graphite parent relationships. Compare the result against
all input changes and explain material final-tree differences. Report actual
commands and outcomes; failing required checks leave the work incomplete, and
unavailable checks leave validation explicitly blocked.

Finish with the resulting PR sequence, its review story, per-PR validation,
deviations from the approved proposal, and concrete recovery instructions.
Keep the result local: do not push, submit, merge, or update remote PRs. Ask the
user to submit the stack after reviewing it, and report any remote PR cleanup
that will be needed rather than performing it.
