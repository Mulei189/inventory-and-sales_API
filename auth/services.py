from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .models import User
from .schemas import SignUpSchema
from core.security import hash_password


def create_user(payload, db: Session):
    data = payload.model_dump()

    existing_user = (
        db.query(User)
        .filter(User.email == data["email"])
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    data["password"] = hash_password(data["password"])

    user = User(**data)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user