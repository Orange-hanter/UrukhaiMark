# Матрица товарных групп

## Сводная таблица (целевые SKU)

| Товар | ТН ВЭД | Продажа в РБ | Экспорт в РФ | API group | label_type | DataMatrix |
|-------|--------|--------------|--------------|-----------|------------|------------|
| Пиво солодовое | 2203 | **УКЗ** | Через контрагента РФ | `ukz` | — | Нет на товаре |
| Освежители / аэрозоли | 3307* | Уточнить** | **СИ**, с 01.07.2025 | `cosmetics` | **7** | **Да** |
| Газовые баллоны (тех.) | 7311, 7613… | Не в перечне | TBD | — | — | — |

\* Кроме 3307 41 000 0, 3307 90 000 1, 3307 90 000 2  
\*\* Освежители 3307 не в перечне УКЗ РБ (моющие 3402 — с 01.10.2025). Запрос: support@datamark.by

## Product Router (логика приложения)

```
if product.group == "cosmetics" and destination == "RF":
    pipeline = EAEU(label_type=7)

elif product.tnved.startswith("2203"):
    if destination == "RB":
        pipeline = UKZ()
    elif destination == "RF":
        pipeline = CRPTViaPartner()  # datamark не выдаёт label_type=7

else:
    raise UnknownProductError
```

---

## Пиво (2203)

### Продажа в РБ

- Маркировка: **УКЗ**, не СИ
- Знаки: 17×18 мм (до 1 л), 17×34 мм (свыше 1 л)
- Коды бланков: 201659, 201660 (РБ), 202610–202666 (импорт)
- API: [спецификация УКЗ](https://datamark.by/wp-content/uploads/gis-markirovki-web-servis-mezhsistemnogo-vzaimodejstviya-speczifikacziya-api-markirovka-tovarov-unificirovannymi-kontrolnymi-znakami.pdf)
- Процесс: [domestic-rb-beer.md](processes/domestic-rb-beer.md)

### Экспорт в РФ

- **Блокер:** datamark.by не выдаёт коды российского образца для пива
- Решение ЕЭК по трансграничной маркировке пива **не принято**
- Рекомендация: коды у контрагента-резидента РФ через CRPT
- В РФ: поэкземплярный учёт с 01.12.2025
- Источник: [kb.belblank.by — пиво для экспорта](https://kb.belblank.by/kb/jelektronnyj-blank/obshhie-voprosy/kak-promarkirovat-pivo-dlja-jeksporta-na-territoriju-rf/)

---

## Освежители / аэрозоли (3307)

### Экспорт в РФ

- API: `group=cosmetics`, `label_type=7`
- ОКПД2: 20.42.16, 20.42.17, 20.42.19
- Аэрозольные баллончики — в перечне типов упаковки для DataMatrix
- Процесс: [export-rf-cosmetics.md](processes/export-rf-cosmetics.md)

### Документы при отгрузке в РФ

- Декларация о соответствии
- СГР / сертификат (по группе)

### Отчёт о производстве

- Дата производства (обязательно)
- Дата истечения срока годности (если применимо)

---

## Газовые баллоны

| Тип | Классификация | Действие |
|-----|---------------|----------|
| Аэрозоль-освежитель | 3307 | → cosmetics |
| Технический газ (пропан и т.п.) | 7311, 7613, 2706 | Консультация support@datamark.by |

---

## SKU tracker (заполнить)

| SKU | Наименование | ТН ВЭД | ОКПД2 | GTIN | Группа API | Режим РБ | Режим РФ |
|-----|--------------|--------|-------|------|------------|----------|----------|
| | | | | | | | |
| | | | | | | | |
