---
inclusion: auto
---

# 🗄️ 02 — Banco de Dados Moderno, ORMs & Performance

Este documento estabelece os padrões obrigatórios de modelagem de dados, chaves primárias e otimização de queries.

---

## 1. Identificadores Primários: Padrão UUIDv7 / ULID
- **Proibição de UUIDv4 Aleatório:** `gen_random_uuid()` / `UUIDv4` causa fragmentação severa de disco (B-Tree Page Splitting) em tabelas com alto volume de escrita.
- **Proibição de Inteiros Sequenciais Expostos:** `BIGINT SERIAL` (`/users/101`) expõe volume de negócios e gera colisão em apps offline/distribuídos.
- **Padrão Obrigatório:** Use sempre **UUIDv7** (ordenável por timestamp de 48-bits + payload aleatório de 74-bits) ou **ULID**:
  ```sql
  -- PostgreSQL
  CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v7(),
    customer_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
  );
  ```

---

## 2. Eliminação Total da Query N+1
- **Anti-Pattern Proibido:** NUNCA faça requisições ao banco de dados dentro de loops (`for`, `forEach`, `map`).
  ```typescript
  // ❌ ERRADO: 1 + 100 queries
  for (const user of users) {
    const orders = await db.select().from(ordersTable).where(eq(ordersTable.userId, user.id));
  }
  ```
- **Padrão Correto:** Use sempre **Eager Loading com JOIN** ou cláusulas **`IN (...)`**:
  ```typescript
  // ✅ CORRETO: 1 única query
  const usersWithOrders = await db.select()
    .from(usersTable)
    .leftJoin(ordersTable, eq(usersTable.id, ordersTable.userId));
  ```

---

## 3. Connection Pooling em Ambientes Serverless & Edge
- Em ambientes Serverless (Lambdas, Vercel, Supabase Edge Functions), conexões diretas esgotam o limite `max_connections` do banco.
- **Regra:** Conecte-se sempre através da porta do **Pooler de Conexões** (ex: Supabase porta `6543` / PgBouncer / Transaction Mode). Use a porta direta `5432` apenas para rodar migrações (*DDL*).

---

## 4. Migrações Versionadas e Reversíveis
- Toda alteração estrutural no banco deve ter um arquivo de migração versionado (`0001_create_users.sql`, `0002_add_status_to_orders.sql`).
- Toda migração deve ser idempotente e possuir estratégia de rollback seguro.
