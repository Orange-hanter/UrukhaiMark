# Architecture Decision Records

ADR фиксирует архитектурное решение **снимком на момент принятия**. После
`Accepted` разделы Context/Decision не переписываются: пересмотр оформляется
новым ADR, старый получает `Superseded by ADR-NNNN`.

## Статусы

```
Proposed → Accepted → (остаётся Accepted, пока действует)
                    ↘ Superseded by ADR-XXXX  (если решение пересмотрено)
                    ↘ Deprecated              (если решение отменено без замены)
```

**Правило неизменности:** после `Accepted` секции `Context` и `Decision` не
редактируются задним числом. Если решение нужно изменить:

1. Создайте новый файл `NNNN-short-title.md` со следующим порядковым номером.
2. Новый ADR получает `Status: Accepted` и ссылается на предыдущий в `Context`.
3. У старого ADR меняется **только строка Status** → `Superseded by ADR-NNNN`.

То же правило действует для архива планирования: см. [planning/archive/](../planning/archive/).

## Реестр

| ID | Решение | Статус |
|----|---------|--------|
| [ADR-0001](0001-backend-stack.md) | Backend runtime | Proposed |
| [ADR-0002](0002-ui-surface.md) | CLI-first или Web-first | Proposed |
| [ADR-0003](0003-label-format.md) | ZPL или PDF по умолчанию | Proposed |
| [ADR-0004](0004-deployment-topology.md) | Modular monolith + edge-ready | Accepted |
| [ADR-0005](0005-km-storage.md) | Binary-safe KM storage | Accepted |

## Шаблон

```markdown
# ADR-NNNN: Title

## Status

Proposed | Accepted | Deprecated | Superseded by ADR-NNNN

## Date

YYYY-MM-DD

## Context

## Decision

## Consequences
```
