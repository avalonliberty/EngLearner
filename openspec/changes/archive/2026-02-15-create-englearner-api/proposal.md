## Why

Learners need an effective way to memorize vocabularies over time. Current systems often use fixed intervals (e.g., 1, 3, 7 days), which may not be optimal for long-term retention. A Fibonacci-based spaced repetition system (1, 2, 3, 5, 8, 13, 21 days) provides more natural spacing that adapts to the learner's retention curve, improving long-term memory retention.

## What Changes

- Add a new API endpoint to receive vocabularies for future review
- Implement Fibonacci-based scheduling logic (1, 2, 3, 5, 8, 13, 21 days)
- Track user progress through review cycles
- Reset progress to day 1 when users fail to answer correctly
- Provide review status and next review date for each vocabulary

## Capabilities

### New Capabilities
- `vocabulary-review-queue`: API to add vocabularies to the review queue with Fibonacci-based scheduling
- `vocabulary-review-progress`: Track and manage user's review progress for each vocabulary
- `vocabulary-review-reset`: Handle automatic reset to day 1 when users fail a review

### Modified Capabilities
- None (new capability)

## Impact

- New API endpoints for vocabulary management
- New database models for tracking review progress
- New service logic for Fibonacci scheduling
