# ⚡ TechMind Agentic Starter Kits & Templates

<div align="center">

```
  _______        _     __  __ _           _ _____             
 |__   __|      | |   |  \/  (_)         | |  __ \            
    | | ___  ___| |__ | \  / |_ _ __   __| | |  | | _____   __
    | |/ _ \/ __| '_ \| |\/| | | '_ \ / _` | |  | |/ _ \ \ / /
    | |  __/ (__| | | | |  | | | | | | (_| | |__| |  __/\ V / 
    |_|\___|\___|_| |_|_|  |_|_|_| |_|\__,_|_____/ \___| \_/  
```

**Repositório Oficial de Starter Kits, Steering Rules, ADRs e Quality Gates para Engenharia de Software com IA**

[![GitHub Stars](https://img.shields.io/github/stars/techminddev-byte/techmind-agentic-starter-kits?style=for-the-badge&color=00FF41&logo=github)](https://github.com/techminddev-byte/techmind-agentic-starter-kits)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Academy](https://img.shields.io/badge/Academy-TechMind-blue?style=for-the-badge&color=00FF41)](https://techminddev.com)

</div>

---

## 🎯 Por que este repositório existe?

Agentes de IA (Cursor, Kiro, Claude Code, Trae, Antigravity) são extremamente poderosos, mas sem **regras determinísticas de engenharia**, eles geram:
- Arquivos monolíticos de 2.000 linhas sem abstração;
- Vazamento de modelos de banco (ORM) dentro de regras de negócio;
- Secrets expostos no frontend e bypass de segurança;
- Falhas de idempotência e *dual-write problem*.

Este repositório fornece **a blindagem necessária para transformar qualquer agente de IA em um Engenheiro Sênior disciplinado**.

---

## 📦 Conteúdo dos Starter Kits

| Diretório / Arquivo | Ferramenta | Descrição |
| :--- | :---: | :--- |
| [`.cursorrules`](file:///.cursorrules) | **Cursor IDE** | Regras universais de Clean Architecture, TDD e prevenção de alucinações. |
| [`CLAUDE.md`](file:///CLAUDE.md) | **Claude Code** | Guia de contexto, comandos de terminal e restrições para agentes CLI. |
| [`.kiro/steering/`](file:///.kiro/steering/) | **Kiro IDE** | Steering files modulares e hooks automáticos de enforcement. |
| [`adrs/`](file:///adrs/) | **Arquitetura** | Template de *Architecture Decision Records* (ADRs) para versionar decisões com IA. |
| [`docker/`](file:///docker/) | **DevOps** | `Dockerfile` multi-stage leve e seguro (não-root) + `docker-compose.yml`. |
| [`github-actions/`](file:///github-actions/) | **CI/CD** | Pipeline de *Quality Gates* que barra Pull Requests com código quebrado de IA. |
| [`mcp-server/`](file:///mcp-server/) | **MCP** | Boilerplate de Servidor Model Context Protocol (TypeScript) para criar Custom Tools. |
| [`checklists/`](file:///checklists/) | **Auditoria** | Checklist de Auditoria Semântica para revisão de código gerado por IA. |

---

## 🚀 Como Usar no seu Projeto

### Opção 1: Usar como Template no GitHub
Clique no botão verde **"Use this template"** no topo deste repositório para iniciar um novo projeto já com todas as regras configuradas.

### Opção 2: Clonar via Terminal
```bash
# Clone o repositório
git clone https://github.com/techminddev-byte/techmind-agentic-starter-kits.git

# Copie as regras para o seu projeto existente
cp techmind-agentic-starter-kits/.cursorrules ./meu-projeto/
cp -r techmind-agentic-starter-kits/adrs ./meu-projeto/
```

---

## 🏛️ Princípios de Engenharia Aplicados

1. **A Regra da Dependência:** Regras de negócio puras em `domain/` sem imports de frameworks.
2. **Value Objects em vez de Primitives:** Tipos auto-validados para evitar alucinações.
3. **Single-File Use Cases:** Cada caso de uso é um arquivo isolado com um único método `execute()`.
4. **Resiliência por Padrão:** Circuit Breaker, Idempotência e Outbox Pattern.

---

## 📄 Licença
Distribuído sob a licença MIT. Livre para uso pessoal e comercial em seus projetos e empresas.

<div align="center">
  <sub>Desenvolvido com 💚 pela equipe <b>TechMindDev</b></sub>
</div>
