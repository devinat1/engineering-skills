# Lab file shape

Generate one coding exercise with an obvious learner entry point and executable
tests.

## Directory

```text
YYYY-MM-DD-<topic-slug>/
  EXERCISE.md
  answer.<ext>
  test_answer.<ext>
```

Use the language's conventional test filename when it differs.

## Exercise instructions

`EXERCISE.md` contains:

```markdown
# <Topic> lab

Goal: <one observable outcome>

Constraints:
- <constraint that teaches the concept>

Run: `<exact test command>`

Estimated time: ~<minutes> min
```

## Learner file

Provide the smallest starter that exposes the target concept:

```python
def normalize_topic(raw: str) -> str:
    """Return a filesystem-safe slug."""
    raise NotImplementedError("Implement this")
```

## Tests

Use ordinary assertions and behavior-revealing names:

```python
from answer import normalize_topic


def test_lowercases_and_replaces_spaces():
    assert normalize_topic("Signal Handling") == "signal-handling"


def test_collapses_extra_separators():
    assert normalize_topic(" nats / jetstream ") == "nats-jetstream"
```

Tests must be runnable locally without hidden services or credentials. Avoid
conceptual prompts, hidden grading rubrics, answer keys, and solution files.
