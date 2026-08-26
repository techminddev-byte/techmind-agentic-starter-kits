# 🤖 Universal Agentic IDE Rules — TechMindDev
# Compatible with: Antigravity, Trae, Cursor, Kiro, Claude Code, Windsurf

Este documento contém o conjunto universal de regras para qualquer IDE Agentic.

---

## 1. Clean Architecture & Estrutura de Pastas
- Estruture o código no padrão **Feature-First** (`src/features/{feature}/`).
- Mantenha cada arquivo com no máximo **200 linhas de código**.
- Isole a camada de apresentação (UI) das regras de negócio e chamadas de API.

---

## 2. Consumo Seguro de APIs Externas (Anti-Ban & Quota Management)
- **Cache-First Obrigatório:** NUNCA faça requisições diretas de leitura na renderização de tela sem consultar o cache local (Redis/Postgres) com TTL mínimo de 12 horas.
- **Batching:** Agrupe múltiplos IDs em lotes (ex: 50 IDs por chamada na API do YouTube/Maps).
- **Throttling:** Limite a taxa para no máximo 2 requisições por segundo via `p-limit`.
- **Resiliência:** Implemente **Exponential Backoff com Jitter** para erros HTTP 429 e 403.

---

## 3. Bancos de Dados & Persistência
- Chaves primárias devem usar **UUIDv7** (`uuid_generate_v7()`) ou ULID.
- Tabelas no Supabase/Postgres DEVEM ter **Row Level Security (RLS)** ativo com policies vinculadas ao `auth.uid()`.
- Evite o problema da query **N+1** utilizando `JOINs` explícitos.

---

## 4. Segurança 360°
- NUNCA coloque chaves de API secretas no frontend.
- Valide todos os payloads recebidos com **Zod / Pydantic**.
- Valide assinaturas criptográficas (HMAC) em todos os webhooks de pagamento.
