# 🤖 UNIVERSAL AGENTIC IDE RULES — TechMindDev
# Compatible with: Antigravity, Trae, VSCode Copilot, Kiro, Cursor, Claude Code, Windsurf

Este arquivo governa a geração de código em qualquer IDE Agentic.

---

## 1. Clean Architecture, SOLID & Qualidade de Código
- **Estrutura de Camadas:** Separe estritamente em `domain/` (puro), `application/` (use cases), `infrastructure/` (db/apis) e `presentation/` (ui/controllers).
- **Limite Rígido:** Máximo de **200 linhas por arquivo** e **40 linhas por método**. Proibido arquivos acumuladores (*God Files*).
- **Programação por Interfaces:** "Programe para uma interface, não para uma implementação." Todas as portas de saída de I/O devem ser abstrações injetadas.
- **Use Cases:** 1 classe por arquivo com método único `execute()`.

---

## 2. Resiliência, Fail-Fast & Idempotência
- **Fail-Fast:** Valide parâmetros com Guard Clauses no topo de cada método e falhe no primeiro milissegundo.
- **Value Objects:** Combata a Primitive Obsession criando objetos imutáveis e auto-validados (`Email`, `Money`, `Cpf`).
- **Idempotência:** Mutações críticas e webhooks devem usar `X-Idempotency-Key` e tabela de deduplicação.
- **Circuit Breaker:** Chamadas externas a APIs e LLMs devem ter timeouts estritos (3-5s) e fallback gracioso.
- **Anti-Dual-Write:** Use Transactional Outbox ou filas assíncronas para disparar eventos após salvar no banco.

---

## 3. Banco de Dados Moderno & ORMs
- **Chaves Primárias:** Use sempre **UUIDv7** ou **ULID**. Proibido UUIDv4 aleatório para índices B-Tree e serial exposto.
- **Anti-N+1 Query:** NUNCA execute queries dentro de loops; use `JOIN` ou cláusulas `IN (...)`.
- **Pooler de Conexões:** Conecte via porta do Pooler (ex: `6543`) em ambientes serverless/edge.

---

## 4. Versionamento Semântico (SemVer 2.0.0)
- **Formato:** `MAJOR.MINOR.PATCH`.
- **Conventional Commits:** `fix:` (Patch), `feat:` (Minor), `feat!:` / `BREAKING CHANGE:` (Major).
- **Changelog:** Atualização contínua do `CHANGELOG.md` no padrão Keep a Changelog.

---

## 5. Mobile & Flutter Cache-Busting
- **pubspec.yaml:** `version: MAJOR.MINOR.PATCH+BUILD_NUMBER`.
- **Telemetria de Versão:** Exiba a versão real na tela do app via `PackageInfo.fromPlatform()`.
- **Reset de Cache:** Limpeza profunda com `flutter clean && flutter pub get` e `./gradlew clean`.

---

## 6. Tipagem, Resiliência & Segurança
- **Zero `any`:** Tipagem estrita no TypeScript e Pydantic/TypedDict no Python.
- **Zero Catch Vazio:** Proibido silenciar exceções. Lance exceções nomeadas de domínio.
- **Validação de Bordas:** Valide requisições e webhooks com esquemas tipados (Zod/Pydantic).
- **Segredos Seguros:** Chaves e credenciais devem residir exclusivamente em `.env` (ignorado pelo Git).
