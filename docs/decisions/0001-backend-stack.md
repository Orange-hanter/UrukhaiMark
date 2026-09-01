# ADR-0001: Backend runtime

## Status

Proposed

## Date

2026-08-01

## Context

Кандидаты — Python/FastAPI и Node.js/TypeScript. Оба поддерживают требуемые API,
worker и PostgreSQL; выбор зависит от проверенного DataMatrix toolchain и команды.

## Decision

Не принято. Решение должно опираться на spike encoder/printing, а не на UI-язык.

## Consequences

Логическая архитектура и порты не зависят от runtime. Scaffold блокирован до выбора.
