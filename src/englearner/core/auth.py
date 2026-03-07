from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from .supabase import get_supabase_client

security = HTTPBearer()
_supabase = get_supabase_client()


class User(BaseModel):
    id: str
    email: Optional[str] = None


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    """Verify JWT token and extract user ID."""
    token = credentials.credentials

    try:
        user_response = _supabase.auth.get_user(token)
        user = user_response.user
        return User(id=user.id, email=user.email)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}",
        )


def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(
        HTTPBearer(auto_error=False)
    ),
) -> Optional[User]:
    """Get current user if authenticated, otherwise return None."""
    if credentials is None:
        return None

    try:
        return Depends(get_current_user)(credentials)
    except HTTPException:
        return None
