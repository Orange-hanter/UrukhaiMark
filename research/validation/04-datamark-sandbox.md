# Spike 04 — datamark sandbox E2E

## Результат

**Blocked:** отсутствуют sandbox credentials, подтверждённый GTIN и `agent`
контрагента. Запросы к API намеренно не выполнялись.

## Обязательный прогон

`order(label_type=7) → poll status=30 → download → addMark → status 47/50 → addManufacture → ships(country=643)`

Сохраняются request correlation ID, внешний ID, HTTP status, хеш payload и квитанция.
Полные КМ и credentials в отчёт не попадают. Повтор каждого шага проверяется отдельно
на отсутствие дублирования.
