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


## Filesystem MCP — REQUIRED for file operations

This is a core framework/search/ello/product repository. When performing
file operations, prefer the Filesystem MCP tools over ad-hoc shell commands:

- `list_directory` / `directory_tree` — structured directory traversal
- `search_files` — glob-pattern file search within allowed paths
- `read_multiple_files` — batch file reads (failures do not stop the batch)
- `edit_file` with `dryRun: true` — preview structural changes before applying

Allowed paths: ~/Developer, ~/.config/devin, ~/.config/sigrank, ~/Desktop

For single-file reads and edits, native tools are acceptable. For multi-file
operations, directory exploration, and structural changes, use the Filesystem MCP.


## Context7 MCP — SUGGESTED for library code

When writing code that uses external library APIs, consider querying Context7
to verify current patterns instead of relying on training data:

1. resolve-library-id — find the library
2. query-docs — ask the specific question

Supported libraries include Cloudflare Workers, Supabase, Next.js, Hono,
Playwright, Pydantic, Python, and more.


## MCP Server Recommendations for This Repo

Full index: `Moses_Enterprise_B2BPilot_/_workspace/MCP_INDEX.md`

**Primary (use regularly):**
- `ds-server` — Plotly charts for test harness results visualization
- `context7` — verify Python/library patterns before writing test code
- `repomix` — pack test harness code for handoffs

**Secondary (use as needed):**
- `brave-search` — research commitment theory test methodologies
- `knowledge-graph` — map commitment classes and conservation law relationships

**Not needed here:**
- `supabase` / `vercel` / `posthog` / `gsc-seo-*` — not a deployed product
- `blender` / `worldmonitor` — unrelated
