# Setup Instructions

This document contains manual setup steps that need to be completed in external services.

## Supabase Setup

### 1. Enable Supabase Auth
1. Go to [Supabase Dashboard](https://supabase.com/dashboard)
2. Select your project
3. Go to **Authentication** → **Providers**
4. Enable **Email** provider (or any provider you want to use)
5. Configure settings as needed

### 2. Run Database Migration
1. Go to **SQL Editor** in Supabase
2. Copy and paste the contents of `supabase/migrations/001_create_vocabularies.sql`
3. Run the SQL

### 3. Get Credentials
1. Go to **Project Settings** → **API Keys**
2. Click **Create new API Keys** if you don't have them
3. Copy:
    - **Project URL** → set as `SUPABASE_URL` in `.env`
    - **Publishable key** (format: `sb_publishable_...`) → set as `SUPABASE_PUBLISHABLE_KEY` in `.env`
    - **Secret key** (format: `sb_secret_...`) → set as `SUPABASE_SECRET_KEY` in `.env`

## GitHub Setup

### Configure Branch Protection
1. Go to your GitHub repository
2. Go to **Settings** → **Branches**
3. Add rule for `main`:
   - Require pull request reviews before merging
   - Require status checks to pass before merging
   - Include administrators
4. Add same rule for `develop`

## Environment Variables

Create a `.env` file:
```bash
SUPABASE_URL=your_supabase_url
SUPABASE_PUBLISHABLE_KEY=your_supabase_publishable_key
SUPABASE_SECRET_KEY=your_supabase_secret_key
```

## Run the API

```bash
uv run fastapi dev
```

API will be available at `http://localhost:8000`
Swagger docs at `http://localhost:8000/docs`
