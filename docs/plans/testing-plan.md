# План тестирования

> Стратегия QA для UrukhaiMark: уровни, сценарии, критерии приёмки.

## 1. Стратегия

| Уровень | Scope | Tooling | When |
|---------|-------|---------|------|
| Unit | KM parser, GS validation, FNC1 encoder | pytest/jest | Every commit |
| Integration | datamark API client (mock) | wiremock/nock | Every PR |
| Sandbox E2E | Full pipeline real API | pytest + sandbox creds | Pre-release |
| Visual/Golden | DataMatrix images | Image diff | Encoder changes |
| UAT | Operator workflow | Manual checklist | Before prod |
| Prod smoke | 1 order, 1 print | Manual | After deploy |

## 2. Critical test cases (must pass)

### GS integrity (P0)

| ID | Test | Expected |
|----|------|----------|
| T-GS-01 | Save KM to DB and reload | GS count unchanged |
| T-GS-02 | JSON serialize for addManufacture | `\u001d` preserved |
| T-GS-03 | Copy-paste simulation (strip GS) | Validator rejects |

### DataMatrix (P0)

| ID | Test | Expected |
|----|------|----------|
| T-DM-01 | Encode sample KM | Decodable, FNC1 present |
| T-DM-02 | Compare golden PNG | Pixel diff < threshold |
| T-DM-03 | QR library by mistake | CI fails (lint rule) |

### Order flow (P0)

| ID | Test | Expected |
|----|------|----------|
| T-ORD-01 | Create order label_type=7 | order_id returned |
| T-ORD-02 | Poll until status=30 | Within timeout |
| T-ORD-03 | Download KM count matches | count == requested |

### Compliance chain (P0)

| ID | Test | Expected |
|----|------|----------|
| T-RPT-01 | addMark before addManufacture | Success order |
| T-RPT-02 | addManufacture without mark | API error caught |
| T-SHP-01 | ship without manufacture | API error caught |
| T-SHP-02 | Full chain sandbox | ship accepted |

## 3. Sandbox E2E scenario

**Scenario: Cosmetics export RF — happy path**

```
Given: sandbox credentials, test GTIN in catalog
When:
  1. Create batch (100 units)
  2. Order label_type=7
  3. Download KM
  4. Generate 100 DataMatrix
  5. addMark
  6. addManufacture
  7. ships/add to agent
Then:
  - All KM status progressed
  - Ship document created
  - No GS corruption in audit log
```

## 4. Test data

| Asset | Location |
|-------|----------|
| Sample KM with GS | `tests/fixtures/km-samples.txt` |
| Golden DataMatrix | `tests/datamatrix-golden/` |
| Mock API responses | `tests/fixtures/datamark/` |

**Never commit:** prod credentials, real prod KM.

## 5. UAT checklist (operator)

- [ ] Login / config sandbox visible
- [ ] Select product by GTIN
- [ ] Order 10 codes (test batch)
- [ ] Preview DataMatrix on screen
- [ ] Print 10 labels
- [ ] Scan with mobile app «Электронный знак»
- [ ] Submit reports (sandbox)
- [ ] Verify batch status = Shipped

## 6. Regression triggers

Full sandbox E2E required when changing:

- DataMatrix encoder
- KM storage layer
- Report/shipment client
- Product Router logic

## 7. Acceptance criteria (MVP release)

- [ ] All P0 tests green in CI
- [ ] Sandbox E2E passed 3 consecutive runs
- [ ] UAT signed by operator
- [ ] No open P0/P1 bugs
- [ ] Runbook reviewed
