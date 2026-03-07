from fastapi import APIRouter, Depends, HTTPException, status

from ..core.auth import User, get_current_user
from ..core.supabase import supabase, get_supabase_admin_client
from .models import VocabularyCreate, VocabularyResponse, ReviewSubmit, ReviewResponse
from .vocabulary import VocabularyService

router = APIRouter(prefix="/api/v1/vocabularies", tags=["vocabularies"])


def get_vocabulary_service() -> VocabularyService:
    return VocabularyService(supabase)


def get_admin_vocabulary_service() -> VocabularyService:
    return VocabularyService(get_supabase_admin_client())


@router.post("", response_model=VocabularyResponse, status_code=status.HTTP_201_CREATED)
async def create_vocabulary(
    vocab_data: VocabularyCreate,
    current_user: User = Depends(get_current_user),
    service: VocabularyService = Depends(get_vocabulary_service),
):
    """Add a vocabulary to the review queue."""
    return service.create_vocabulary(current_user.id, vocab_data)


@router.get("", response_model=list[VocabularyResponse])
async def get_vocabularies(
    current_user: User = Depends(get_current_user),
    service: VocabularyService = Depends(get_vocabulary_service),
):
    """Get all vocabularies in the review queue."""
    return service.get_vocabularies(current_user.id)


@router.get("/due", response_model=list[VocabularyResponse])
async def get_due_vocabularies(
    current_user: User = Depends(get_current_user),
    service: VocabularyService = Depends(get_vocabulary_service),
):
    """Get vocabularies due for review today or overdue."""
    return service.get_due_vocabularies(current_user.id)


@router.post("/{vocabulary_id}/review", response_model=ReviewResponse)
async def submit_review(
    vocabulary_id: str,
    review: ReviewSubmit,
    current_user: User = Depends(get_current_user),
    service: VocabularyService = Depends(get_vocabulary_service),
):
    """Submit a review answer for a vocabulary."""
    try:
        return service.submit_review(current_user.id, vocabulary_id, review)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/test/create", response_model=VocabularyResponse, status_code=status.HTTP_201_CREATED)
async def create_vocabulary_test(
    vocab_data: VocabularyCreate,
    service: VocabularyService = Depends(get_admin_vocabulary_service),
):
    """Test endpoint to add a vocabulary without authentication (for testing only)."""
    test_user_id = "test-user-123"
    return service.create_vocabulary(test_user_id, vocab_data)
