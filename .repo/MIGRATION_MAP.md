# Migration Map — commitment-test-harness

**Installed:** 2026-08-19
**Mode:** migrate
**Profile:** experiment

## Existing structure preserved

All existing root directories declared in `allowed_root_dirs_extra`:
- `data/` — test data (added to artifact_roots)
- `diagrams/` — diagrams (added to artifact_roots)
- `notebooks/` — Jupyter notebooks
- `paper_sections/` — paper section source (added to document_roots)
- `src/` — harness source code
- `tests/` — test suite

All existing root files declared in `allowed_root_files_extra`:
- `appendix_a_extractor.md`, `debug_extraction.py`, `environment.yml`,
  `Harnesstest.ini`, `quick_test.py`

## Special handling

- Preserve experimental/test provenance — do not convert test outputs into ordinary docs
- Test data and results are artifacts, not canonical documentation

## Canon context

- Authority role: `evidence_source`
- Canon contexts: `commitment-theory`, `conservation_law`
- Authority owner: `search_authority`

## Migration steps (before enforce)

1. [ ] Run `repo_check.py --ci` until clean (currently clean)
2. [ ] Verify GitHub ruleset application (solo-fast)
3. [ ] Switch REPO.yaml mode from `migrate` → `enforce`

## Enforce readiness

Ready after ruleset verification — no structural defects.
