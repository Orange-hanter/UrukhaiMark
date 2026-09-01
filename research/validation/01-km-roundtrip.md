# Spike 01 — побайтовый round-trip КМ

## Цель

Доказать сохранность `0x1D` на пути bytes → JSON → bytes. Полная проверка требует
PostgreSQL и выбранного DataMatrix encoder.

## Выполненная проверка

```python
import json

source = b"010481001234567821SERIAL\x1d91KEY1\x1d92CRYPTO"
payload = json.dumps({"km": source.decode("utf-8")}, ensure_ascii=True)
restored = json.loads(payload)["km"].encode("utf-8")
assert restored == source
assert payload.count("\\u001d") == 2
```

Результат: **partial pass**. JSON round-trip сохраняет оба GS. Не проверены
PostgreSQL `BYTEA`, драйвер БД и итоговый encoder; они остаются обязательным P0-тестом.
