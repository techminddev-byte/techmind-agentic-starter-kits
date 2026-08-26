---
name: database-audit
description: Auditoria de banco de dados, RLS e prevenção de queries N+1 para Antigravity
---

# Database Audit Skill — Antigravity

Ao inspecionar ou gerar código que toca bancos de dados:
1. Verifique se as tabelas no Supabase/PostgreSQL possuem `ENABLE ROW LEVEL SECURITY`.
2. Certifique-se de que chaves primárias usam UUIDv7 (`uuid_generate_v7()`) ou ULID.
3. Impeça loops que gerem queries N+1 (use JOINs ou `whereIn`).
