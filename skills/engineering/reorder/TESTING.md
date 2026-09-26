# Absorb and reorder checks

From the engineering-skills repository root, run:

```sh
python3 scripts/generate-skill-metadata.py --check
git diff --check
```

Check that both skills link to `CHANGE-POLICY.md`, and that pre-pr-review delegates
stack preparation to reorder without adding a second approval or validation loop.
The pre-existing `scripts/test-stack-skills.py` targets the retired policy: it
requires a 0.80 threshold, three-cycle budget, and final rewrite approval. It is
not an acceptance test for this instruction-only revision; no scripts were changed.

Exercise these agent scenarios in a disposable Graphite stack. Static text checks
do not prove placement correctness, model behavior, or latency. Compare elapsed
time and inspection/API round trips with the previous instructions on the same
starting state before claiming a measured speedup.

| Input | Expected behavior |
| --- | --- |
| Clean checkout | No-op without a Jev call or rewrite. |
| Ordinary completed diff with existing owners | Reuse task context; one batched ownership request, one absorb dry-run, matching absorption, one final check. |
| Highest-probability owner has low confidence | Use the returned owner without threshold, retry, or host-agent rejudgment. |
| Tied maximum probabilities | Use the API's returned choice if it is one of the maxima. |
| New file cannot be absorbed into its selected owner | From absorb places it explicitly, reusing the owner; no repeated Jev check or priority interview. |
| Ownership selects `no_fit` | Hand off once; Jev chooses a bounded new layout rather than forcing an existing owner. |
| Layout selects `none_fit` | Leave affected changes pending; do not choose the runner-up or begin a revision loop. |
| Direct whole-stack reorder | Ask priorities once, select a layout with Jev, apply immediately without final-layout approval; leave superseded local resources in place. |
| Coupled grouping/order choices | Select a complete feasible layout; avoid incompatible independent decisions. |
| Handoff after successful absorption | Reuse evidence/choices; operate only on remaining changes and check only changed state. |
| Missing implementation or unrelated edits | Keep incomplete/dependent groups pending and unrelated contents/staging intact. |
| Missing credentials, unavailable Jev, API error, timeout, or malformed response | Stop immediately; no host-agent fallback or automatic retry. |
| Command failure, conflict, or detected concurrent changes | Stop and report actual partial progress; do not blindly continue. |
| Pre-pr-review preparation and later fixes | Delegate to reorder, reuse selected priorities, and do not reintroduce approval/confidence loops. |
