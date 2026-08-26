# CLAUDE.md — TECHMINDDEV AGENTIC STARTER KIT
# Canonical instructions for Anthropic's Claude Code CLI

## 🚀 Quick Commands
- **Build:** `npm run build || flutter build web`
- **Test:** `npm test || flutter test`
- **Lint/Format:** `npm run lint && npm run format || dart format .`
- **Typecheck:** `npx tsc --noEmit`

## 🗺️ Architecture & Index Pointer
- **ALWAYS** consult `PROJECT_INDEX.md` before searching across the disk.
- Follow Clean Architecture with **Feature-First** structure (`src/features/{feature}/`).
- Keep all files strictly under **200 lines of code**.

## 🛡️ Database & Security Rules
- Enable Row Level Security (RLS) on all Supabase/PostgreSQL tables.
- Use UUIDv7 for primary keys (`uuid_generate_v7()`).
- Never hardcode secret API keys in frontend bundles. Always use backend `.env` variables.
- External API calls (YouTube, Maps, OpenAI) MUST use Cache-First and batching.

## 📌 Session Checkpoints
- When completing tasks or when prompted, update `docs/CURRENT_STATE.md` with decisions, modified files and the next objective.
