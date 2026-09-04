# Skill connections

This file configures completion-time skill suggestions. A source without a row
has no configured suggestion.

When a source skill reaches an intentional final result, append:

```markdown
**Suggested next:**
- `/target` — [one short reason tied to the completed result]
```

Only the top-level skill emits suggestions. Omit a target already used during
the same run.

| Source | Suggest |
| --- | --- |
| `onboard` | `scale` |
