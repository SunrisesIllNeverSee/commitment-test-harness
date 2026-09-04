# AGENTS.md — Commitment Test Harness

> Research-grade prototype for testing commitment conservation under compression and recursion.

## What this is

Prototype implementation of the falsification protocol described in
*"A Conservation Law for Commitment in Language Under Transformative
Compression and Recursive Application"* (McHenry, 2026).

Early-stage, illustrative tooling. Tests the hypothesis that linguistic
signals contain a conserved structure (hard commitments) that remains
invariant under lossy compression until a sharp collapse threshold.

## Operating notes

- Python project (pyproject.toml, requirements.txt, environment.yml)
- CI: `.github/workflows/ci.yaml` (pytest)
- Tracked externally by ello-repo-control's catalog
- For canon context, load Search Authority conservation_law context before
  modifying research claims or methodology

## stickypads — check the shared board

Before starting work, check the shared operational board for tasks assigned
to you or this repo:

```bash
python3 ~/Developer/_control/stickypads/scripts/check_in.py --agent <your-name>
```

Or clone the ello-ops repo and run from there. The board has:
- TODOs across all repos
- Memos/notes from other agents and the owner
- Current session state

If you discover work that can't be completed immediately, create a task or
drop a note:

```bash
# Create a formal task
python3 ~/Developer/_control/stickypads/scripts/create_task.py \
    --title "Specific actionable title" \
    --project <this-repo-name> \
    --owner <your-name>

# Drop a quick memo (no format required)
python3 ~/Developer/_control/stickypads/scripts/drop.py \
    --from <this-repo-name> \
    "Quick note about what needs attention"
```

At session end or meaningful completion, reconcile this repo's coord kit
state into stickypads:

```bash
python3 ~/Developer/_control/stickypads/scripts/reconcile_coord.py \
    --repo-path . --dry-run
```
