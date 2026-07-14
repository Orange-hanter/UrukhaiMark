# Документация UrukhaiMark

> Маркировка товаров через ГИС «Электронный знак» (Беларусь) для продажи в РБ и экспорта в РФ.
> Обновлено: 14.07.2026

## Быстрый старт

1. Прочитайте [глоссарий](glossary.md) — термины КМ, СИ, УКЗ, DataMatrix.
2. Определите режим для вашего SKU в [матрице товаров](product-matrix.md).
3. Пройдите [чеклист регистрации](processes/registration.md).
4. Для освежителей → РФ: [процесс экспорта](processes/export-rf-cosmetics.md).
5. Для разработки: [дорожная карта](ROADMAP.md) + [архитектура](architecture.md).

## Навигация

### Планирование

- [ROADMAP.md](ROADMAP.md) — дорожная карта проекта
- [plan.md](plan.md) — сохранённый мастер-план (полная сводка)
- [open-questions.md](open-questions.md) — открытые вопросы бизнеса

### Предметная область

- [glossary.md](glossary.md) — термины и сокращения
- [regulatory.md](regulatory.md) — нормативная база и календари
- [product-matrix.md](product-matrix.md) — товарные группы и label_type

### Процессы

- [processes/registration.md](processes/registration.md) — регистрация GS1, ePASS, «Электронный знак»
- [processes/export-rf-cosmetics.md](processes/export-rf-cosmetics.md) — экспорт освежителей в РФ
- [processes/domestic-rb-beer.md](processes/domestic-rb-beer.md) — пиво в РБ (УКЗ)

### Технология нанесения кодов

- [technology/README.md](technology/README.md) — индекс обзорных материалов
- [technology/industrial-marking.md](technology/industrial-marking.md) — **промышленное нанесение**: CIJ, лазер, VDP, print-and-apply, PLC
- [technology/laser-engraving.md](technology/laser-engraving.md) — **лазерная гравировка** DataMatrix на металле и полимерах
- [technology/overview.md](technology/overview.md) — «QR» vs DataMatrix, виды маркировки, жизненный цикл
- [technology/application-methods.md](technology/application-methods.md) — пилотные наклейки, УКЗ
- [technology/packaging-carriers.md](technology/packaging-carriers.md) — размещение на аэрозолях, флаконах, коробах
- [technology/equipment.md](technology/equipment.md) — принтеры, сканеры, верификаторы
- [technology/quality-control.md](technology/quality-control.md) — ISO 15415, приёмка партии, брак

### Техническая реализация

- [datamatrix-spec.md](datamatrix-spec.md) — GS1 DataMatrix, encoder, сканеры
- [api/cookbook.md](api/cookbook.md) — примеры HTTP-запросов
- [api/reference.md](api/reference.md) — endpoints, label_type, лимиты, статусы
- [architecture.md](architecture.md) — модули UrukhaiMark, стек, Product Router
- [troubleshooting.md](troubleshooting.md) — частые ошибки

## Важно

В разговорной речи коды называют «QR Честного знака», но **стандарт — GS1 DataMatrix**, не QR Code.
