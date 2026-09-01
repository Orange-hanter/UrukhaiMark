# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

**Documentation-only, greenfield.** There is no `src/`, no package manifest, no application build/test tooling yet — only Markdown docs. The `src/` and `tests/` layouts described in `docs/explanation/architecture.md` are a *plan*, not existing code. Do not assume any code exists until you've checked; when asked to "implement" something, expect to be scaffolding from scratch per `docs/planning/work-plan.md`.

There are no application build/test commands. The repo does have docs-as-code tooling (see "Docs tooling" below) — that's the only thing `.github/workflows/docs-lint.yml` runs.

## What UrukhaiMark is

A system for Belarusian manufacturers/exporters to automate the full product-marking (маркировка) lifecycle:

1. Order marking codes via the `datamark.by` API (ГИС «Электронный знак»)
2. Generate GS1 DataMatrix barcodes and print labels
3. File compliance reports (marking, manufacture)
4. Report shipments to Russia's «Честный знак» (ГИС МТ, operator ЦРПТ)

All documentation and domain content is written in **Russian** — match that when editing or adding docs.

## Critical domain facts (get these wrong and the whole pipeline breaks)

- **GS1 DataMatrix, not QR.** Colloquially people call these codes "QR Честного знака," but the actual standard is GS1 DataMatrix (ECC 200). The formats are incompatible — never treat them as interchangeable. See `docs/reference/datamatrix-spec.md`.
- **GS separators (Group Separator, ASCII 29, `\u001d`) must never be lost.** The КМ (marking code) format is `[FNC1] 01{GTIN14} 21{Serial} [GS] 91{Key4} [GS] 92{Crypto44}`. Opening a КМ file in Excel strips the GS bytes and corrupts it — codes must only be handled through the API/DB path, never through Excel/CSV. This is called out as a high-probability risk in `docs/planning/roadmap.md`.
- **`label_type` and product group drive the pipeline.** Product routing is TN VED (ТН ВЭД) code + destination country, not something inferred loosely — see the Product Router in `docs/explanation/architecture.md` and `docs/reference/product-matrix.md`. Aerosols/cosmetics (TN VED 3307) → `group=cosmetics`, `label_type=7`, export to RF. Beer (TN VED 2203) → УКЗ (a physical stamp, *not* a DataMatrix code) for domestic RB sale; RF export for beer is currently blocked (no `label_type=7` from datamark.by — needs an RF-resident partner via CRPT/True API).
- **Compliance report ordering is strict**: `addMark` → `addManufacture` → `ships`, gated on status codes (30 for order readiness, 47/50 before manufacture reporting).

## Documentation structure

Entry point: `docs/README.md` (full navigation index). Docs are organized per [Diátaxis](https://diataxis.fr/) — one file, one function — plus two non-Diátaxis trees for project management. When adding a new doc, put it in the quadrant matching its function rather than wherever feels convenient, and don't restate facts that already live in `reference/`; link to them instead.

- `docs/tutorials/` — onboarding, learn-by-doing. Currently just `registration.md` (GS1/ePASS/datamark signup checklist).
- `docs/how-to/` — task-oriented guides: `export-rf-cosmetics.md`, `domestic-rb-beer.md`, `quality-control.md` (canonical "check first three labels" procedure — other docs link here instead of restating it), `operations-runbook.md`, `deployment.md`, `troubleshooting.md`.
- `docs/reference/` — lookup data, source of truth for shared constants (grade threshold, API limits, support contacts): `glossary.md`, `product-matrix.md`, `regulatory.md`, `datamatrix-spec.md`, `data-model.md`, `testing-plan.md`, `api/cookbook.md` + `api/reference.md`, plus `obsidian-kb.md` (index of related personal Obsidian notes — not a substitute for in-repo reference).
- `docs/explanation/` — architecture and domain context: `architecture.md` (canonical target architecture — C4, domains, principles P1–P8, evolution), `integration-plan.md`, `technology/` (physical code-application methods — see `technology/README.md`).
- `docs/decisions/` — ADR. **Once a decision reaches `Accepted`, its Context/Decision text is never edited retroactively** — a changed decision gets a new `NNNN-title.md` file, and the old one's `Status` line becomes `Superseded by ADR-NNNN`. Current: ADR-0001…0003 `Proposed`; ADR-0004 (deployment topology) and ADR-0005 (KM storage) `Accepted`. Process detail in `decisions/README.md`.
- `docs/planning/` — project management, not Diátaxis: `roadmap.md` (sole source of capability slices 0–7 and gates), `architecture-validation.md` (assumptions/NFR/spikes), `work-plan.md`, `governance.md`, `open-questions.md`. `planning/archive/` holds frozen historical snapshots — same "don't edit, supersede" discipline as ADRs.
- `research/` — working notes and validation spike logs (`research/validation/`); not part of the Diátaxis product docs index unless promoted into `docs/`.

## Docs tooling

`.markdownlint-cli2.jsonc` + `scripts/check_markdown_links.py` + `.github/workflows/docs-lint.yml` run markdown lint and relative-link checking in CI on every push/PR touching `**/*.md`. See `CONTRIBUTING.md` for local-check commands and the review workflow. `llms.txt` at the repo root is a separate, publicly-oriented machine-readable doc index (llmstxt.org format) — update it when adding/removing/renaming a doc file, independently of this file.

## License

CC BY 4.0 (not MIT) — attribution is required per the block in `README.md`. Keep the SPDX identifier and license text consistent with `LICENSE` when touching licensing-related content.
