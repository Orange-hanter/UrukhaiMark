# Пиво в РБ — маркировка УКЗ

Пиво (ТН ВЭД 2203) на территории Беларуси маркируется **унифицированными контрольными знаками (УКЗ)**, не GS1 DataMatrix на упаковке товара.

## Когда применяется

- Пиво солодовое, разлитое в упаковку любой вместимости
- Безалкогольное пиво (2202 91 000 0) — с 01.10.2025

## Форматы знаков

| Объём | Размер знака | Коды бланков (примеры) |
|-------|--------------|------------------------|
| до 1 л | 17×18 мм | 201659, 202610 |
| св. 1 л | 17×34 мм | 201660, 202611 |

## Процесс

| # | Шаг |
|---|-----|
| 1 | Регистрация в «Электронном знаке», группа `ukz` |
| 2 | Заказ УКЗ (ЛК или [API УКЗ](https://datamark.by/wp-content/uploads/gis-markirovki-web-servis-mezhsistemnogo-vzaimodejstviya-speczifikacziya-api-markirovka-tovarov-unificirovannymi-kontrolnymi-znakami.pdf)) |
| 3 | Нанесение знака на упаковку |
| 4 | Передача сведений о маркировке **до** оборота |
| 5 | Оборот: ТТН/эТТН (объёмно-сортовой учёт) |

## UrukhaiMark — модуль beer-ukz (Фаза 3)

- Заказ знаков по объёму упаковки
- Учёт серии/номера бланка
- Статус: использован / списан
- **Не** использовать label_type=7 и DataMatrix encoder

## Экспорт пива в РФ

Datamark **не выдаёт** коды российского образца для пива.

- Коды — у контрагента-резидента РФ (CRPT)
- См. [product-matrix.md](../product-matrix.md)

Источник: [kb.belblank.by — пиво для экспорта](https://kb.belblank.by/kb/jelektronnyj-blank/obshhie-voprosy/kak-promarkirovat-pivo-dlja-jeksporta-na-territoriju-rf/)

## См. также

- [markirovka-ukz на datamark.by](https://datamark.by/markirovka-ukz/)
