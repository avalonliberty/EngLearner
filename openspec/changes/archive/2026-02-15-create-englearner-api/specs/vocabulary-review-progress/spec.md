## ADDED Requirements

### Requirement: System tracks progress through Fibonacci sequence
The system SHALL track each vocabulary's current position in the Fibonacci review sequence using current_day_index (0-6).

#### Scenario: Initial state after adding vocabulary
- **WHEN** vocabulary is added to queue
- **THEN** current_day_index is set to 0
- **AND** next_review_date is calculated as today + Fibonacci[0] = today + 1 day

### Requirement: Correct answer advances to next Fibonacci interval
The system SHALL advance the vocabulary to the next Fibonacci interval when user answers correctly.

#### Scenario: Correct answer at day 1 (index 0)
- **WHEN** user answers correctly for vocabulary at current_day_index = 0
- **THEN** current_day_index increments to 1
- **AND** next_review_date is recalculated as today + Fibonacci[1] = today + 2 days
- **AND** streak_count increments by 1

#### Scenario: Correct answer at day 2 (index 1)
- **WHEN** user answers correctly for vocabulary at current_day_index = 1
- **THEN** current_day_index increments to 2
- **AND** next_review_date is recalculated as today + Fibonacci[2] = today + 3 days

#### Scenario: Correct answer at final interval (index 6)
- **WHEN** user answers correctly for vocabulary at current_day_index = 6 (21 days)
- **THEN** vocabulary status changes to "completed"
- **AND** current_day_index remains at 6
- **AND** no further reviews are scheduled

### Requirement: User can submit review answer
The system SHALL accept user's answer for a vocabulary review and determine if it is correct or incorrect.

#### Scenario: Submit correct answer
- **WHEN** user calls POST /api/vocabularies/{id}/review with correct=true
- **THEN** the system marks the answer as correct
- **AND** advances progress to next Fibonacci interval
- **AND** returns updated vocabulary with new next_review_date

#### Scenario: Submit incorrect answer
- **WHEN** user calls POST /api/vocabularies/{id}/review with correct=false
- **THEN** the system marks the answer as incorrect
- **AND** triggers progress reset (see vocabulary-review-reset)
