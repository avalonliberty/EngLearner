from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class VocabularyCreate(BaseModel):
    word: str = Field(..., min_length=1, description="The vocabulary word")
    definition: str = Field(..., min_length=1, description="Definition of the word")
    example: Optional[str] = Field(None, description="Example sentence using the word")


class VocabularyResponse(BaseModel):
    id: str
    word: str
    definition: str
    example: Optional[str]
    user_id: str
    current_day_index: int = Field(ge=0, le=6)
    next_review_date: date
    status: str
    streak_count: int = Field(ge=0)
    created_at: str
    updated_at: str


class ReviewSubmit(BaseModel):
    correct: bool = Field(..., description="Whether the answer was correct")


class ReviewResponse(BaseModel):
    vocabulary: VocabularyResponse
    reset: bool = False
    message: Optional[str] = None
