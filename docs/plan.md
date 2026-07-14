# Мастер-план: маркировка из Беларуси

> Сохранённая сводка исследования для UrukhaiMark.  
> Дата: 11.07.2026  
> Детализированная документация разнесена по каталогу [`docs/`](README.md).

## Executive summary

UrukhaiMark автоматизирует маркировку через ГИС **«Электронный знак»** (datamark.by): заказ кодов, **GS1 DataMatrix** (не QR), отчёты и отгрузки в РФ.

| Товар | MVP через datamark | Приоритет |
|-------|-------------------|-----------|
| Освежители → РФ | `cosmetics`, label_type=**7** | **P0** |
| Пиво → РБ | УКЗ (отдельный API) | P2 |
| Пиво → РФ | **Блокер** — коды через контрагента РФ | P3 |

## Карта документации

| Раздел мастер-плана | Файл |
|---------------------|------|
| §1 Глоссарий | [glossary.md](glossary.md) |
| §2 Нормативная база, календари, стоимость | [regulatory.md](regulatory.md) |
| §3–4 Архитектура систем, матрица товаров | [product-matrix.md](product-matrix.md), [architecture.md](architecture.md) |
| §5 Календарь РФ (cosmetics) | [regulatory.md](regulatory.md) |
| §6 Процессы | [processes/](processes/) |
| §7 DataMatrix | [datamatrix-spec.md](datamatrix-spec.md) |
| §8–9 API, статусы СИ | [api/](api/) |
| §10 Стоимость | [regulatory.md](regulatory.md) |
| §11 Архитектура приложения | [architecture.md](architecture.md) |
| §12 Troubleshooting | [troubleshooting.md](troubleshooting.md) |
| §13 Трансграничный обмен | [processes/export-rf-cosmetics.md](processes/export-rf-cosmetics.md) |
| §14 Контакты | [regulatory.md](regulatory.md), [api/reference.md](api/reference.md) |
| §15 Дорожная карта | [ROADMAP.md](ROADMAP.md) |
| §16 Открытые вопросы | [open-questions.md](open-questions.md) |

## Ключевые решения

1. **Формат:** GS1 DataMatrix (ECC 200, FNC1 + GS `\u001d`), не QR.
2. **Экспорт в РФ:** label_type=7, цепочка mark → manufacture → ship.
3. **Пиво в РФ:** datamark не выдаёт коды; нужен партнёр + CRPT.
4. **Запас кодов:** ≥ 7 дней производства.

## Следующий шаг

[ROADMAP.md — Фаза 0](ROADMAP.md#фаза-0--подготовка-12-недели): регистрация, sandbox API, классификация SKU.

## Источник

Исходный plan-файл Cursor: `.cursor/plans/маркировка_чз_by_e6c4668a.plan.md`
