## Why

Supabase is deprecating the legacy JWT-based anon and service_role API keys in favor of a new API key system that improves security and key management. The legacy keys are tied to a single JWT secret that cannot be rotated without breaking all applications, while the new system provides revocable, individually manageable keys following industry best practices.

## What Changes

- Replace legacy `SUPABASE_KEY` (anon JWT) with new `SUPABASE_PUBLISHABLE_KEY` (sb_publishable_...)
- Replace legacy `SUPABASE_SERVICE_KEY` (service_role JWT) with `SUPABASE_SECRET_KEY` (sb_secret_...)
- Update Python Supabase client initialization in `src/englearner/core/supabase.py`
- Update environment variable documentation in `.env.example` and `SETUP.md`
- Remove dependency on JWT secret for verification (no longer needed with new key system)

## Capabilities

### New Capabilities
- `supabase-api-key-migration`: Complete migration from legacy to new Supabase API key system

### Modified Capabilities
(None - this is a straightforward credential update)

## Impact

- **Code changes**: Update `src/englearner/core/supabase.py` client initialization
- **Configuration**: Update `.env`, `.env.example`, and `SETUP.md` documentation
- **Authentication**: Simplify JWT verification logic in `src/englearner/core/auth.py` (JWT secret no longer needed)
- **Dependencies**: No new dependencies - Python supabase library already supports new keys
- **Requirement**: Existing deployments must update to new API keys