# Открытые вопросы

> Технические решения ведутся в [ADR](../decisions/README.md), проверяемые API-
> предположения — в [architecture-validation](architecture-validation.md).

## Бизнес и регуляторика

| ID | Вопрос | Влияние | Gate | Статус |
|----|--------|---------|------|--------|
| B01 | Точный ТН ВЭД/ОКПД2 и GTIN каждого SKU | Product Router | Slice 0 | Открыт |
| B02 | Газовый баллон — aerosol/cosmetics или технический газ? | Scope | Future | Открыт |
| B03 | Контрагент РФ и `ships.agent` | MVP shipment | Slice 0 | Открыт |
| B04 | Кто получает КМ пива РФ и на каком юр. основании? | CRPT pipeline | Slice 7 | Открыт |
| B05 | Обязательна ли маркировка освежителей при продаже в РБ? | Domestic pipeline | Phase 2 | Support |
| B06 | Кто является master для партий: UrukhaiMark или ERP? | ERP contract | Slice 7 | Отложен |
| B07 | Нужны FBO, FBS или оба сценария? | Marketplace | Future | Отложен |
| B08 | Допускаются смешанные палеты и по каким правилам? | Packaging | Slice 5 | Открыт |
| B09 | Нужна прямая палетизация без короба? | Package model/UI | Slice 5 | Открыт |
| B10 | Вес маркируется на единице или только на упаковке? | Data/device model | Future | Открыт |

## API и эксплуатация

| ID | Вопрос | Влияние | Проверка |
|----|--------|---------|----------|
| A02 | Когда возникает datamark status 50? | Manufacture gate | API spec/support |
| A03 | Обязателен ли `manufacture_date` в `addMark`? | Payload contract | Sandbox |
| A04 | Правило повторной печати и списания повреждённого КМ? | Print FSM | Operator procedure |
| A05 | Есть подтверждённый API вывода из оборота? | Future capability | Primary spec |
| A06 | Как отменяется ошибочная BY-отгрузка? | Compensation | Written support answer |
| A09 | Какой контракт aggregation/SSCC применим? | Package model | API contract |
| O01 | Реальные скорость линии и расстояние printer→scanner? | Timeout/L2 design | Site survey |
| O02 | Какие ACK/no-read/grade сигналы выдаёт оборудование? | Driver contract | Vendor test |
| O03 | Требуемые RPO/RTO и offline SLA? | Deployment topology | Operations owner |

## Действия

- [ ] Заполнить [product-matrix.md](../reference/product-matrix.md).
- [ ] Получить письменные ответы datamark по A02—A06.
- [ ] Подтвердить контрагента РФ.
- [ ] Провести физические spikes по [validation reports](../../research/validation/README.md).

Выбор runtime, UI и print format не дублируется здесь: см. ADR-0001—0003.
