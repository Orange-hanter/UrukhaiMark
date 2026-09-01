# GS1 DataMatrix — спецификация для UrukhaiMark

## Формат кода маркировки (КМ)

```
[FNC1] 01{GTIN14} 21{Serial} [GS] 91{Key4} [GS] 92{Crypto44}
```

- **КМ** = КИ (31 символ) + криптохвост
- **FNC1** — ASCII 232, добавляется генератором штрихкода
- **GS** — ASCII 29, в JSON API: `\u001d`

## Блоки данных

| AI | Содержание | Длина |
|----|------------|-------|
| 01 | GTIN | 14 цифр |
| 21 | Серийный номер | до 13 символов |
| 91 | Ключ проверки | 4 символа |
| 92 | Криптоподпись | 44 символа |

## Правила кодирования

| # | Правило |
|---|---------|
| 1 | Первый символ — FNC1, не строка «FNC1» |
| 2 | GS после serial, перед 91 и 92 |
| 3 | GS **не** после GTIN (фиксированная длина 01) |
| 4 | Символика ECC 200, **не QR** |
| 5 | Качество печати ≥ 1.5 (C) ISO/IEC 15415 |

## Алгоритм encoder (UrukhaiMark)

```
Input:  KM from API (with \u001d)
1. Validate AI 01, 21, 91, 92
2. Preserve GS separators — never strip
3. Encode with FNC1 prefix (libdmtx / zxing-cpp)
4. Output: PNG/SVG (UI), ZPL/EPL (printer)
5. Optional: POST /v2/labels validation
6. Persist: km_hash, gtin, serial, order_id, printed_at
```

## Типичные ошибки генерации

| Ошибка | Последствие |
|--------|-------------|
| QR вместо DataMatrix | Код не принимается |
| Текст «FNC1» вместо символа | Сканер не видит GS1 |
| Потеря GS | «Нет криптохвоста» |
| GS после GTIN | Неверный парсинг |

## Сканеры

| Режим | GS передаётся | Рекомендация |
|-------|---------------|--------------|
| HID (клавиатура) | Часто нет | Не для верификации КМ |
| COM/Serial | Да | **Рекомендуется** |

Проверка: мобильное приложение «Электронный знак» ([datamark.by](https://datamark.by/)).

## Работа с файлами КМ

- Скачивать только через API или ЛК
- **Не** открывать в Excel — GS удаляется
- Для просмотра: Notepad++ с отображением control characters

## Стандарты

- ISO/IEC 16022 (Data Matrix)
- ISO/IEC 15415 (качество печати)
- GS1 General Specifications
- [kb.belblank.by — GS1 DataMatrix](https://kb.belblank.by/kb/jelektronnyj-znak/kod-markirovki-i-sredstvo-identifikacii/shtrih-kod-markirovki-gs1-datamatrix-kak-on-vygljadit-i-rabotaet-chto-nuzhno-znat/)

## Тесты (Фаза 5)

- `tests/fixtures/km-samples.txt` — эталонные КМ с GS
- `tests/datamatrix-golden/` — эталонные PNG для regression
