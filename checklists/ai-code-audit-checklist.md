# 📋 Checklist de Auditoria Semântica para Código Gerado por IA

Utilize este checklist antes de aprovar qualquer Pull Request ou aceitar mudanças de agentes de IA:

---

## 1. 🏛️ Arquitetura & Camadas
- [ ] **Zero vazamento de infraestrutura no domínio:** A pasta `domain/` não importa ORM, HTTP clients ou frameworks?
- [ ] **Use Cases isolados:** As regras de negócio estão em arquivos de Use Case com método único `execute()`?
- [ ] **Injeção de dependências:** Todas as portas de I/O são injetadas através de interfaces no construtor?
- [ ] **Tamanho de arquivo controlado:** O arquivo alterado tem menos de 250 linhas?

---

## 2. 🛡️ Segurança & Validação
- [ ] **Sem Primitive Obsession:** Campos críticos (Email, CPF, Dinheiro, Status) usam Value Objects validados?
- [ ] **Sem secrets no código:** Não há API keys, senhas ou tokens hardcoded?
- [ ] **Proteção contra injeção:** Queries SQL são 100% parametrizadas (sem concatenação de strings)?
- [ ] **Output DTOs:** A API não retorna entidades internas diretamente no JSON de resposta?

---

## 3. ⚙️ Resiliência & Tratamento de Erros
- [ ] **Sem `try/catch` vazios:** Nenhum erro está sendo engolido sem log estruturado ou re-throw?
- [ ] **Timeouts definidos:** Toda chamada HTTP externa ou chamada de LLM tem timeout estrito configurado?
- [ ] **Idempotência:** Operações críticas de mutação aceitam cabeçalho `X-Idempotency-Key`?

---

## 4. 🧪 Testes & Confiabilidade
- [ ] **Testes unitários presentes:** O novo fluxo tem testes unitários cobrindo cenários de sucesso e erro?
- [ ] **Mocks apenas em contratos:** Os testes mockam apenas interfaces, sem simular comportamentos fictícios do domínio?
