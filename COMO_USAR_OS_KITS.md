# 🚀 Como Usar os Starter Kits de Governança Agentic

Bem-vindo ao **TechMind Agentic Starter Kit**! 

Basta escolher a IDE que você utiliza e copiar o arquivo correspondente para a raiz do seu projeto. O seu agente de IA assumirá imediatamente a postura de um **Arquiteto de Software de Elite**.

---

## 📦 Qual arquivo copiar para o seu projeto?

### 1. Se você usa o **Kiro IDE**:
- Copie a pasta **`.kiro/steering/`** para a raiz do seu projeto.
- O Kiro carregará automaticamente todos os 5 arquivos modulares:
  - `01-clean-architecture-solid.md` (Clean Arch, SOLID, Interfaces, Max 200 linhas)
  - `02-database-and-orm.md` (UUIDv7, Anti-N+1, Connection Pooler)
  - `03-versioning-and-semver.md` (SemVer 2.0.0, Conventional Commits)
  - `04-mobile-flutter-cache.md` (pubspec.yaml, versionName+buildNumber, cache reset)
  - `05-security-and-resilience.md` (Zod, Env vars, Zero any, Zero catch vazio)

---

### 2. Se você usa o **Cursor IDE**:
- Copie o arquivo **`.cursorrules`** para a raiz do seu projeto.

---

### 3. Se você usa o **Antigravity (Google / Gemini)**:
- Copie a pasta **`.agents/rules/`** para a raiz do seu projeto.

---

### 4. Se você usa o **Claude Code (Terminal CLI)**:
- Copie o arquivo **`CLAUDE.md`** para a raiz do seu projeto.

---

### 5. Se você usa o **Windsurf (Cascade)**:
- Copie o arquivo **`.windsurfrules`** para a raiz do seu projeto.

---

### 6. Se você usa **Trae, VSCode Copilot ou outra IDE**:
- Copie o arquivo **`AGENTS.md`** para a raiz do seu projeto.

---

## 🎯 O que o seu Agente passará a fazer imediatamente:
1. **Nunca mais criará arquivos gigantes:** O agente respeitará o limite de 200 linhas e quebrará a lógica em Use Cases e componentes modulares.
2. **Programará orientado a Interfaces:** Dependências de banco e APIs serão injetadas via portas desacopladas.
3. **Usará UUIDv7 e evitará Query N+1:** O banco de dados nascerá performático e escalável.
4. **Versionará no padrão SemVer:** Sugerirá commits no padrão `feat:`, `fix:`, `feat!:` e manterá o `CHANGELOG.md` atualizado.
5. **No Mobile (Flutter):** Manterá a sincronia de `versionName + buildNumber` eliminando problemas de cache.
