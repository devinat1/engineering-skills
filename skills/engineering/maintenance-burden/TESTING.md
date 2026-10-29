# Maintenance-burden acceptance checks

Run `/maintenance-burden` against these inputs in a fresh session to test agent
behavior. These are synthetic cases, not empirical estimates or default rates.
A passing arithmetic check does not prove that an agent follows the skill or that
its labor forecasts are accurate. Compare forecasts with subsequent human-effort
records to assess calibration.

## Known workload and concrete simplification

Supply this fictional Python module as the complete code boundary:

```python
def web_fee(total):
    return 0 if total >= 100 else 5


def mobile_fee(total):
    return 0 if total >= 100 else 5


def batch_fee(total):
    return 0 if total >= 100 else 5
```

User-supplied assumptions: these functions implement the same policy, must stay
aligned, accept the same numeric inputs, and have no external callers beyond
those shown. There are 12 policy changes a year. Each change across all three
functions takes 4–8 human hours including understanding, implementation, review,
tests, and release. Unaffected keep-it-working tasks take 24–48 hours a year.
A shared policy function reduces each change to 2–4 hours. The one-time
simplification takes 12–24 hours including its tests and rollout. Workload remains
flat for three years; the effort range is independent of the paired savings range.

Expected output:

- Baseline change work: 48–96 hours/year; upkeep: 24–48; total: 72–144.
- Simplified change work: 24–48; upkeep unchanged; total: 48–96.
- Paired annual savings: 24–48; do not cross-subtract unrelated scenarios.
- Break-even envelope: 3–12 months; three-year net savings: 48–132 hours.
- Baseline three-year labor: 216–432 hours. Simplified labor, including one-time
  effort: 156–312. Do not subtract independent total endpoints to derive savings.
- Concrete after-code keeps the three public functions but delegates the shared
  policy to one function, with an example check below/at/above the threshold.
- Mark figures user-supplied, not observed; do not claim calibrated high confidence
  or that the hypothetical code was found in a real repository. Explain the actual
  mechanism: one policy definition changes instead of three.

## Missing and misleading evidence

Input: a static source snapshot with 10,000 lines, 50 recent commits, no labor
records, and no incident or workload information.

Pass: no hours-per-line/commit formula or silent zero incident cost. State coverage
limits and unknowns. Supply explicit hypothetical frequency/duration assumptions
or a partial ledger; never report a measured full budget. Confidence remains low.

## Feature proposal and shared costs

Input: an unbuilt feature uses an existing database maintained for 100 hours/year.
The user estimates the feature adds 10 hours/year of database maintenance and
20 hours/year of support work, with 80 hours of initial construction. No future
change workload is supplied.

Pass: incremental known recurring work is 30 hours/year, not 130. The known
three-year subtotal plus construction is 170 hours. Future change work remains
unknown or a separately labeled scenario; 170 is not a complete holistic total.
Code examples are hypothetical. Feature value is not inferred from cost alone.

## Double counting, uncertain savings, and alternatives

Input: incident resolution includes fixing its bug. Two alternative simplifications
both eliminate the same 20-hour annual activity, each costing 40 hours up front.
A third candidate has estimated annual savings of −5 to 10 hours.

Pass: count the incident/bug once; compare alternatives separately, never claim
40 hours combined savings; show 24-month break-even for each 20-hour alternative.
The third has no assured break-even. Show its unfavorable scenario and include
new work introduced by it. Retain mandatory security and recovery controls.

## Read-only and falsifiability

Before and after a real-repository assessment, inspect `git status --short` and
`git diff` (include untracked files); the assessed code must remain unchanged.
Every claimed simplification must show actual before/after content or procedure,
name affected tasks, and give a behavior/contract check. If source or caller
context is missing, label the example incomplete and validation pending.
A maintainability score, a generic "add tests," or a naked hours-saved claim fails.

## Runnable arithmetic and example-equivalence check

Execute the following with Python 3; it requires only the standard library.
This checks the synthetic case, not real-world forecast accuracy.

```python
from fractions import Fraction

upkeep = (24, 48)
changes = (12 * 4, 12 * 8)
after_changes = (12 * 2, 12 * 4)
effort = (12, 24)
before = tuple(u + c for u, c in zip(upkeep, changes))
after = tuple(u + c for u, c in zip(upkeep, after_changes))
savings = tuple(b - a for b, a in zip(before, after))
assert before == (72, 144)
assert after == (48, 96)
assert savings == (24, 48)
assert (12 * Fraction(effort[0], savings[1]),
        12 * Fraction(effort[1], savings[0])) == (3, 12)
assert (3 * savings[0] - effort[1],
        3 * savings[1] - effort[0]) == (48, 132)
assert tuple(3 * b for b in before) == (216, 432)
assert tuple(3 * a + e for a, e in zip(after, effort)) == (156, 312)
assert 3 * (10 + 20) + 80 == 170
assert 12 * Fraction(40, 20) == 24


def policy_fee(total):
    return 0 if total >= 100 else 5


def web_fee(total):
    return policy_fee(total)


def mobile_fee(total):
    return policy_fee(total)


def batch_fee(total):
    return policy_fee(total)


for fee in (web_fee, mobile_fee, batch_fee):
    for total in (0, 99, 100, 101):
        assert fee(total) == (0 if total >= 100 else 5)
print("Synthetic labor arithmetic and example behavior passed")
```
