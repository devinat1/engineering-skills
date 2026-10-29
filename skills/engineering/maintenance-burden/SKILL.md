---
name: maintenance-burden
description: Estimate human-only maintenance labor for a codebase, existing feature, or proposed feature. Use for upkeep budgeting, feature maintenance tradeoffs, or finding labor-saving simplifications with concrete before/after changes.
---

# Maintenance Burden

Estimate person-hours, not a maintainability score. Explain which work consumes
those hours and show the simplifications that could remove it. Code inspection
supports a forecast, not a measurement of historical labor.

## 1. Bound the assessment

Identify the repository/revision and feature boundary, or the supplied proposal.
Use existing context first; ask only for a missing target or an assumption that
would materially change the result. Otherwise state assumptions and proceed.

Default to humans working without coding agents, familiar with the language and
stack. Ordinary tools, tests, and automation already present remain available.
Count everyone's active work, including investigation, implementation, review,
testing, release, coordination, documentation, and operational follow-up.
Two people working an hour is two person-hours. Separate elapsed lead time,
on-call coverage, and machine runtime from active labor.

Use annual recurring hours and a three-year comparison by default. State workload,
change frequency, team familiarity, service expectations, and the forecast start
point. With no roadmap, estimate effort per representative change and show an
explicit hypothetical frequency instead of pretending future demand is known.
Keep one-time onboarding, cleanup, migration, and initial feature construction
separate. Three years of flat workload is a scenario, not a growth prediction.

Assessment is read-only: inspect source, available history, docs, and authorized
operational evidence. Show proposed changes without editing the target repository,
installing dependencies, or performing production actions. If writing a report,
use an explicitly requested location or shared `artifacts/maintenance-burden/`
under `${AGENTIC_HOME:-$HOME/.agentic}`. Follow active approval and advice gates
before recommendations or any separate implementation handoff.

**Complete when:** target, human assumptions, horizon, and exclusions are explicit.

## 2. Gather evidence for actual work

Read repository guidance and trace representative end-to-end flows, callers,
shared dependencies, tests, deployment, and operational responsibilities. Use
CodeGraph for structure when available; respect repository initialization gates.
If unavailable, trace with file search and report that limitation. Sample large
repositories deliberately, disclose coverage, and avoid extrapolating a few
files to every subsystem without support.

Look for maintenance drivers across:

- **Corrective:** bugs, incidents, diagnosis, recovery, and regression checks.
- **Adaptive:** dependency/security patches, runtime upgrades, external API changes,
  schema/data migrations, and compatibility obligations.
- **Operational:** release work, monitoring, backups/restore drills, data repair,
  capacity work, and applicable security/compliance activities.
- **Evolution:** modifying/extending behavior, tracing coupling, integration,
  review, testing, rollout, and updating docs/contracts.
- **Knowledge and coordination:** onboarding, ownership gaps, handoffs, and
  support investigation where engineering labor is involved.

For each applicable area, connect a concrete source to a task someone must do.
Check history, issue/incident records, time logs, runbooks, and CI evidence when
available and authorized. Record source paths/lines or record IDs and the observed
period. An issue's open duration and commit timestamps are not hours worked.
Lines of code, churn, test counts, or complexity are clues to investigate, not
conversion factors from code to labor. No incidents recorded is not proof of
zero incident work; automated updates still need human validation when applicable.

Classify each input as **observed**, **user-supplied**, or **assumed**. Distinguish
historical human-only work from AI-assisted history before using it to calibrate
this forecast. Mark missing operational data rather than silently assigning zero.
For a proposal, cite its design assumptions and label examples hypothetical;
there is no existing implementation to inspect.

**Complete when:** each cost driver has evidence or an explicit assumption, and
coverage gaps are recorded.

## 3. Build a labor ledger

Use non-overlapping activities with these columns:

`Activity | Scope/category | Events/year | Human hours/event | Hours/year | Evidence/assumption | Confidence`

For each activity, calculate `events/year × person-hours/event`; include recurring
fixed tasks as scheduled events. Use low/high scenarios and calculate with a
calculator or executable arithmetic. State why both frequency and duration are
plausible. Use supplied work logs to calibrate when representative. Otherwise,
label values judgment-based; do not invent industry benchmarks or fitted weights.

Assign each task once. Incident resolution includes its bug fix unless explicitly
split; testing/review are either included in each task or separate rows, not both.
Onboarding depends on assumed staffing changes, not an automatic annual charge.
Keep ordinary feature-development work visible but separate from the extra effort
caused by the existing design; when those cannot be separated, say so.

Show three distinct amounts:

