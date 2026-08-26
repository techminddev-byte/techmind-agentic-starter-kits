# 🗺️ PROJECT REPOSITORY INDEX & ARCHITECTURE MAP
<!-- Template oficial TechMindDev para agentes de IA (Antigravity, Kiro, Claude Code, Cursor, Windsurf) -->

Este arquivo é o mapa de arquitetura canônico do repositório. Agentes de IA devem consultar este índice antes de realizar buscas no disco ou modificar arquivos.

---

## 1. Mapa de Domínio & Features (Feature-First)

| Feature / Módulo | Diretório | Responsabilidade Principal | Arquivo de Entrada |
| :--- | :--- | :--- | :--- |
| **Auth** | `src/features/auth/` | Autenticação, JWT, RLS e recuperação de senha | `auth.service.ts` |
| **Checkout** | `src/features/checkout/` | Carrinho, cálculo de totais e regras de frete | `checkout.controller.ts` |
| **Payments** | `src/features/payments/` | Webhooks Stripe, PIX e idempotência | `stripe.webhook.ts` |
| **Core Network** | `src/core/network/` | Cliente HTTP com interceptors e retry | `api_client.ts` |
| **Database** | `src/core/db/` | Schemas Drizzle/Drift e migrations | `schema.ts` |

---

## 2. Dicionário de Entidades & Chaves Primárias

| Entidade / Tabela | Tipo de ID | Chave Primária | RLS Ativo? | Localização do Schema |
| :--- | :--- | :--- | :---: | :--- |
| `users` | UUIDv7 | `id` | ✅ Sim | `src/core/db/schema.ts` |
| `orders` | UUIDv7 | `id` (FK: `user_id`) | ✅ Sim | `src/core/db/schema.ts` |
| `payments` | ULID | `id` (FK: `order_id`)| ✅ Sim | `src/core/db/schema.ts` |

---

## 3. Invariantes de Localização para Agentes de IA
1. Interfaces visuais (UI): `src/features/{feature}/views/` ou `src/features/{feature}/widgets/`
2. Lógica e chamadas de API: `src/features/{feature}/services/` ou `src/features/{feature}/repositories/`
3. Contratos e Schemas Zod/Pydantic: `src/features/{feature}/types/` ou `packages/contracts/`
4. NUNCA crie arquivos soltos fora dessas pastas sem atualizar este índice.
