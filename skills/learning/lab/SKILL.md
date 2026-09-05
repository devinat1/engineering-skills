---
name: lab
description: Create one standalone coding exercise with learner files and executable unit tests. Use when the user asks for a coding lab, hands-on programming exercise, test-driven practice, or selects the lab modality in /learn. Conceptual and written-response exercises are out of scope.
---

# Lab

Create one executable coding exercise for one confirmed topic, then stop.

## Intake

Use a concise learning brief supplied by `/learn` as the source. Otherwise,
resolve the current conversation plus any argument:

- URL: fetch and read it.
- Readable file or directory: inspect only the material relevant to the topic.
- Other argument: treat it as the requested topic.

Confirm one topic when it is not already clear. Ask one question if the language
or test runner remains ambiguous.

Read [agent memory](../agent-memory-logging.md), resolve the project slug, and
recall relevant prior knowledge when the skill is invoked. Use recalled
knowledge only to personalize scope and difficulty; it is not current proof of
mastery. If recall fails, report that once and continue.

Read [EXAMPLE.md](EXAMPLE.md) before creating the lab. It is the source of truth
for the generated file shape.

## Create the exercise

Resolve the destination as:

```text
~/.claude/process-exercises/<repo>/YYYY-MM-DD-<topic-slug>/
```

Append `-2`, `-3`, and so on when needed. Resolve `<repo>` from the git root
basename, then the current directory basename, then `no-repo`.

Create:

- `EXERCISE.md` with the goal, constraints, test command, and estimated time,
- a learner-owned starter file such as `answer.py`,
- a conventional executable unit-test file such as `test_answer.py`.

Use 2–4 focused tests with behavior-revealing names. Include an edge case only
when it teaches the target concept. The starter should make the intended edit
location obvious without revealing the implementation.

## Report and stop

Report the absolute exercise directory, learner file, test file, exact test
command, visible test cases, and a concrete completion-time estimate. The user
runs and iterates on the tests independently.

This skill creates files only. It does not remain active, grade the result,
infer mastery, create a solution file, or write to agent memory.

At successful completion, suggest `/dunning-krueger` so the user can later
provide their questions and answers for an evidence-based assessment. Do not
invoke it automatically.
