# ADR-0003: Default print format

## Status

Proposed

## Date

2026-08-01

## Context

ZPL обеспечивает прямую промышленную печать, PDF — переносимый fallback. Корректность
FNC1/GS зависит от реального printer toolchain и carrier.

## Decision

Не принято. ZPL — рабочая гипотеза, PDF — fallback; выбор закрывает физический spike.

## Consequences

Print port поддерживает независимые adapters. Ни один формат не считается production-
ready до побайтового scan-back и проверки grade.
