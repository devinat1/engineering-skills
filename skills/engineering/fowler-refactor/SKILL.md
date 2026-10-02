---
name: fowler-refactor
description: Apply Fowler's behavior-preserving, incremental refactoring practices when restructuring existing code to make it easier to understand or change. Load before extracting or inlining logic, moving responsibilities, or otherwise changing code structure without intending to change behavior; keep feature behavior changes distinct.
---

# Fowler Refactor

Use Fowler's refactoring discipline when changing existing code's structure without intending to change its observable behavior. Refactoring is a means to make the next change easier, not a mandate to eliminate every smell or use a catalog of techniques.

## Workflow

1. **Set the boundary.** State the structural improvement sought and the behavior that must remain unchanged. If the task also changes behavior, identify that separately and keep the behavior change distinguishable from preparatory or follow-up refactoring.
2. **Understand the code.** Trace relevant callers and tests; inspect contracts, side effects, error behavior, authorization, ordering, and transaction or concurrency guarantees where applicable. Reuse existing codebase conventions.
3. **Choose one useful transformation.** Make the smallest coherent change that improves comprehension or makes the next change easier. Use a named refactoring technique only when it addresses a concrete problem; do not treat smells or metrics as automatic instructions to restructure.
4. **Verify each step.** Run the most relevant tests or checks after the transformation. If coverage is missing for behavior at risk, add the smallest useful characterization test when feasible. Tests are evidence, not proof; inspect externally observable behavior and critical invariants directly.
5. **Review the result.** Check the diff for accidental behavior changes, unnecessary abstractions, unrelated cleanup, and broken contracts. Run broader required checks when the change warrants them.

## Technique selection

- **Extract Function / Rename** when a name makes intent or a distinct operation clearer; avoid extraction that merely replaces a few straightforward lines with indirection.
- **Inline Function / Class** when a wrapper or abstraction no longer earns its cost and removing it preserves behavior and clarity.
- **Move Function** when responsibility belongs with the data or module that owns the behavior; preserve dependency direction and existing architectural boundaries.
- **Replace Conditional with Polymorphism** only when the alternatives are genuinely varying behaviors and the added types clarify the design. A clear conditional is often simpler.
- Apply other Fowler techniques on the same basis: solve an observed design problem, preserve behavior, and prefer the smallest change that improves the code.

For every refactoring step, keep the before-and-after behavior equivalent within the stated boundary. When equivalence is uncertain, stop and resolve the uncertainty before claiming the work is a refactor.
