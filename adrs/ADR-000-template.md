# ADR-000: [Título Curto e Imperativo da Decisão]

* **Status:** [ Proposto | Aceito | Rejeitado | Obsoleto | Substituído por ADR-XXX ]
* **Data:** YYYY-MM-DD
* **Autores:** [ Nome do Engenheiro / Pair com IA ]
* **Decisores:** [ Equipe de Engenharia / Tech Lead ]

---

## 1. Contexto & Declaração do Problema
*Descreva o contexto técnico ou de negócio que gerou a necessidade desta decisão. Quais são as restrições, dores atuais e requisitos que devemos atender?*

Exemplo:
> "Nosso sistema atual faz chamadas síncronas para a API da OpenAI dentro dos endpoints HTTP. Quando a latência da API aumenta, as conexões de banco de dados se esgotam e travam o servidor."

---

## 2. Opções Consideradas

### Opção A: [Nome da Opção A]
* **Vantagens:** 
  * [Pró 1]
  * [Pró 2]
* **Desvantagens:**
  * [Contra 1]
  * [Contra 2]

### Opção B: [Nome da Opção B]
* **Vantagens:** 
  * [Pró 1]
  * [Pró 2]
* **Desvantagens:**
  * [Contra 1]
  * [Contra 2]

---

## 3. Decisão Escolhida
*Declare a opção escolhida de forma clara e a justificativa técnica principal.*

> "Decidimos adotar a **Opção B**, implementando o padrão **Circuit Breaker com Fallback** e enfileiramento assíncrono via Redis BullMQ."

---

## 4. Consequências & Trade-offs

### Consequências Positivas:
- [Benefício 1]
- [Benefício 2]

### Consequências Negativas / Custos:
- [Trade-off 1 / Nova dependência adicionada]
- [Necessidade de monitoramento adicional]

---

## 5. Notas de Implementação & Regras para Agentes de IA
*Instruções claras para que agentes de IA (Cursor/Kiro) saibam como implementar código em conformidade com esta ADR.*

- [ ] Toda chamada externa deve usar a classe `ResilientHttpClient`.
- [ ] O tempo limite (timeout) padrão deve ser de 5.000ms.
