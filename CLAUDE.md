# CLAUDE.md — TechMind Agentic Guidelines for Claude Code

## Project Overview
Este projeto segue a metodologia de Engenharia de Software para Agentes da TechMind Academy.

## Build and Test Commands
- `npm run build` or `pnpm build`: Constrói o projeto em produção
- `npm test` or `pytest`: Executa a suíte de testes unitários e de integração
- `npm run lint`: Valida conformidade de estilo e arquitetura

## Architecture Guidelines
1. **Separation of Concerns:**
   - `domain/`: Regras de negócio puras, Entidades, Value Objects e Interfaces de Repositório (Zero dependências externas).
   - `application/`: Casos de Uso (Use Cases) e DTOs de entrada/saída.
   - `infrastructure/`: Implementações de banco de dados (ORM/SQL), APIs de terceiros, LLMs e servidores HTTP.

2. **Code Style & Practices:**
   - Programe para interfaces e use Injeção de Dependências no construtor.
   - Trate erros lançando exceções tipadas de domínio.
   - Mantenha funções e métodos pequenos e coesos.
