# KIRO STEERING — PROJECT REPOSITORY MAP

<!-- Kiro IDE lê este arquivo permanentemente como âncora de contexto de alta prioridade -->

## 1. Domain Features
- **Auth:** `src/features/auth/` -> Login, JWT, RLS e recuperação de senha.
- **Orders:** `src/features/orders/` -> Carrinho, checkout e cálculo de totais.
- **Payments:** `src/features/payments/` -> Webhooks Stripe, PIX e idempotência.
- **Core DB:** `src/core/db/` -> Schemas Drizzle/Drift e migrations.

## 2. Invariants for Kiro
- Always inspect `PROJECT_INDEX.md` before searching across the disk.
- Keep files below 200 lines.
- Always generate tests for new business logic.
