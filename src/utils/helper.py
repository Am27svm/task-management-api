from fastapi import Request,HTTPException,status,Depends
from src.utils.settings import settings
from sqlalchemy.orm import Session
import jwt
from src.user.models import UserModel
from src.utils.db import get_db



def is_authenticated(request: Request, db: Session=Depends(get_db)):
    try:
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization header missing"
            )
        token = token.split(" ")[-1]
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = data.get("_id")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You are Unauthorized..."
            )
        return user
    except jwt.InvalidTokenError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="You are Unauthorized..."
            )