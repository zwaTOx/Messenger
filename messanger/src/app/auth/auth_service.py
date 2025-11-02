from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models.user import User
from src.app.exceptions.user_exceptions import UserAlreadyExistsException, PasswordMismatchException, InvalidUserCredentialsException
from src.app.repositories.user_repository import UserRepository
from .schemes import RegisterRequest, LoginRequest, UserResponse, TokenResponse
from .auth_utils import verify_password, create_token, hash_password

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repo = UserRepository(session)

    async def _get_user(self, email: str) -> User:
        existing_by_email = await self.user_repo.get(email=email)
        return existing_by_email

    async def create_user(self, user_data: RegisterRequest) -> UserResponse:
        if await self._get_user(user_data.email):
            raise UserAlreadyExistsException
        if user_data.password != user_data.verify_password:
            raise PasswordMismatchException
        password = hash_password(user_data.password)
        return await UserRepository(self.session).create(user_data.email, password)
    
    async def login_user(self, user_data: LoginRequest) -> TokenResponse:
        founded_user = await self._get_user(user_data.email)
        if not founded_user or not verify_password(user_data.password, founded_user.password): 
            raise InvalidUserCredentialsException
        access_token = create_token({"sub": str(founded_user.id)})
        return TokenResponse(access_token=access_token)
        

        