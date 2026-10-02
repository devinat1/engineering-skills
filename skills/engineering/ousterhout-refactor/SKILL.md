---
name: ousterhout-refactor
description: Deepen existing modules using Ousterhout's information-hiding lens when restructuring code without changing behavior. Load when callers know implementation details, a multi-step recipe leaks across modules, or an interface is harder to use than the complexity it hides; keep feature changes separate.
---

# Ousterhout Refactor

Refactor to make a module's interface simpler than the complexity behind it. Depth is about information hidden from callers, not file length or number of functions. Use Fowler's incremental, behavior-preserving discipline for each change; this skill chooses the boundary worth changing.

## Workflow

1. **Find leaked knowledge.** Trace the relevant callers, callee, tests, and side effects. Name the specific decision or invariant callers must currently repeat or coordinate (for example, a required call sequence or shared field relationship). If no concrete leak exists, leave the boundary alone. Done when the leak and its affected callers are identified.
2. **Choose an owner.** Put that knowledge in the module best positioned to enforce it. State the proposed caller-facing operation and what callers no longer need to know. Prefer an existing module and a small interface over an extra layer. Keep necessary timing, authorization, and transaction responsibilities explicit. Done when the new interface hides the named knowledge without making ordinary use harder.
3. **Move one coherent responsibility.** Change the interface and callers in a behavior-preserving step. Retain externally observable outputs, errors, ordering, privacy, idempotency, and concurrency guarantees; distinguish any requested behavior change from the refactor. Done when all affected callers use the new boundary and no old recipe remains exposed solely for them.
4. **Verify the boundary.** Run focused tests and inspect the diff for changed behavior. Where an invariant lacks coverage, add the smallest useful characterization check. Compare before and after: can a caller accomplish the task with less knowledge and fewer ways to misuse the API? If not, inline or revert the new abstraction. Done when checks pass and the interface improvement is concrete.

## Design tests

- **Information hiding:** Group code by the decision it owns, not merely by execution phase. When a decision changes, how many modules must change together?
- **Deep interface:** Prefer one operation that performs an inseparable recipe over public helpers that force callers to assemble it. Avoid an operation whose name sounds like storage but silently performs unrelated domain transitions.
- **Pass-throughs:** A wrapper that merely forwards parameters adds a surface without hiding a decision; inline it unless it establishes a useful boundary.
- **Complexity downward:** Let the owning module handle exceptional cases when that simplifies its callers overall. Do not bury a constraint callers must know to use it safely.

Treat these as prompts to inspect actual code, not automatic instructions to split long files, merge modules, introduce classes, or rewrite the whole repository.
