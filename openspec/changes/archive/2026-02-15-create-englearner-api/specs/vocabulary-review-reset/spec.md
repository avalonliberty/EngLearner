## ADDED Requirements

### Requirement: Incorrect answer resets progress to day 1
The system SHALL reset vocabulary progress to the beginning (day 1) when user answers incorrectly.

#### Scenario: Reset after incorrect answer
- **WHEN** user submits incorrect answer for vocabulary at any current_day_index > 0
- **THEN** current_day_index resets to 0
- **AND** next_review_date is recalculated as today + Fibonacci[0] = today + 1 day
- **AND** streak_count resets to 0
- **AND** the vocabulary returns to the beginning of the review cycle

### Requirement: System provides feedback about reset
The system SHALL communicate to the user that their progress has been reset due to an incorrect answer.

#### Scenario: Review response indicates reset occurred
- **WHEN** user submits incorrect answer
- **THEN** the API response includes reset: true
- **AND** message indicates "Progress reset - starting from day 1"
