# Управление проектом

> Governance, коммуникации, документооборот.

## 1. Артефакты проекта

Полный индекс — [docs/README.md](../README.md).

| Артефакт | Владелец | Расположение |
|----------|----------|--------------|
| Roadmap | PO | [planning/roadmap.md](roadmap.md) |
| Architecture validation | PO/Dev | [planning/architecture-validation.md](architecture-validation.md) |
| Work plan | PO/Dev | [planning/work-plan.md](work-plan.md) |
| Architecture | Dev | [explanation/architecture.md](../explanation/architecture.md) |
| Integration | Dev | [explanation/integration-plan.md](../explanation/integration-plan.md) |
| Product matrix | PO/Operator | [reference/product-matrix.md](../reference/product-matrix.md) |
| Open questions | PO | [planning/open-questions.md](open-questions.md) |
| ADR | Dev | [decisions/](../decisions/README.md) |
| Runbook | Operator | [how-to/operations-runbook.md](../how-to/operations-runbook.md) |

## 2. Жизненный цикл документа

```
Draft → Review → Approved → Living (update on change)
```

При изменении API datamark или регламентов — обновить:

- [reference/regulatory.md](../reference/regulatory.md)
- [reference/api/reference.md](../reference/api/reference.md)
- [explanation/integration-plan.md](../explanation/integration-plan.md)

## 3. ADR (Architecture Decision Records)

Создавать ADR при решениях:

- Выбор стека (Python vs Node)
- Стратегия хранения KM
- CLI vs Web first
- Printer protocol

Шаблон и реестр: [docs/decisions/README.md](../decisions/README.md).

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
4. Deploy prod per [deployment.md](../how-to/deployment.md)
5. Release notes in CHANGELOG.md

## 6. Compliance review cadence

| Review | Frequency |
|--------|-----------|
| datamark API spec | Quarterly |
| Belblank kb / webinars | Monthly |
| Product matrix / TN VED | On new SKU |
| RF cosmetics calendar | Quarterly |
