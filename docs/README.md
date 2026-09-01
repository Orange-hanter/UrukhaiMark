# Документация UrukhaiMark

> Каноническая документация self-hosted-системы маркировки для производителя РБ.

Документация организована по Diátaxis. Этот файл — единственный индекс.

## Быстрый старт

1. [Глоссарий](reference/glossary.md).
2. [Матрица товаров](reference/product-matrix.md).
3. [Регистрация](tutorials/registration.md).
4. [Экспорт cosmetics в РФ](how-to/export-rf-cosmetics.md).
5. [Итоговая архитектура](explanation/architecture.md).
6. [Дорожная карта](planning/roadmap.md).

## Tutorials

| Документ | Назначение |
|----------|------------|
| [registration.md](tutorials/registration.md) | GS1, ePASS и «Электронный знак» |

## How-to

| Документ | Назначение |
|----------|------------|
| [export-rf-cosmetics.md](how-to/export-rf-cosmetics.md) | MVP cosmetics → РФ |
| [domestic-rb-beer.md](how-to/domestic-rb-beer.md) | UKZ для пива РБ |
| [quality-control.md](how-to/quality-control.md) | Проверка DataMatrix и grade |
| [operations-runbook.md](how-to/operations-runbook.md) | Ежедневные операции |
| [deployment.md](how-to/deployment.md) | Self-hosted deployment/rollback |
| [troubleshooting.md](how-to/troubleshooting.md) | Диагностика ошибок |

## Reference

| Документ | Источник истины |
|----------|-----------------|
| [glossary.md](reference/glossary.md) | Термины |
| [product-matrix.md](reference/product-matrix.md) | SKU → pipeline |
| [regulatory.md](reference/regulatory.md) | Нормативная база |
| [datamatrix-spec.md](reference/datamatrix-spec.md) | GS1 DataMatrix |
| [data-model.md](reference/data-model.md) | PostgreSQL schema/invariants |
| [testing-plan.md](reference/testing-plan.md) | QA и acceptance |
| [api/reference.md](reference/api/reference.md) | API статусы и лимиты |
| [api/cookbook.md](reference/api/cookbook.md) | HTTP-примеры |

## Explanation

| Документ | Назначение |
|----------|------------|
| [architecture.md](explanation/architecture.md) | Каноническая целевая архитектура |
| [integration-plan.md](explanation/integration-plan.md) | Границы и контракты интеграций |
| [technology/README.md](explanation/technology/README.md) | Нанесение и оборудование |

## Planning

| Документ | Назначение |
|----------|------------|
| [roadmap.md](planning/roadmap.md) | Capability slices и gates |
| [architecture-validation.md](planning/architecture-validation.md) | Предположения, NFR, failure scenarios |
| [work-plan.md](planning/work-plan.md) | WBS/RACI |
| [open-questions.md](planning/open-questions.md) | Бизнес-блокеры |
| [governance.md](planning/governance.md) | Владение документами |
| [archive/](planning/archive/) | Исторические снимки, не канон |

## Decisions

[ADR index](decisions/README.md) содержит Proposed и Accepted решения.

## Статусы scope

- **MVP** — реализуется в Slice 1;
- **Next** — следующий capability после MVP;
- **Future** — требует отдельного gate;
- **Blocked** — отсутствует подтверждённый контракт или бизнес-вход.

В разговорной речи КМ называют «QR Честного знака», но символика — **GS1 DataMatrix**.
