# API Reference — datamark.by

Спецификация: [PDF rev. 4.24](https://datamark.by/wp-content/uploads/gis-markirovki-web-servis-mezhsistemnogo-vzaimodejstviya-speczifikacziya-api-markirovka-i-oborot-tovarov.pdf)

## Подключение

| Параметр | Значение |
|----------|----------|
| Encoding | UTF-8 |
| Protocol | HTTPS |
| Methods | GET, POST, PUT |
| Auth | Header `Token` (кроме `/auth`) |

## Группы endpoints

| Prefix | Назначение |
|--------|------------|
| `/auth`, `/users` | Авторизация, поверенные |
| `/catalogs`, `/items` | Каталог GTIN |
| `/orders`, `/v3/orders` | Заказ кодов |
| `/labels` | Типы, валидация, агрегация, списание |
| `/reports`, `/v3/reports` | Отчёты |
| `/ships`, `/v3/ships` | Отгрузки |
| `/contracts` | Контрагенты |
| `/directories` | Справочники |
| `/downloads` | Файлы |

API v3: префикс `/v3/` в URL.

## label_type

| id | Название | method | Использование |
|----|----------|--------|---------------|
| **7** | Код стран ЕАЭС | km | Экспорт в РФ |
| 6 | SSCC агрегация | sscc | Короба/паллеты |
| 12 | Код РБ молоко | nobsomilk | РБ |
| 13 | Собственный КА | — | addAggregate |
| **20** | Код РБ (обувь/шины/лёгкая) | km_rb | РБ |
| 19 | Знак защиты | — | destroy |

Полный список: `GET /labels/types`

## Товарные группы (group)

| code | Название |
|------|----------|
| `cosmetics` | Косметика и бытовая химия |
| `ukz` | УКЗ |
| `juice` | Безалкогольные напитки |
| `milk` | Молочная продукция |
| `shoes` | Обувь |
| … | См. табл. 4.2.1.2 в PDF |

## Лимиты

| Операция | Лимит |
|----------|-------|
| Заказ кодов | ≤ 1000 / заказ |
| Отчёт производства | ≤ 10 000 КМ |
| Отгрузка в ЕАЭС | ≤ 30 000 КМ |
| Отгрузка (прочее) | ≤ 100 000 КМ |
| Token TTL | ~20 мин |

## Статусы СИ

| code | Статус | Следующий шаг |
|------|--------|---------------|
| 47 | Нанесён | addManufacture |
| 50 | Промаркирован | addManufacture |
| — | Экспортирован в ЕАЭС | Приёмка в РФ |

## Экранирование GS

В JSON КМ передаются с `\u001d` (ASCII 29). UrukhaiMark must preserve on store and forward.

## UKZ API (отдельный документ)

[API маркировка УКЗ PDF](https://datamark.by/wp-content/uploads/gis-markirovki-web-servis-mezhsistemnogo-vzaimodejstviya-speczifikacziya-api-markirovka-tovarov-unificirovannymi-kontrolnymi-znakami.pdf)

## CRPT True API (РФ, пиво)

[docs.crpt.ru/gismt/True_API](https://docs.crpt.ru/gismt/True_API/) — отдельная интеграция, не datamark.by.

## Поддержка

- support@datamark.by
- @datamarkby
- [kb.belblank.by](https://kb.belblank.by/)
