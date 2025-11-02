from typing import Annotated
from fastapi import Depends, Request
from jose import JWTError, jwt
from src.app.models.user import User
from src.app.repositories.user_repository import UserRepository
from src.core.auth_token_config import auth_token_settings
from src.app.database import DbSession
from src.app.exceptions.user_exceptions import TokenException

async def get_current_user(
    request: Request,
    session: DbSession
):
    token = request.cookies.get("access_token")
    if not token:
        token = request.headers.get("Authorization")
        # if authorization and authorization.startswith("Bearer "):
        #     token = authorization[7:]
    if not token:
        raise TokenException(detail="Token required")
    try:
        payload = jwt.decode(token, auth_token_settings.JWT_SECRET_KEY, algorithms=[auth_token_settings.JWT_ALG])
        user_id = payload.get('sub')
    except JWTError:
        raise TokenException(detail="Could not validate user")
    if not user_id:
        raise TokenException(detail="Invalid token payload")
    user = await UserRepository(session).get(
        user_id=int(user_id)
    )
    if not user:
        raise TokenException(detail="User not found")
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]