---
inclusion: auto
---

# 🏛️ 01 — Clean Architecture, SOLID & Regra das 200 Linhas

Este documento define as regras inegociáveis de arquitetura de software, modularidade e qualidade de código para o projeto.

---

## 1. Regra de Ouro do Tamanho de Arquivo (Anti-Monolito)
- **Limite por Arquivo:** Nenhum arquivo deve ultrapassar **200 linhas de código** (com tolerância máxima absoluta de 250 linhas em arquivos de schema/config).
- **Limite por Função/Método:** Funções não devem ter mais de **40 linhas**. Se uma função fizer mais do que uma coisa, quebre-a em sub-funções puras e privadas.
- **Tolerância Zero a God Files:** Proibido arquivos acumuladores como `utils.ts`, `helpers.py`, `CommonService.dart` ou controllers gigantescos. Cada responsabilidade deve ter seu próprio arquivo.

---

## 2. Princípios SOLID & Boas Práticas de Engenharia

### S — Single Responsibility (Responsabilidade Única)
- Cada classe ou arquivo deve ter apenas **um único motivo para mudar**.
- Separe validação de dados, regras de negócio e chamadas de rede/banco em arquivos distintos.

### O — Open/Closed (Aberto para Extensão, Fechado para Modificação)
- Comportamentos novos devem ser adicionados criando novas implementações ou estratégias (Strategy Pattern), nunca adicionando dezenas de `if/else` ou `switch` aninhados em código existente.

### L — Liskov Substitution (Substituição de Liskov)
- Subclasses ou implementações devem ser substituíveis por suas interfaces base sem quebrar o comportamento do sistema.

### I — Interface Segregation (Segregação de Interfaces)
- Crie interfaces pequenas, focadas e específicas (Ports). Clientes não devem ser forçados a depender de métodos que não utilizam.

### D — Dependency Inversion (Inversão de Dependência)
- **"Programe para uma interface, não para uma implementação."** Módulos de alto nível (Regras de Negócio/Domínio) **NUNCA** devem depender de módulos de baixo nível (Banco, APIs, Frameworks). Ambos dependem de **Abstrações/Interfaces**.

---

## 3. Cláusulas Fail-Fast & Value Objects (DDD)

### Cláusulas Fail-Fast (Falhe no 1º Milissegundo)
- Verifique todas as pré-condições e parâmetros no topo de cada método usando *Guard Clauses*. Aborte imediatamente antes de alocar memória, abrir conexões ou alterar estados:
  ```typescript
  if (!user.isActive) throw new UserInactiveException();
  if (order.items.length === 0) throw new EmptyOrderException();
  ```

### Combate à Primitive Obsession (Value Objects)
- Não use tipos primitivos soltos (`string`, `number`) para conceitos críticos de domínio. Crie **Value Objects** imutáveis e auto-validados (ex: `Email`, `Cpf`, `Money`, `ZipCode`):
  ```typescript
  const price = new Money(199.90, "BRL");
  const email = new Email("contato@techmind.dev.br");
  ```

---

## 4. Estrutura de Camadas (Clean Architecture)

```
src/
├── domain/            # 1. Entidades, Value Objects e Interfaces de Repositório (Zero Dependências)
├── application/       # 2. Use Cases (1 Use Case por arquivo com método execute())
├── infrastructure/    # 3. Implementações de DB (Drizzle, Prisma, Drift), APIs externas e Gateways
└── presentation/      # 4. Controllers, Rotas HTTP, Telas e Componentes UI
```

### Regra da Dependência:
- `domain` ➔ Não importa NADA de fora (nem ORM, nem HTTP client, nem UI).
- `application` ➔ Depende apenas do `domain`.
- `infrastructure` ➔ Implementa as interfaces definidas no `domain` ou `application`.
- `presentation` ➔ Executa Use Cases da `application` e converte dados para a UI.

---

## 5. Programação Orientada a Interfaces (Ports & Adapters)
- Todas as dependências externas de I/O (repositórios, gateways de pagamento, envio de email, brokers de mensageria) devem ser injetadas via **Interfaces**.
- **Exemplo Correto:**
  ```typescript
  // domain/ports/order-repository.port.ts
  export interface OrderRepositoryPort {
    save(order: Order): Promise<void>;
    findById(id: string): Promise<Order | null>;
  }

  // application/use-cases/create-order.use-case.ts
  export class CreateOrderUseCase {
    constructor(private readonly orderRepo: OrderRepositoryPort) {} // Injeção via Interface
    async execute(input: CreateOrderInput): Promise<OrderOutput> { ... }
  }
  ```
