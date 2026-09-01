# Contributing

## Documentation checks

Run before submitting documentation changes:

```bash
npx --yes markdownlint-cli2 "**/*.md"
git diff --check
python3 scripts/check_markdown_links.py
```

Do not edit files under `docs/planning/archive/` except for mechanical link repair.
Architecture changes require an ADR when they alter a previously accepted decision.
Regulatory claims require a primary source, sandbox evidence or a written operator
answer recorded in `docs/planning/architecture-validation.md`.
