# API Cookbook — datamark.by

Практические примеры для UrukhaiMark. Полный справочник: [reference.md](reference.md).

**Base URLs:**

- Sandbox: `https://sandbox-api.datamark.by`
- Production: `https://api.datamark.by`

---

## Авторизация

```http
POST /auth
Content-Type: application/json

{
  "username": "user@company.by",
  "password": "***",
  "is_rules_agree": true
}
```

Ответ:

```json
{
  "token": "eyJ...",
  "expires_in": "2026-07-11 13:20:00"
}
```

Дальнейшие запросы:

```http
Token: eyJ...
Content-Type: application/json; charset=utf-8
```

Token TTL ~20 мин — реализовать auto-refresh в UrukhaiMark.

---

## Типы кодов

```http
GET /labels/types
Token: {token}
```

Ключевые значения: `7` (экспорт РФ), `20` (СИ РБ), `6` (SSCC).

---

## Заказ кодов (экспорт РФ)

```http
POST /v3/orders/add
Token: {token}

{
  "label_type": 7,
  "count": 100,
  "gtin": "04810012345678",
  "comment": "Освежитель партия 2026-07"
}
```

Ответ:

```json
{
  "id": 2000489528,
  "created_at": "2026-07-11 12:00:00"
}
```

### Polling статуса

```http
GET /v3/orders/list/2000489528
Token: {token}
```

Ждать `status.code === 30` («Выполнен»).

### Скачивание КМ

```http
POST /v3/orders/downloads
Token: {token}

{
  "order_id": 2000489528
}
```

КМ содержат `\u001d` — **сохранять as-is** в БД.

---

## Отчёт о маркировке

```http
POST /v3/reports/addMark
Token: {token}

{
  "group": "cosmetics",
  "gtin": "04810012345678",
  "labels": ["010481001234567821ABC...\u001d91...\u001d92..."],
  "params": {
    "manufacture_date": "2026-07-01"
  }
}
```

После успеха: status КМ → **47** (Нанесён).

---

## Отчёт о производстве

```http
POST /v3/reports/addManufacture
Token: {token}

{
  "group": "cosmetics",
  "labels": ["..."],
  "params": {
    "manufacture_date": "2026-07-01",
    "expiration_date": "2028-07-01"
  }
}
```

Условия: label_type=7, status 47/50, ≤ 10 000 КМ.

---

## Отгрузка в РФ

```http
POST /v3/ships/add
Token: {token}

{
  "shipping_doc": "tnttn",
  "nomer_tn": "ТТН-001234",
  "agent": 18413,
  "count": 100,
  "country": "643",
  "operation_date": "2026-07-11",
  "labels": ["010481001234567821..."],
  "eas_products": {
    "04810012345678": {
      "certificate_document_data": [{
        "certificate_type": "CONFORMITY_DECLARATION",
        "certificate_number": "ЕАЭС BY/112 ДОПОП 123",
        "certificate_date": "2025-01-15"
      }]
    }
  }
}
```

`agent` — ID контрагента из `/contracts` или ЛК.

---

## Валидация КМ

```http
POST /v2/labels
Token: {token}

{
  "labels": ["010481001234567821..."]
}
```

---

## Справочники

```http
GET /directories/{code}
Token: {token}
```

Коды: `country`, `currency`, `certificate_types`, `shippingDocs`.

---

## Обработка ошибок

| HTTP | Действие |
|------|----------|
| 401 | Refresh token / re-auth |
| 400 + GTIN not found | Sync ePASS → catalog |
| 400 + status | Проверить порядок reports |

См. [troubleshooting.md](../troubleshooting.md).
