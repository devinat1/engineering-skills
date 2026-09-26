#!/usr/bin/env python3
"""Static stack-skill contracts; does not exercise an agent or rewrite Git history."""
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills/engineering"
spec = importlib.util.spec_from_file_location("metadata", ROOT / "scripts/generate-skill-metadata.py")
metadata = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metadata)

absorb = (SKILLS / "absorb/SKILL.md").read_text()
reorder = (SKILLS / "reorder/SKILL.md").read_text()
policy = (SKILLS / "reorder/CHANGE-POLICY.md").read_text()
review = (SKILLS / "pre-pr-review/SKILL.md").read_text()

for name in ("absorb", "reorder"):
    path = SKILLS / name / "SKILL.md"
    fields = metadata.read_frontmatter(path)
    assert fields["name"] == name
    assert fields.get("disable-model-invocation") != "true"
    assert "CHANGE-POLICY.md" in path.read_text()
    for target in re.findall(r"\]\(([^)]+\.md)(?:#[^)]*)?\)", path.read_text()):
        assert (path.parent / target).is_file(), target

# The API and common recovery policy have one owner.
for document in (absorb, reorder):
    assert "api.typesafe.ai/v1/systemone" not in document
    assert "0.80" not in document
assert "There is no confidence threshold" in policy
assert "Reuse handed-off owners" in policy
assert "there is no LLM-only fallback" in policy
assert "pending/out-of-scope work" in policy

assert "gt absorb --dry-run" in absorb
assert "Invoke the installed `reorder` skill" in absorb
assert "Do not implement an amend/create/reorder fallback" in absorb
assert "whole-stack\nredesign or cleanup" in absorb
assert "## From absorb" in reorder and "## Whole stack" in reorder
assert "the priority menu and a second approval prompt" in reorder
assert "Do not ask for a second approval" in reorder
assert "Do not call `absorb` back" in reorder
assert "`reorder` skill in Whole stack mode" in review
assert "`graphite` skill" not in review
assert not (SKILLS / "graphite").exists()
manifest = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
assert "./skills/engineering/reorder" in manifest["skills"]
assert "./skills/engineering/graphite" not in manifest["skills"]
print("PASS: shared policy, bounded handoff, whole-stack gate, caller, rename, and links")
