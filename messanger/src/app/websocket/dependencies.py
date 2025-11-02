from jose import JWTError, jwt
from src.app.models.user import User
from src.app.repositories.user_repository import UserRepository
from src.core.auth_token_config import auth_token_settings
from src.app.database import async_session_maker
from src.app.exceptions.user_exceptions import TokenException

async def get_websocket_user(
    token: str
) -> User:
    if not token:
        raise TokenException
    try:
        payload = jwt.decode(token, auth_token_settings.JWT_SECRET_KEY, algorithms=[auth_token_settings.JWT_ALG])
        user_id = payload.get('sub')
    except JWTError:
        raise TokenException
    
    if not user_id:
        raise TokenException
    
    async with async_session_maker() as session:
        user = await UserRepository(session).get(user_id=int(user_id))
        if not user:
            raise TokenException
        return user