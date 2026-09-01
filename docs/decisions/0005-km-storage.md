# ADR-0005: Бинарно-безопасное хранение КМ

## Status

Accepted

## Date

2026-09-01

## Context

КМ содержит управляющий GS `0x1D`. Текстовые экспорты, trim/normalization и неверное
экранирование способны незаметно повредить код. База должна хранить каноническое
представление независимо от runtime и JSON serializer.

## Decision

Хранить канонический `km_raw` в PostgreSQL `BYTEA`. SHA-256 вычисляется по точным
байтам и имеет unique index. GTIN, serial и provider metadata — производные поля.
Преобразование bytes ↔ UTF-8/JSON выполняется только в валидируемом provider adapter.

Полный КМ запрещён в application logs, audit details, CSV и Excel. Backup содержит
raw КМ и поэтому шифруется и защищается как production secret.

## Consequences

GS сохраняется без зависимости от строковой нормализации. Поиск и диагностика идут
по hash/parsed fields. Код приложения обязан использовать value object вместо
произвольных строк; ручной SQL и экспорт КМ становятся менее удобными намеренно.

