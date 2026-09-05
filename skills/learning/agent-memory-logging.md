# Agent memory for hands-on learning

AgentMemory is the durable store for prior learning evidence.

## Roles

- `/lab` recalls prior knowledge read-only to personalize an exercise.
- `/break-it` persists measured load thresholds after an observed run.
- `/dunning-krueger`, supplied by `devinat1/skills`, owns knowledge-assessment
  writes such as demonstrated knowledge, confirmed gaps, and resolutions.

## MCP server

- **Server:** `user-agentmemory`
- **Tools:** `memory_save`, `memory_recall`, `memory_smart_search`
- **Prerequisite:** agentmemory at `AGENTMEMORY_URL` (default
  `http://localhost:3111`). Start it with
  `npx @agentmemory/agentmemory@0.9.27`.

Read each tool's schema before calling it. Always pass `project` for scoping.
On MCP failure, report the failed recall or save and continue without a markdown
fallback.

## Project slug

Resolve once per run:

1. Use the `project` value in `docs/agents/agent-memory.md` when present.
2. Otherwise normalize `git remote get-url origin` to an `owner-repo` slug:
   strip `.git` and replace `/` with `-`.
3. Otherwise sanitize the workspace folder name to lowercase kebab-case.

Mention `/setup-devinat1-skills` when falling back to step 3.

## Read-only recall for lab

1. Search the candidate topic and domain with `memory_smart_search`; use
   `memory_recall` when broader project history is needed.
2. Prefer the newest specific evidence when entries conflict.
3. Treat recalled claims as prior evidence. They may change exercise depth and
   emphasis but never prove current mastery.
4. Never save a knowledge claim from `/lab`.

## Break-it save

After the measured run, save one `load-threshold:` fact containing the concept,
throughput, p99, trigger, and predicted ceiling. Deduplicate materially
equivalent measurements first.

```text
load-threshold: {concept} (System Design) — measured {throughput} req/s, p99
{latency} at {trigger}. Predicted ceiling: {derived ceiling}
```
