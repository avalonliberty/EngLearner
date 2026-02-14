# Welcome to EngLearner API

EngLearner is a vocabulary learning application that uses a Fibonacci-based spaced repetition system (SRS) to help learners memorize vocabularies effectively.

## Core Features

- **Fibonacci-based scheduling**: Review intervals follow the sequence 1, 2, 3, 5, 8, 13, 21 days
- **Progress tracking**: Track your learning progress through each review cycle
- **Automatic reset**: Progress resets to day 1 if you fail to answer correctly

## Quick Start

1. Set up Supabase credentials in `.env`
2. Run the API server: `uv run fastapi dev`
3. Access Swagger docs at `/docs`

## Architecture

- **FastAPI**: Modern Python web framework
- **Supabase**: Database and authentication
- **Pytest**: Testing framework
