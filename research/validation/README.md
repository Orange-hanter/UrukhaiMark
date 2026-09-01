# Architecture validation spikes

Дата прогона: 2026-09-01.

| Spike | Результат | Следующий gate |
|-------|-----------|----------------|
| [01 — KM round-trip](01-km-roundtrip.md) | Partial pass | PostgreSQL + encoder |
| [02 — ZPL/FNC1/GS](02-zpl-print.md) | Blocked | Физический принтер |
| [03 — COM scanner](03-com-scanner.md) | Blocked | COM/VCP-сканер |
| [04 — datamark sandbox](04-datamark-sandbox.md) | Blocked | Credentials + GTIN + agent |
| [05 — code allocation](05-code-allocation.md) | Design pass | Реализация PostgreSQL test |
| [06 — edge deduplication](06-edge-deduplication.md) | Design pass | Durable replay prototype |

`Blocked` означает отсутствие необходимой внешней зависимости. Такие результаты
не разрешают соответствующий production gate.

