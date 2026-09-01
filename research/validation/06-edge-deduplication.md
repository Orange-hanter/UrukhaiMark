# Spike 06 — повторная доставка edge-событий

## Результат

**Design pass:** принят inbox/outbox-контракт с at-least-once delivery и
идемпотентным consumer.

Каждое событие содержит:

- глобальный `event_id`;
- `agent_id`, `line_id` и монотонный `agent_sequence`;
- `allocation_id`, `code_hash`, тип и timestamp;
- версию схемы и causation/correlation IDs.

Центр сначала атомарно записывает `event_id` в inbox и применяет переход FSM.
Повтор с тем же ID возвращает прежний результат. Разрыв последовательности ставит
линию в `reconciliation_required`, но не переигрывает уже подтверждённые события.

## Acceptance

Replay в случайном порядке не создаёт вторую печать, allocation или запись упаковки;
после восстановления агент удаляет outbox-событие только по ACK центра.
