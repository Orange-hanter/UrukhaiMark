# Troubleshooting

| Симптом | Вероятная причина | Решение |
|---------|-------------------|---------|
| GTIN не найден / не синхронизирован | Нет в ePASS или каталоге | ePASS → `/items` → повтор |
| code 4001 Business entity not found | Неверный UNP/GLN | Проверить регистрацию |
| Нет криптохвоста при скане | HID-сканер без GS | COM-режим; Notepad++ |
| КМ ломается после копирования | Excel/Блокнот удалил GS | Только API path |
| addManufacture rejected | status ≠ 47/50 | Сначала addMark |
| ships rejected | Нет addManufacture | Полная цепочка reports |
| DataMatrix не читается | QR вместо DM / нет FNC1 | [datamatrix-spec.md](datamatrix-spec.md) |
| Token expired | TTL ~20 мин | Auto-refresh auth |
| Пиво в РФ — нет кодов datamark | Нет решения ЕЭК | Контрагент РФ / CRPT |
| Отгрузка > 30k KM | Лимит ЕАЭС | Разбить на несколько ships |
| Разные группы в одной отгрузке | Ограничение API | Одна group на ship |

## Диагностика GS-разделителей

1. Скачать КМ через API
2. Открыть в Notepad++ → View → Show Symbol → Show All Characters
3. Убедиться в наличии `GS` (0x1D) перед AI 91 и 92

## Проверка DataMatrix

1. Мобильное приложение «Электронный знак»
2. `POST /v2/labels` — валидация в API
3. Golden test PNG vs эталон

## Контакты поддержки

- support@datamark.by
- @datamarkby
- [kb.belblank.by](https://kb.belblank.by/)
