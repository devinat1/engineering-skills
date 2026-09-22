---
name: clean
description: Review code for clean naming conventions — descriptive, intention-revealing names. Use when the user invokes /clean or asks for a clean code naming review.
disable-model-invocation: true
---
## Automatic Jev check

During an actual `/clean` review, after proposing a naming finding against a
bounded changed-code slice, read
`${AGENTIC_HOME:-$HOME/.agentic}/artifacts/jev/PROTOCOL.md` and run its helper.
Send only stable source IDs, the relevant declaration/use lines, and the proposed
finding. Ask one **Noul** per finding: `Does this evidence show that the proposed
name fails the stated clean-naming criterion?` True means the cited evidence
supports that exact failure; false means it does not; unavailable context is not
false. Reconcile the advisory answer with the evidence. On unavailable or
ambiguous evidence, keep the ordinary review; do not invoke this check when
these criteria are merely borrowed by another skill. It never suppresses an
evidence-backed finding or authorizes changes.



# Clean Naming

- Use descriptive, intention-revealing names. A variable name should tell you why it exists, what it does, and how it's used.
- Avoid abbreviations and single-letter names outside of tiny loop scopes.
- Use consistent naming conventions across the codebase (e.g., `camelCase` for variables, `PascalCase` for types/classes).
- Name booleans as predicates: `isActive`, `hasPermission`, `shouldRetry`.
- Name functions after what they do, not how they do it.
