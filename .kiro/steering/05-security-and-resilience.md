---
inclusion: auto
---

# 🛡️ 05 — Segurança, Resiliência, Idempotência & Circuit Breakers

Este documento define regras de proteção de dados, tratamento de exceções, resiliência de software e prevenção de falhas em produção.

---

## 1. Idempotência Obrigatória (Cobrança Dupla e Webhooks)
- Toda operação de mutação crítica (pagamentos, pedidos, emissão de notas) ou recebimento de Webhooks deve suportar cabeçalhos de **`X-Idempotency-Key`**.
- Registre o `idempotency_key` ou `event_id` no banco de dados em transação antes de executar a lógica de negócio para evitar processamento duplicado.

---

## 2. Circuit Breakers & Timeouts Estritos para APIs Externas
- Toda chamada externa (APIs de Terceiros, Gateways, LLMs da OpenAI/Anthropic/Gemini) deve possuir:
  - **Timeout Explícito:** Máximo de 3 a 5 segundos para APIs normais e 15s para LLMs.
  - **Circuit Breaker:** Se houver falhas consecutivas, abra o circuito e retorne fallback imediato para não exaurir o pool de conexões e causar *Out-of-Memory (OOM)*.

---

## 3. Prevenção do Problema de "Dual-Write" (Transactional Outbox)
- NUNCA salve no banco e dispare um evento externo (WhatsApp, Email, Webhook) na mesma função de forma ingênua:
  ```typescript
  // ❌ PROIBIDO: Se a rede cair entre o passo 1 e o 2, os dados ficam corrompidos
  await db.orders.create(order);
  await sendWhatsApp(order);
  ```
- **Padrão Correto:** Use o padrão **Transactional Outbox** (grave o evento na tabela `outbox` na mesma transação atômica do banco) ou use filas assíncronas (Redis/BullMQ/Kafka).

---

## 4. Tratamento de Exceções & Zero Catch Silencioso
- **Proibição Absoluta:** NUNCA crie blocos `try/catch` vazios ou que apenas façam `console.log(e)`.
- **Exceções de Domínio:** Lance exceções nomeadas e tipadas (ex: `InvalidEmailException`, `UnauthorizedOperationException`, `EntityNotFoundException`).
- **Log Estruturado:** Erros de sistema devem ser encaminhados para observabilidade (Sentry, Winston, Datadog) com contexto do usuário e stack trace preservado.

---

## 5. Tipagem Rigorosa (Zero `any`)
- **TypeScript:** Use `strict: true` no `tsconfig.json`. Proibido o uso de `any`. Use tipos literais, `unknown` com type guards ou interfaces explícitas.
- **Python:** Proibido retornar dicionários genéricos `dict` soltos em funções críticas. Use `Pydantic` models ou `TypedDict`.
- **Dart:** Null safety ativado e uso criterioso do operador `!`.

---

## 6. Validação de Entradas com Schemas (Zod / Pydantic)
- Toda entrada de dados vinda do usuário, de requisições HTTP ou de Webhooks deve ser validada e sanitizada antes de atingir a camada de domínio.
- Use **Zod** (TypeScript) ou **Pydantic** (Python) nas bordas do sistema (*Presentation Layer*).

---

## 7. Gerenciamento Seguro de Segredos (.env)
- Chaves de API, senhas de banco e certificados NUNCA devem estar no código-fonte.
- Devem ser lidos exclusivamente via variáveis de ambiente (`process.env`, `os.environ`, `Platform.environment`).
- O arquivo `.env` deve estar explicitamente incluído no `.gitignore`.
