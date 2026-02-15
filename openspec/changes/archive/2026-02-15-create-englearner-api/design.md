## Context

EngLearner is a new vocabulary learning application. This is the initial API implementation for the vocabulary review feature. There is no existing backend - this is a greenfield project.

The core feature is a Fibonacci-based spaced repetition system (SRS) for vocabulary review:
- Users add vocabularies to a review queue
- Review intervals follow Fibonacci sequence: 1, 2, 3, 5, 8, 13, 21 days
- Correct answers advance to the next interval
- Incorrect answers reset progress to day 1

## Goals / Non-Goals

**Goals:**
- Create RESTful API endpoints for vocabulary review queue management
- Implement Fibonacci-based scheduling logic
- Track user progress through review cycles
- Handle automatic reset on failed reviews
- Provide review status and next review date

**Non-Goals:**
- Multiple vocabulary lists/folders (future work)
- Analytics or statistics (future work)
- Import/export functionality (future work)

## Decisions

### Decision 1: API Framework - FastAPI

Chosen FastAPI over Flask/Django for:
- Built-in OpenAPI/Swagger documentation
- Native async support for better performance
- Pydantic for automatic request/response validation
- Minimal boilerplate compared to Django

### Decision 2: Project Management - uv

Using uv as the Python package manager and project tool:
- Fast dependency resolution (written in Rust)
- Unified tool management (run, test, lint all in one)
- Works with pyproject.toml directly
- Better than pip/poetry for this project's scale

```bash
# Commands used
uv run fastapi dev      # Development server
uv add <package>        # Add dependencies
uv test                 # Run tests
uvx <tool>              # Run one-off tools
```

### Decision 3: Testing Framework - pytest

Using pytest as the main testing framework:
- Industry-standard Python testing
- Simple test discovery (test_*.py files)
- Rich fixtures and parametrize support
- FastAPI TestClient integration for API testing

```bash
# Commands
uv test                 # Run all tests
uv test -v             # Verbose output
uv test -k "fibonacci" # Run tests matching pattern
```

**Test Structure:**
```
tests/
├── unit/
│   ├── test_fibonacci.py
│   └── test_models.py
├── api/
│   └── test_vocabulary_api.py
└── conftest.py        # Shared fixtures
```

**Coverage Target:** All business logic (Fibonacci calculations, progress tracking)

### Decision 4: Database - Supabase (PostgreSQL)

Using Supabase (managed PostgreSQL) for data storage:
- Fully managed database - no server maintenance required
- Built-in row-level security (RLS) for data isolation
- Real-time subscriptions available for future features
- Easy to set up and scale
- Supabase client libraries for Python

### Decision 5: Authentication - Supabase Auth

Using Supabase's built-in authentication:
- JWT-based stateless authentication
- Built-in user management (signup, login, logout)
- Supports email/password and magic links
- Token passed via `Authorization: Bearer <token>` header
- User ID extracted from JWT for RLS policies

```
┌─────────────────────────────────────────────────┐
│              Authentication Flow                  │
├─────────────────────────────────────────────────┤
│                                                  │
│   Web UI                                          │
│      │                                            │
│      ▼                                            │
│   POST /auth/signup  ──▶  Supabase Auth          │
│      │                                            │
│      │  { access_token, refresh_token }          │
│      ▼                                            │
│   Store token in localStorage/session            │
│      │                                            │
│      ▼                                            │
│   API requests include:                          │
│   Authorization: Bearer <jwt_token>              │
│      │                                            │
│      ▼                                            │
│   FastAPI validates token, extracts user_id      │
│      │                                            │
│      ▼                                            │
│   Supabase queries use RLS to filter            │
│   by user_id = auth.uid()                        │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Why Supabase Auth:**
- Tightly integrated with Supabase database
- Free tier supports our expected usage (< 10 users)
- Magic links = no passwords to manage
- Built-in JWT validation via Supabase SDK

### Decision 6: Fibonacci Sequence Storage

The Fibonacci sequence [1, 2, 3, 5, 8, 13, 21] is stored as a constant in code rather than database:
- Sequence is fixed and well-known
- No need for runtime configuration
- Simple to modify in code if needed

### Decision 7: Progress Tracking - Day Counter + Status

Track progress using:
- `current_day_index`: Integer (0-6) representing position in Fibonacci sequence
- `next_review_date`: Date when the next review is due
- `status`: pending/reviewing/completed

This approach:
- Allows easy calculation of next interval
- Simplifies reset logic (just set current_day_index to 0)
- Enables querying "due" vocabularies efficiently

### Decision 8: API Documentation - MkDocs + Swagger UI

Using dual documentation approach for developer reference:

**FastAPI Built-in (Swagger UI):**
- Available at `/docs` - auto-generated from code
- Try-out functionality directly in browser
- Shows request/response schemas, examples

**MkDocs (Static Docs):**
- Available at `/mkdocs` or as separate static site
- Written documentation for concepts, architecture
- Setup guides, authentication flow explanation
- Deployment instructions

```bash
# Commands
uvx mkdocs serve          # Local docs server
uvx mkdocs build          # Build static site
```

**Why both:**
- Swagger = quick API reference, try endpoints
- MkDocs = conceptual docs, onboarding, architecture
- MkDocs can be served from same app or deployed separately

### Decision 9: Git Workflow - Git Flow

Using Git Flow for branch management and releases:

```
┌─────────────────────────────────────────────────────────────┐
│                    Git Flow Branches                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  main ──────●────────────────●────────────────●──────►      │
│             │                │                │              │
│             │    release/   │                │              │
│  develop ───●──────●────●───●──────●────●─────●──────►    │
│             │    v1.0   │   │    v1.1   │                 │
│             │            │   │            │                 │
│             ▼            ▼   ▼            ▼                 │
│        feature/       hotfix/       feature/                │
│        vocab-api      bug-fix       other                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Branch Types:**
- `main` - Production-ready code, tagged releases
- `develop` - Integration branch for next release
- `feature/*` - New features (from develop)
- `release/*` - Preparing for production release
- `hotfix/*` - Urgent fixes (from main)

**Workflow:**
1. Create feature branch from develop: `git checkout -b feature/vocab-api develop`
2. Implement and commit changes
3. Merge to develop via PR
4. Create release branch when ready
5. Merge release to main and develop

**Commands:**
```bash
# Start new feature
git checkout -b feature/vocab-api develop

# Finish feature
git checkout develop
git merge --no-ff feature/vocab-api
git push
git branch -d feature/vocab-api
```

## Risks / Trade-offs

- **[Risk] Token expiration** → Implement token refresh logic in frontend; API returns 401 on expired tokens
- **[Risk] Timezone handling** → Store all dates in UTC, convert to user's timezone in API responses
- **[Risk] Date precision** → Use date-only (no time) for review scheduling to avoid edge cases around midnight
- **[Risk] Empty queue handling** → Return empty array with 200 status, not 404
- **[Risk] Concurrent updates** → Use database transactions for progress updates to prevent race conditions
