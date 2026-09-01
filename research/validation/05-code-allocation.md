# Spike 05 — конкурентное резервирование КМ

## Результат

**Design pass:** выбран атомарный PostgreSQL-паттерн. Runtime-проверка входит в
реализацию persistence layer.

```sql
WITH candidates AS (
  SELECT id
  FROM marking_codes
  WHERE lifecycle_status = 'available'
  ORDER BY id
  FOR UPDATE SKIP LOCKED
  LIMIT :count
)
UPDATE marking_codes AS mc
SET lifecycle_status = 'allocated'
FROM candidates
WHERE mc.id = candidates.id
RETURNING mc.id;
```

Allocation создаётся в той же транзакции; уникальный индекс разрешает не более
одной активной аренды на КМ. Выдача линии происходит только после commit.

## Acceptance

Два параллельных клиента резервируют непересекающиеся множества; rollback возвращает
КМ в доступный пул; истечение lease не переиспользует КМ с подтверждённой печатью.

