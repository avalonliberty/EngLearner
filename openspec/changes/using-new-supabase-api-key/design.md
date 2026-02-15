## Context

The application currently uses Supabase's legacy JWT-based API keys (anon and service_role) which are tied to a single JWT secret. Supabase has announced deprecation of these keys in favor of a new API key system with individual revocable keys. The Python Supabase client library already supports the new key format.

Current implementation:
- `SUPABASE_KEY` environment variable: anon JWT key
- `SUPABASE_SERVICE_KEY` environment variable: service_role JWT key
- `SUPABASE_JWT_SECRET` environment variable: for token verification
- Client initialized in `src/englearner/core/supabase.py`
- JWT verification in `src/englearner/core/auth.py`

## Goals / Non-Goals

**Goals:**
- Migrate to Supabase's new API key system without breaking existing functionality
- Simplify authentication by removing JWT secret dependency
- Update all configuration documentation

**Non-Goals:**
- Changing authentication logic beyond credential migration
- Modifying application features or API behavior
- Revoking existing keys during migration

## Decisions

**Direct credential replacement**
- Replace `SUPABASE_KEY` and `SUPABASE_SERVICE_KEY` with `SUPABASE_PUBLISHABLE_KEY` and `SUPABASE_SECRET_KEY`
- **Rationale**: Supabase's documentation shows exact substitution - the new keys work identically with the client library. This provides the simplest migration path.

**Remove JWT secret dependency**
- Remove `SUPABASE_JWT_SECRET` from environment and verification logic
- **Rationale**: The new key system uses individual revocable keys, removing the need for JWT secret-based verification. The supabase client handles authentication internally.

**Zero-downtime deployment**
- Deploy configuration changes during transition period where both key systems work
- **Rationale**: Supabase supports legacy and new keys simultaneously during migration, allowing safe deployment without service interruption.

**Documentation updates**
- Keep variable names self-documenting while following Supabase's naming conventions
- **Rationale**: Using `SUPABASE_PUBLISHABLE_KEY` and `SUPABASE_SECRET_KEY` maintains clarity and aligns with Supabase documentation.

## Risks / Trade-offs

**Risk: Missing environment variable updates** → Mitigation: Update all configuration files (`.env`, `.env.example`, `SETUP.md`) in the same commit to ensure consistency.

**Risk: Breaking existing deployments** → Mitigation: Use Supabase's transition period where legacy keys remain valid. Deploy and test with new keys before removing old ones from configuration.

**Trade-off: Simplification vs. future-proofing** → Using new key system provides better security and key management but requires configuration updates for existing deployments.

## Migration Plan

1. Update environment variables in application code
2. Update configuration documentation (`.env.example`, `SETUP.md`)
3. Remove JWT secret references from initialization
4. Test with publishable key for client operations
5. Create rotation procedure for future secret key updates

## Migration Plan

1. Update environment variables in application code
2. Update configuration documentation (`.env.example`, `SETUP.md`)
3. Remove JWT secret references from initialization
4. Update deployment configuration

## Open Questions

None - this is a straightforward credential migration with clear documentation from Supabase.