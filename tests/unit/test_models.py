import pytest
from datetime import date, datetime
from pydantic import ValidationError

from englearner.api.models import (
    VocabularyCreate,
    VocabularyResponse,
    ReviewSubmit,
    ReviewResponse,
)


class TestVocabularyCreate:
    def test_valid_vocabulary(self):
        vocab = VocabularyCreate(
            word="ephemeral",
            definition="lasting a very short time",
            example="The ephemeral beauty of cherry blossoms",
        )
        assert vocab.word == "ephemeral"
        assert vocab.definition == "lasting a very short time"
        assert vocab.example == "The ephemeral beauty of cherry blossoms"

    def test_vocabulary_without_example(self):
        vocab = VocabularyCreate(word="test", definition="a test definition")
        assert vocab.word == "test"
        assert vocab.example is None

    def test_vocabulary_empty_word_fails(self):
        with pytest.raises(ValidationError):
            VocabularyCreate(word="", definition="test")

    def test_vocabulary_empty_definition_fails(self):
        with pytest.raises(ValidationError):
            VocabularyCreate(word="test", definition="")


class TestReviewSubmit:
    def test_correct_true(self):
        review = ReviewSubmit(correct=True)
        assert review.correct is True

    def test_correct_false(self):
        review = ReviewSubmit(correct=False)
        assert review.correct is False


class TestVocabularyResponse:
    def test_vocabulary_response(self):
        vocab = VocabularyResponse(
            id="test-uuid",
            word="test",
            definition="test definition",
            example="example",
            user_id="user-uuid",
            current_day_index=0,
            next_review_date=date.today(),
            status="reviewing",
            streak_count=0,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        )
        assert vocab.id == "test-uuid"
        assert vocab.current_day_index == 0

    def test_current_day_index_bounds(self):
        with pytest.raises(ValidationError):
            VocabularyResponse(
                id="test-uuid",
                word="test",
                definition="test",
                user_id="user-uuid",
                current_day_index=7,
                next_review_date=date.today(),
                status="reviewing",
                streak_count=0,
                created_at="",
                updated_at="",
            )


class TestReviewResponse:
    def test_review_response_with_reset(self):
        vocab = VocabularyResponse(
            id="test-uuid",
            word="test",
            definition="test",
            example="test example",
            user_id="user-uuid",
            current_day_index=0,
            next_review_date=date.today(),
            status="reviewing",
            streak_count=0,
            created_at="",
            updated_at="",
        )
        response = ReviewResponse(
            vocabulary=vocab, reset=True, message="Progress reset - starting from day 1"
        )
        assert response.reset is True
        assert response.message == "Progress reset - starting from day 1"

    def test_review_response_without_reset(self):
        vocab = VocabularyResponse(
            id="test-uuid",
            word="test",
            definition="test",
            example="test example",
            user_id="user-uuid",
            current_day_index=1,
            next_review_date=date.today(),
            status="reviewing",
            streak_count=1,
            created_at="",
            updated_at="",
        )
        response = ReviewResponse(
            vocabulary=vocab, reset=False, message="Progress advanced!"
        )
        assert response.reset is False
