---
name: rate
description: Rate the current branch diff (1-5) against clean code, DDD, OOP, and idiomatic principles. Use when the user invokes /rate.
disable-model-invocation: true
---
## Automatic Jev check

When `/rate` is reviewing an actual branch diff and has an evidence-backed
preliminary rating for a named guideline, read
`${AGENTIC_HOME:-$HOME/.agentic}/artifacts/jev/PROTOCOL.md` and run its helper.
Send stable source IDs, the bounded diff/context, the named guideline, and the
proposed rating. Ask a **Choice**: `Does the supplied evidence support this
proposed rating?` with `supports` (the cited evidence supports it), `contradicts`
(the cited evidence materially conflicts), and `unclear` (context is insufficient).
Reconcile the advisory answer with the evidence; retain the original rating and
explanation on unavailable, contradiction, or unclear. When `/clean`, `/ddd`, or
`/oop` are borrowed criteria, do not invoke their separate Jev checks; still run
this `/rate` check. It never changes the
visible 1–5 scale or authorizes changes.



Before scoring, say that you are using `/clean`, `/ddd`, and `/oop` as review
criteria. These are borrowed criteria, not child-skill invocations.

According to /branch, rate from 1 to 5 (5 means perfect, 1 means terrible) how much my code follows principles for each principle shown in:
## Bob Martin guidelines
/bob

## Clean code guidelines
/clean

## Domain driven design guidelines
/ddd

## Object oriented guidelines
/oop

## Idiomatic guidelines
/idiomatic

Also, make sure to explain each of the terminologies you are using.
