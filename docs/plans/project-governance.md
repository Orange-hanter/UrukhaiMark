# Управление проектом

> Governance, коммуникации, документооборот.

## 1. Артефакты проекта

| Артефакт | Владелец | Расположение |
|----------|----------|--------------|
| Roadmap | PO | docs/ROADMAP.md |
| Work plan | PO/Dev | docs/plans/work-plan.md |
| Architecture | Dev | docs/plans/architecture-plan.md |
| Integration | Dev | docs/plans/integration-plan.md |
| Product matrix | PO/Operator | docs/product-matrix.md |
| Open questions | PO | docs/open-questions.md |
| ADR | Dev | docs/plans/adr/ |
| Runbook | Operator | docs/plans/operations-runbook.md |

## 2. Жизненный цикл документа

```
Draft → Review → Approved → Living (update on change)
```

При изменении API datamark или регламентов — обновить:

- regulatory.md
- api/reference.md
- integration-plan.md

## 3. ADR (Architecture Decision Records)

Создавать ADR при решениях:

- Выбор стека (Python vs Node)
- Стратегия хранения KM
- CLI vs Web first
- Printer protocol

Шаблон: `docs/plans/adr/NNNN-title.md`

```markdown
# ADR-0001: Title
## Status: Proposed | Accepted | Deprecated
## Context
## Decision
## Consequences
```

## 4. Issue tracking (рекомендация)

| Label | Meaning |
|-------|---------|
| `P0` | Blocker |
| `compliance` | Regulatory/API |
| `gs-integrity` | Critical path |
| `enhancement` | Nice to have |

## 5. Release process

1. Feature complete → QA sandbox E2E
2. UAT sign-off (operator)
3. Version tag `v0.x.y`
4. Deploy prod per [deployment-plan.md](deployment-plan.md)
5. Release notes in CHANGELOG.md

## 6. Compliance review cadence

| Review | Frequency |
|--------|-----------|
| datamark API spec | Quarterly |
| Belblank kb / webinars | Monthly |
| Product matrix / TN VED | On new SKU |
| RF cosmetics calendar | Quarterly |
