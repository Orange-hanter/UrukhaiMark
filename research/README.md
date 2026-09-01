# Research notes

Рабочие материалы и spike-логи. **Не канон** продуктовой документации —
канон живёт в [`docs/`](../docs/README.md). Уровень доверия черновиков —
Probable/Unknown по [architecture-validation.md](../docs/planning/architecture-validation.md).

## Validation spikes (канон журнала)

Актуальный журнал прогонов architecture validation:
[`validation/README.md`](validation/README.md). Связан с
[`docs/planning/architecture-validation.md`](../docs/planning/architecture-validation.md).

## Черновики по оборудованию и архитектуре маркировки

| Файл | Содержание | Связь с планом / каноном |
|------|------------|--------------------------|
| [marking-line-equipment.md](marking-line-equipment.md) | Рынок inline-оборудования: единица → короб → палета | **Slice 3+** (inline). § «минимальный вариант TIJ/CIJ» — **не** путь MVP: канон — настольный термотрансфер 300 dpi, см. [equipment.md](../docs/explanation/technology/equipment.md) |
| [chestny-znak-marking-architecture.md](chestny-znak-marking-architecture.md) | L1/L2/L3, СУЗ, РЭ — нативная архитектура **ГИС МТ/ЦРПТ** | Контекст приёмки в РФ и Slice 7; **не** topology MVP UrukhaiMark (datamark.by → `/v3/ships/add`, см. [integration-plan.md](../docs/explanation/integration-plan.md)) |
| [Marking_Line_Equipment.bento.html](Marking_Line_Equipment.bento.html) | Bento-обзор (визуализация к `marking-line-equipment.md`) | То же назначение, что markdown-черновик |

**Канон UrukhaiMark:** [equipment.md](../docs/explanation/technology/equipment.md) · [industrial-marking.md](../docs/explanation/technology/industrial-marking.md) · [roadmap.md](../docs/planning/roadmap.md) · [obsidian-kb.md](../docs/reference/obsidian-kb.md)
