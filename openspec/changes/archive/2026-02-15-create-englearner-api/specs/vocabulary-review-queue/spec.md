## ADDED Requirements

### Requirement: User can add vocabulary to review queue
The system SHALL allow users to add a vocabulary to their review queue with Fibonacci-based scheduling. Upon addition, the vocabulary SHALL be scheduled for first review in 1 day.

#### Scenario: Successfully add vocabulary to queue
- **WHEN** user calls POST /api/v1/vocabularies with vocabulary data (word, definition, example)
- **THEN** the system creates a new vocabulary record in Supabase
- **AND** sets current_day_index to 0 (representing day 1 in Fibonacci sequence)
- **AND** sets next_review_date to tomorrow's date
- **AND** returns the created vocabulary with status "reviewing"

#### Scenario: Add vocabulary with missing required fields
- **WHEN** user calls POST /api/v1/vocabularies without required field "word"
- **THEN** the system returns HTTP 422 validation error
- **AND** includes error message indicating missing field

### Requirement: User can retrieve all vocabularies in review queue
The system SHALL allow users to retrieve all vocabularies currently in their review queue, ordered by next_review_date.

#### Scenario: Get all vocabularies
- **WHEN** user calls GET /api/v1/vocabularies
- **THEN** the system returns all vocabularies for the user
- **AND** orders them by next_review_date ascending (earliest first)
- **AND** includes current_day_index and next_review_date for each

#### Scenario: Get vocabularies when queue is empty
- **WHEN** user calls GET /api/v1/vocabularies and no vocabularies exist
- **THEN** the system returns an empty array with HTTP 200

### Requirement: User can get vocabularies due for review
The system SHALL allow users to retrieve vocabularies that are due for review today or overdue.

#### Scenario: Get due vocabularies
- **WHEN** user calls GET /api/v1/vocabularies/due
- **THEN** the system returns vocabularies where next_review_date <= today
- **AND** orders them by next_review_date ascending (oldest overdue first)
