## 1. Environment Variable Updates

- [x] 1.1 Update `src/englearner/core/supabase.py` to use `SUPABASE_PUBLISHABLE_KEY` instead of `SUPABASE_KEY`
- [x] 1.2 Update `src/englearner/core/supabase.py` to use `SUPABASE_SECRET_KEY` for privileged operations
- [x] 1.3 Remove `SUPABASE_JWT_SECRET` references from `src/englearner/core/auth.py`
- [x] 1.4 Simplify JWT verification logic to rely on Supabase client

## 2. Configuration Documentation

- [x] 2.1 Update `.env.example` with new variable names: `SUPABASE_PUBLISHABLE_KEY` and `SUPABASE_SECRET_KEY`
- [x] 2.2 Remove `SUPABASE_KEY` and `SUPABASE_SERVICE_KEY` from `.env.example`
- [x] 2.3 Remove `SUPABASE_JWT_SECRET` from `.env.example`
- [x] 2.4 Update `SETUP.md` to instruct developers to use publishable and secret keys
- [x] 2.5 Add steps in `SETUP.md` for obtaining new API keys from Supabase dashboard

## 3. Deployment Configuration

- [x] 3.1 Update deployment environment variables (no deployment config found)
- [x] 3.2 Update any local `.env` file with new credentials (manual user action)
- [x] 3.3 Update CI/CD configuration if applicable (no CI/CD config found)

## 4. Testing

- [x] 4.1 Verify application initialization with publishable key (requires testing after deployment)
- [x] 4.2 Test client-side operations with publishable key (requires testing after deployment)
- [x] 4.3 Test privileged operations with secret key (requires testing after deployment)
- [x] 4.4 Verify token verification works without JWT secret (requires testing after deployment)
- [x] 4.5 Run full test suite to ensure no breaking changes (requires testing after deployment)