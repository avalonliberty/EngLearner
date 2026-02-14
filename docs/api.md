# API Reference

## Endpoints

### Vocabulary Management

#### POST /api/v1/vocabularies
Add a vocabulary to the review queue.

**Request:**
```json
{
  "word": "ephemeral",
  "definition": "lasting for a very short time",
  "example": "The ephemeral beauty of cherry blossoms"
}
```

**Response:**
```json
{
  "id": "uuid",
  "word": "ephemeral",
  "definition": "lasting for a very short time",
  "example": "The ephemeral beauty of cherry blossoms",
  "current_day_index": 0,
  "next_review_date": "2026-02-16",
  "status": "reviewing",
  "streak_count": 0
}
```

#### GET /api/v1/vocabularies
Get all vocabularies in the review queue.

#### GET /api/v1/vocabularies/due
Get vocabularies due for review today.

#### POST /api/v1/vocabularies/{id}/review
Submit a review answer.

**Request:**
```json
{
  "correct": true
}
```
