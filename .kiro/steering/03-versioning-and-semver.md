---
inclusion: auto
---

# 🏷️ 03 — Versionamento Semântico (SemVer) & Conventional Commits

Este documento rege a disciplina de releases, numeração de versão e mensagens de commit.

---

## 1. Padrão Semantic Versioning (SemVer 2.0.0)

Formato: `MAJOR . MINOR . PATCH` (ex: `2.4.1`)

| Dígito | Nome | Gatilho de Incremento | Exemplo |
| :---: | :--- | :--- | :--- |
| **1º** | **`MAJOR`** | **Breaking Change:** Quebra de contrato, alteração de endpoint público, mudança incompatível de banco ou assinatura. | `1.4.2` ➔ `2.0.0` |
| **2º** | **`MINOR`** | **Nova Feature:** Adição de rotas, componentes, telas ou parâmetros opcionais sem quebrar o código anterior. | `1.4.2` ➔ `1.5.0` |
| **3º** | **`PATCH`** | **Bug Fix:** Correções de defeitos internos, refatoração de código sem impacto externo, pequenos ajustes. | `1.4.2` ➔ `1.4.3` |

---

## 2. Padrão de 4 Números (Windows / Mobile)

Quando compilando executáveis (.exe, .dll) ou gerando pacotes mobile (.apk, .ipa):
- Formato: `MAJOR . MINOR . BUILD . REVISION` (ex: `2.1.1840.12`).
- **`BUILD` (3º dígito):** Número sequencial gerado automaticamente pelo servidor de CI/CD.
- **`REVISION` (4º dígito):** Hotfix emergencial aplicado sobre um binário já gerado.

---

## 3. Padrão Conventional Commits (Gatilhos do Agente)

O Agente de IA deve sugerir mensagens de commit padronizadas:

- `fix(modulo): descricao` ➔ Dispara incremento **PATCH**.
- `feat(modulo): descricao` ➔ Dispara incremento **MINOR**.
- `feat!(modulo): descricao` ou `fix!(modulo): descricao` (com `BREAKING CHANGE:` no rodapé) ➔ Dispara incremento **MAJOR**.
- `refactor:`, `perf:`, `chore:`, `docs:`, `test:` ➔ Manutenções internas sem alteração na versão pública ou apenas PATCH.

---

## 4. Atualização Obrigatória do `CHANGELOG.md`
Toda release concluída deve gerar uma entrada no topo do `CHANGELOG.md` seguindo o formato [Keep a Changelog]:
- `### Added` (Novidades)
- `### Changed` (Alterações de comportamento)
- `### Fixed` (Correções de bugs)
- `### Removed` (Recursos descontinuados / Breaking Changes)
