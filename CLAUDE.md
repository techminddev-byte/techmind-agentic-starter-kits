# CLAUDE.md — TechMindDev Agentic Guidelines

This file provides system instructions for Claude Code and Agentic workflows.

## 1. Architecture & Clean Code
- Follow Clean Architecture: `domain` (pure), `application` (use cases), `infrastructure` (db/apis), `presentation` (ui/controllers).
- Hard limit: Maximum **200 lines per file** and **40 lines per function**. Never create God Files.
- Program against Interfaces: Always inject I/O dependencies via interfaces/ports.
- 1 file per Use Case with a single public `execute()` method.

## 2. Database & Performance
- Primary Keys: Always use **UUIDv7** (`uuid_generate_v7()`) or **ULID**. Avoid random UUIDv4 in B-Trees.
- Zero N+1 Queries: Never run queries inside loops. Use `JOIN` or `IN (...)`.
- Serverless Pooling: Connect via connection pooler port (`6543`) in serverless environments.

## 3. Semantic Versioning & Commits
- Follow **SemVer 2.0.0** (`MAJOR.MINOR.PATCH`).
- Enforce Conventional Commits (`feat:`, `fix:`, `feat!:` for breaking changes).
- Maintain `CHANGELOG.md` updated per release.

## 4. Mobile & Flutter
- In `pubspec.yaml`, use `version: MAJOR.MINOR.PATCH+BUILD_NUMBER`.
- Display real version via `PackageInfo` on login/settings screen.
- When builds are stale, run `flutter clean && flutter pub get` and `./gradlew clean`.

## 5. Security & Error Handling
- Never swallow exceptions with empty `catch` blocks.
- Strict typing: No `any` in TypeScript; use Pydantic/TypedDict in Python.
- Validate all incoming I/O with Zod schemas.
