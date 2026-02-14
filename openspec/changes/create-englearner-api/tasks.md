## 0. Git Flow Setup

- [x] 0.1 Ensure main and develop branches exist
- [x] 0.2 Create feature branch: `git checkout -b feature/vocab-api develop`
- [x] 0.3 Configure branch protection rules for main/develop

## 1. Project Setup

- [x] 1.1 Initialize FastAPI project with dependencies
- [x] 1.2 Configure Supabase client (database + auth)
- [x] 1.3 Set up environment variables for Supabase credentials (SUPABASE_URL, SUPABASE_KEY)
- [x] 1.4 Set up MkDocs configuration (mkdocs.yml)
- [x] 1.5 Create initial docs structure (index.md, api.md, auth.md)

## 2. Authentication

- [x] 2.1 Enable Supabase Auth in Supabase dashboard
- [x] 2.2 Create JWT verification dependency in FastAPI
- [x] 2.3 Extract user_id from JWT token in protected endpoints
- [x] 2.4 Add authentication middleware/dependency to all vocabulary endpoints

## 3. Database Schema

- [x] 3.1 Create vocabularies table in Supabase
- [x] 3.2 Define column types: id, word, definition, example, user_id, current_day_index, next_review_date, status, streak_count, created_at, updated_at
- [x] 3.3 Enable Row Level Security (RLS) policies
- [x] 3.4 Create RLS policy: users can only see their own vocabularies

## 4. API Models

- [x] 4.1 Create Pydantic models for vocabulary request/response
- [x] 4.2 Create ReviewSubmit model

## 5. Vocabulary Queue Endpoints

- [x] 5.1 Implement POST /api/v1/vocabularies - Add vocabulary to queue
- [x] 5.2 Implement GET /api/v1/vocabularies - Get all vocabularies
- [x] 5.3 Implement GET /api/v1/vocabularies/due - Get due vocabularies

## 6. Review Progress Endpoints

- [x] 6.1 Implement POST /api/v1/vocabularies/{id}/review - Submit review answer
- [x] 6.2 Implement Fibonacci sequence calculation logic
- [x] 6.3 Implement progress advancement on correct answer
- [x] 6.4 Implement progress reset on incorrect answer

## 7. Unit Tests (pytest)

- [x] 7.1 Install pytest and configure pyproject.toml
- [x] 7.2 Create test directory structure (tests/unit/, tests/api/)
- [x] 7.3 Write unit tests for Fibonacci sequence calculation
- [x] 7.4 Write unit tests for progress tracking (advancement, reset)
- [x] 7.5 Write unit tests for Pydantic models validation

## 8. Verification

- [ ] 8.1 Test user signup/login flow with Supabase Auth
- [ ] 8.2 Test protected endpoints with Bearer token
- [ ] 8.3 Verify RLS - ensure users can't access other users' data
- [ ] 8.4 Test API endpoints with curl or Postman
- [ ] 8.5 Verify Supabase data storage

## 9. Merge Feature Branch

- [x] 9.1 Run all tests and ensure passing
- [ ] 9.2 Create pull request to develop branch
- [ ] 9.3 Get code review approval
- [ ] 9.4 Merge feature branch to develop
- [ ] 9.5 Delete feature branch
