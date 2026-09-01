# Contributing

Этот репозиторий — документация (docs-as-code): она живёт в git, ревьюится как код и проходит автоматическую проверку в CI при каждом изменении.

## Структура

Документация организована по [Diátaxis](https://diataxis.fr/) — см. [docs/README.md](docs/README.md). Коротко:

| Раздел | Правило |
|--------|---------|
| `docs/tutorials/` | Обучение с нуля |
| `docs/how-to/` | Решение конкретной задачи |
| `docs/reference/` | Справочные данные (таблицы, лимиты, схемы) |
| `docs/explanation/` | Контекст и рассуждения — «почему» |
| `docs/planning/` | Project-management (roadmap, validation, WBS, governance) — не Diátaxis |
| `docs/decisions/` | ADR — архитектурные решения |
| `research/` | Рабочие заметки и spike-логи; в канон `docs/` не входят, пока явно не перенесены |

**Правило «один файл — одна функция»**: не добавляйте объяснение контекста в how-to и не добавляйте пошаговую инструкцию в reference. Если материал не помещается в один квадрант — разделите на два файла и свяжите ссылкой.

## Архитектурные решения (ADR)

Решения масштаба «выбор стека», «CLI vs Web», «формат печати», topology/KM storage фиксируются как ADR в `docs/decisions/` — не как абзац в `architecture.md`. После статуса `Accepted` секции `Context`/`Decision` **не редактируются**; при пересмотре создаётся новый ADR, у старого меняется только `Status` → `Superseded by ADR-NNNN`. Подробности: [docs/decisions/README.md](docs/decisions/README.md).

Не редактируйте файлы под `docs/planning/archive/`, кроме механического ремонта ссылок.

Regulatory-утверждения требуют первичного источника, sandbox-evidence или письменного ответа оператора, зафиксированного в [docs/planning/architecture-validation.md](docs/planning/architecture-validation.md).

## Как проходит ревью

1. Ветка от `main`, изменения в PR.
2. CI (`.github/workflows/docs-lint.yml`):
   - `markdownlint-cli2` — стиль markdown (`.markdownlint-cli2.jsonc`)
   - `scripts/check_markdown_links.py` — относительные ссылки между `.md` резолвятся
3. Ревью PR: новый/изменённый документ в верном Diátaxis-квадранте, не дублирует источник истины из `docs/reference/`, обновлён `docs/README.md` / `llms.txt` при добавлении или переименовании файла.
4. Merge только после зелёного CI.

## Локальная проверка перед PR

```bash
npx --yes markdownlint-cli2 "**/*.md"
git diff --check
python3 scripts/check_markdown_links.py
```
