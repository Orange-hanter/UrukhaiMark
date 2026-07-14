# Технология нанесения кодов маркировки

> Обзорные материалы по нанесению кодов на товары в контексте ГИС «Электронный знак» (РБ) и «Честный знак» (РФ).
> Обновлено: 14.07.2026

## Для кого

| Роль | С чего начать |
|------|---------------|
| Технолог / упаковка | **[Промышленное нанесение](industrial-marking.md)** → [Упаковка](packaging-carriers.md) |
| Владелец производства | [Обзор](overview.md) → [industrial-marking.md](industrial-marking.md) |
| IT / интегратор | [industrial-marking.md § интеграция](industrial-marking.md#интеграция-с-urukhamark-и-линией) → [equipment.md](equipment.md) |
| Пилот / малый цех | [application-methods.md](application-methods.md) (наклейки) |

## Навигация

| Документ | Содержание |
|----------|------------|
| **[industrial-marking.md](industrial-marking.md)** | **Inline: CIJ, лазер, VDP, print-and-apply, интеграция с PLC** |
| **[laser-engraving.md](laser-engraving.md)** | **Лазерная гравировка DataMatrix: режимы, материалы, линия** |
| [overview.md](overview.md) | Что такое «QR на товаре», виды маркировки, жизненный цикл |
| [application-methods.md](application-methods.md) | Кратко: пилотные наклейки, УКЗ |
| [packaging-carriers.md](packaging-carriers.md) | Зоны на аэрозолях, флаконах, коробах |
| [equipment.md](equipment.md) | Принтеры, сканеры, верификаторы, интеграция с линией |
| [quality-control.md](quality-control.md) | ISO 15415, приёмка партии, типичные дефекты |

## Связанные документы

- [datamatrix-spec.md](../datamatrix-spec.md) — формат GS1 DataMatrix, encoder
- [glossary.md](../glossary.md) — КМ, СИ, УКЗ, FNC1, GS
- [product-matrix.md](../product-matrix.md) — какой режим для вашего SKU
- [processes/export-rf-cosmetics.md](../processes/export-rf-cosmetics.md) — end-to-end для освежителей

## Важно

В разговорной речи коды называют **«QR Честного знака»**, но технический стандарт для средств идентификации (СИ) — **GS1 DataMatrix** (ECC 200). QR Code и DataMatrix **несовместимы**: сканер «Честного знака» не примет QR, сгенерированный обычным генератором.
