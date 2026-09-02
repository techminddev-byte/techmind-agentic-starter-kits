# GOVERNANÇA DE VERSIONAMENTO: SEMANTIC VERSIONING (SemVer 2.0.0)

Esta regra orienta o Agente de IA a manter a disciplina de versionamento contínuo no repositório.

---

## 1. Regras de Classificação de Mudanças

Sempre que concluir alterações no código ou for solicitado a gerar uma versão/release:

1. **PATCH (0.0.X)**:
   - Correções de bugs que não alteram a assinatura de métodos ou endpoints.
   - Refatorações internas, ajustes de estilo, otimizações de performance.
   - Padrão de commit: `fix: ...`, `refactor: ...`, `perf: ...`.

2. **MINOR (0.X.0)**:
   - Adição de novas telas, novos componentes, novos endpoints ou parâmetros opcionais.
   - Qualquer nova funcionalidade retrocompatível.
   - Padrão de commit: `feat: ...`.

3. **MAJOR (X.0.0)**:
   - Remoção ou renomeação de endpoints públicos, colunas essenciais ou parâmetros obrigatórios.
   - Alterações arquiteturais que exigem migração ou quebram integrações legadas.
   - Padrão de commit: `feat!: ...`, `fix!: ...` ou `BREAKING CHANGE: ...`.

---

## 2. Ações Automáticas do Agente

Ao finalizar tarefas de ciclo de release:
1. Atualizar o campo `"version"` no `package.json` (ou arquivo de versão relevante).
2. Atualizar o arquivo `CHANGELOG.md` no padrão **Keep a Changelog**:
   - `### Added` (Novidades)
   - `### Changed` (Modificações)
   - `### Deprecated` (Recursos descontinuados)
   - `### Removed` (Recursos removidos / Breaking Changes)
   - `### Fixed` (Correções)
   - `### Security` (Segurança)
3. Apresentar o resumo das alterações e a mensagem de commit recomendada.
