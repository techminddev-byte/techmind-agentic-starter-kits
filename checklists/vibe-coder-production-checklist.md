# 🚀 Vibe Coder Production Launch Checklist

O checklist definitivo para quem constrói com agentes de IA antes de abrir o app para o público e colocar em produção.

---

## 1. Segurança & Chaves de API
- [ ] **Nenhuma chave secreta no frontend:** `OPENAI_API_KEY`, `STRIPE_SECRET_KEY` ou credenciais de banco estão apenas no `.env` do backend?
- [ ] O arquivo `.env` está listado no `.gitignore` e NUNCA foi commitado no Git?
- [ ] As tabelas do Supabase/PostgreSQL possuem **Row Level Security (RLS)** ativado com policies estritas?
- [ ] As regras do Firestore (`firestore.rules`) validam `request.auth != null` e a propriedade do documento?
- [ ] Todos os endpoints de backend validam o payload de entrada com **Zod / Pydantic**?

---

## 2. Pagamentos, Webhooks & Mídia
- [ ] O endpoint de Webhook valida a **assinatura criptográfica** (`stripe-signature` / HMAC)?
- [ ] O processamento de pagamento é **idempotente** (não entrega o produto duplicado se o webhook for chamado 2x)?
- [ ] Uploads de fotos/vídeos usam **Presigned URLs (S3 / Cloudflare R2)** e não salvam Base64 no banco de dados?
- [ ] Se o app iOS tiver login social, o botão **"Entrar com a Apple"** está implementado?

---

## 3. Infraestrutura, Deploy & FinOps
- [ ] O domínio possui certificado **SSL/HTTPS** ativo (cadeado verde)?
- [ ] A esteira de **CI/CD (GitHub Actions)** roda os testes antes de publicar na produção?
- [ ] O **Sentry / Bugsnag** está configurado para capturar erros e stack traces em tempo real?
- [ ] **Hard Limits e alertas de faturamento** estão ativos na OpenAI, Anthropic e AWS para evitar cobranças acidentais?
