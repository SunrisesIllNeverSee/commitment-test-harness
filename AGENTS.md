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
