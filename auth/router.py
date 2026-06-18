from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.schemas import SignUpSchema
from auth.services import create_user
from core.database import get_db

router = APIRouter(
    prefix='/api/auth',
    tags=['Authentication']
)

@router.post('/signup')
def signup(
    payload: SignUpSchema,
    db: Session = Depends(get_db)
):

    user = create_user(payload, db)
    return {
        "success": True,
        "message": "User created successfully",
        "user": user
    }