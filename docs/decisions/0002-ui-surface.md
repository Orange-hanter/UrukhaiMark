# ADR-0002: UI surface

## Status

Proposed

## Date

2026-08-01

## Context

Оператору нужны явные quality gates и безопасный запуск compliance-операций.
CLI проще для ранней проверки, Web UI удобнее для многопользовательской работы.

## Decision

Не принято. MVP API не должен зависеть от выбранного presentation adapter.

## Consequences

Acceptance test оператора должен определить CLI-first или Web-first до Milestone 1.5.
