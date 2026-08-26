# 🗄️ Database & Persistence AI Audit Checklist

Use este checklist para auditar qualquer código gerado por IA (Cursor, Kiro, Claude Code) que interaja com bancos de dados relacionais, NoSQL ou locais.

---

## 1. Chaves Primárias & IDs
- [ ] Chaves primárias usam **UUIDv7 (`uuid_generate_v7()`)** ou ULID em vez de UUIDv4 aleatório?
- [ ] O código Dart/Flutter não confunde o `doc.id` do Firestore com propriedades internas do payload?
- [ ] Nenhum endpoint público expõe IDs sequenciais numéricos (`/orders/1042`)?

---

## 2. Supabase & PostgreSQL
- [ ] A tabela possui `ALTER TABLE ... ENABLE ROW LEVEL SECURITY;` ativado?
- [ ] Existem policies explícitas de `SELECT`, `INSERT`, `UPDATE` e `DELETE` baseadas em `auth.uid()`?
- [ ] Todas as foreign keys possuem `ON DELETE CASCADE` ou `ON DELETE RESTRICT` explícito?
- [ ] Colunas JSONB consultadas com frequência possuem índice GIN (`CREATE INDEX ... USING gin`)?
- [ ] Funções serverless conectam via PgBouncer / Pooler (porta `6543`) e não na porta direta (`5432`)?

---

## 3. Firebase & Firestore
- [ ] Todas as chamadas de busca possuem cláusula `limit()` estrita?
- [ ] Paginações infinitas utilizam cursores `startAfterDocument()` em vez de offsets manuais?
- [ ] Queries que combinam múltiplos `where()` e `orderBy()` possuem índice composto criado no console?
- [ ] As regras de segurança em `firestore.rules` validam autenticação e propriedade dos dados?

---

## 4. Performance & ORMs (Drizzle / Drift / Prisma)
- [ ] Nenhuma query roda dentro de loops `for` / `forEach` (Problema da Query N+1 eliminado com `JOIN`)?
- [ ] Consultas analíticas pesadas utilizam **DuckDB local (Parquet)** em vez de onerar o banco transacional?
- [ ] Migrations seguem o padrão **Expand & Contract** para zero downtime em produção?
