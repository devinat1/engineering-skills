---
name: interviewer
description: Route a request for a mock interview to a focused interview skill. Use on /interviewer when the interview type is not specified.
disable-model-invocation: true
---

# Interview router

Identify the user's requested practice; if the type is unclear, ask which one. Return the matching command and a one-sentence reason, then stop so the user can invoke the focused skill:

- Research/project pitch → [`/research-pitch-interview`](../research-pitch-interview/SKILL.md) (Heilmeier Catechism; not an investor pitch)
- System design → [`/system`](../system/SKILL.md)
- Behavioral/job experience → [`/behavioral-interview`](../behavioral-interview/SKILL.md)
- Coding/algorithms → [`/coding-interview`](../coding-interview/SKILL.md); for one supplied LeetCode problem with guided coaching, [`/leetcode-interviewer`](../leetcode-interviewer/SKILL.md)
- Technical/domain knowledge → [`/domain-interview`](../domain-interview/SKILL.md)

This compatibility router only identifies the next skill. Do not run a generic mixed-topic interview or score the router itself. The user invokes the selected skill, which owns questioning, debrief, and stopping rules.