- Recurring keep-it-working labor.
- Future change labor at the stated demand, also expressed per change when useful.
- One-time work, including onboarding or proposed simplification work.

`Annual labor = sum of recurring keep-it-working and change rows`

`Three-year labor = one-time work + year 1 + year 2 + year 3`

Only replace the yearly sum with `3 × annual labor` when workload is held constant.
Present low/high totals as scenario bounds, not statistical confidence intervals.
Confidence describes evidence quality: high needs representative human-effort
records, medium has partial records or relevant measured analogues, and low is
largely assumed. Overall confidence must reflect material low-confidence rows.
Round final figures to useful hours or days; define a person-day as eight hours
if used. Show the assumptions that move the total most. Large infrequent incidents
belong in a separate stress scenario when their frequency cannot be defended.

For a proposed feature, compare **without feature** against **with feature** at
the same workload and service expectations. Attribute only additional shared
service work to the feature, not the entire platform. Show incremental annual
labor and initial construction separately. Labor alone cannot establish that a
feature is worth building: identify the missing benefit/value assumption.

If evidence cannot support even a rough numeric range, provide the ledger with
unknown rows, a clearly partial subtotal, and the smallest missing input needed.
An optional hypothetical scenario must be labeled as such, never as a measured
budget or a complete total with unknown rows silently omitted.

**Complete when:** totals reconcile, units and assumptions are visible, and
unknown work is not hidden in a falsely complete estimate.

## 4. Show the simplifications

Find the few largest defensible reductions in human work. Trace callers and
invariants before proposing a shorter implementation. Prefer deletion, existing
helpers, standard library, and native platform behavior when they preserve the
requirements. Fewer lines alone does not establish lower maintenance effort.

For each candidate show:

- **Where and what:** paths/lines, the labor driver, and the exact mechanism that
  removes work (for example, one policy change instead of three coordinated edits).
- **Concrete change:** a focused proposed diff or before/after code/configuration.
  For an operational simplification show the exact before/after procedure. For an
  unbuilt feature show a minimal hypothetical design/code comparison. Mark omitted
  context and untested examples; do not fabricate current source or claim a snippet
  is a complete, tested patch.
- **Safety and tradeoffs:** caller/contract effects and a concrete validation
  command or acceptance check. Preserve security, correctness, accessibility, and
  necessary observability. Label behavior changes, feature removal, outsourcing,
  and lost flexibility explicitly rather than calling them behavior-preserving.
  Account for work shifted to vendors or other teams and residual human oversight.
- **Economics:** affected ledger rows before/after, one-time implementation,
  migration, review, testing, rollout, and learning effort; annual hours saved;
  three-year net hours saved; and break-even time under the same workload.

Use paired before/after scenarios: `annual savings = before − after` at the same
frequency and service level, including any new ongoing work. Preserve dependencies
between assumptions. For independent nonnegative effort and strictly positive
savings ranges, a conservative break-even envelope in months is
`12 × [effort_low / savings_high, effort_high / savings_low]`.
If savings can be zero/negative, report that break-even is not assured; do not
divide by zero or present only the favorable case.

`Three-year net savings = sum of yearly savings − one-time simplification effort`

Subtract implementation effort once. For flat workloads and independent ranges,
use `[3 × savings_low − effort_high, 3 × savings_high − effort_low]`.
For linked assumptions, calculate each coherent scenario instead. Deduplicate
shared savings and migration costs before combining candidates; mutually exclusive
alternatives get separate comparisons. Rank by defensible net labor savings and
risk, not by the size of the deletion. Keep worthwhile-looking but unquantifiable
ideas separate from the numeric savings total. If no defensible simplification
exists, say so rather than manufacture one.

**Complete when:** each quantified candidate has a concrete change, validation
check, and traceable before/after labor calculation.

## 5. Report the decision surface

Lead with the human-only annual range, recurring versus change-work subtotals,
one-time effort, and confidence. Then provide the compact ledger, concrete
simplifications with economics, and the three-year comparisons. End with the
largest uncertainties and the evidence needed to narrow them. Separate what is
observed, assumed, and not verified throughout.

For budgeting, make the labor and staffing assumptions usable without equating
person-hours to elapsed delivery time or full-time staffing without a stated
capacity basis. For feature decisions, expose incremental upkeep and benefit
requirements. For simplification decisions, show effort, savings, tradeoffs, and
break-even together. None authorizes applying a change.

Before delivery, check units, arithmetic, duplicate tasks/savings, scenario
consistency, source references, and whether each proposed simplification actually
removes the stated work. State what was inspected and what was not tested.
See [TESTING.md](TESTING.md) when validating changes to this skill.
