# KIRO AGENTIC RULES — TECHMINDDEV
# Steering rules for Kiro IDE and custom agents

## 1. Core Architecture
- Follow Feature-First domain separation (`features/{feature}/{presentation, data, domain}`).
- Maximum 200 lines per file.

## 2. API Quota & Anti-Ban Protections
- Cache all external API responses (YouTube, OpenAI, Google Maps) in Redis/Local DB for at least 12 hours.
- Implement request batching and rate limiting (max 2 req/s).
- Apply exponential backoff with jitter on status 429/403.

## 3. Database & Security
- Enable RLS on all Postgres tables.
- Use UUIDv7 for primary keys.
- Never commit `.env` or expose private keys to client bundles.
