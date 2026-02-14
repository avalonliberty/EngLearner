from datetime import date
from typing import List, Optional
from supabase import Client

from ..core.fibonacci import (
    calculate_next_review_date,
    advance_progress,
    reset_progress,
    is_completed,
)
from .models import VocabularyCreate, VocabularyResponse, ReviewSubmit, ReviewResponse


class VocabularyService:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def create_vocabulary(
        self, user_id: str, vocab_data: VocabularyCreate
    ) -> VocabularyResponse:
        """Add a vocabulary to the review queue."""
        today = date.today()
        next_review = calculate_next_review_date(0, today)

        data = {
            "word": vocab_data.word,
            "definition": vocab_data.definition,
            "example": vocab_data.example,
            "user_id": user_id,
            "current_day_index": 0,
            "next_review_date": next_review.isoformat(),
            "status": "reviewing",
            "streak_count": 0,
        }

        result = self.supabase.table("vocabularies").insert(data).execute()
        return VocabularyResponse(**result.data[0])

    def get_vocabularies(self, user_id: str) -> List[VocabularyResponse]:
        """Get all vocabularies for a user, ordered by next_review_date."""
        result = (
            self.supabase.table("vocabularies")
            .select("*")
            .eq("user_id", user_id)
            .order("next_review_date")
            .execute()
        )
        return [VocabularyResponse(**item) for item in result.data]

    def get_due_vocabularies(self, user_id: str) -> List[VocabularyResponse]:
        """Get vocabularies that are due for review today or overdue."""
        today = date.today().isoformat()

        result = (
            self.supabase.table("vocabularies")
            .select("*")
            .eq("user_id", user_id)
            .lte("next_review_date", today)
            .order("next_review_date")
            .execute()
        )
        return [VocabularyResponse(**item) for item in result.data]

    def submit_review(
        self, user_id: str, vocabulary_id: str, review: ReviewSubmit
    ) -> ReviewResponse:
        """Submit a review answer and update progress."""
        result = (
            self.supabase.table("vocabularies")
            .select("*")
            .eq("id", vocabulary_id)
            .eq("user_id", user_id)
            .execute()
        )

        if not result.data:
            raise ValueError("Vocabulary not found")

        vocab = result.data[0]
        current_index = vocab["current_day_index"]
        streak = vocab["streak_count"]

        if review.correct:
            new_index = advance_progress(current_index)
            if new_index == -1:
                new_status = "completed"
                new_index = current_index
            else:
                new_status = "reviewing"

            next_review = calculate_next_review_date(new_index)
            streak += 1

            update_data = {
                "current_day_index": new_index,
                "next_review_date": next_review.isoformat(),
                "status": new_status,
                "streak_count": streak,
            }

            message = (
                "Progress advanced!"
                if new_status != "completed"
                else "Vocabulary completed!"
            )

        else:
            new_index = reset_progress()
            next_review = calculate_next_review_date(new_index)

            update_data = {
                "current_day_index": new_index,
                "next_review_date": next_review.isoformat(),
                "status": "reviewing",
                "streak_count": 0,
            }

            message = "Progress reset - starting from day 1"

        updated = (
            self.supabase.table("vocabularies")
            .update(update_data)
            .eq("id", vocabulary_id)
            .execute()
        )

        return ReviewResponse(
            vocabulary=VocabularyResponse(**updated.data[0]),
            reset=not review.correct,
            message=message,
        )
