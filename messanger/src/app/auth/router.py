from fastapi import APIRouter, Response
from .schemes import RegisterRequest, LoginRequest, UserResponse, TokenResponse
from .auth_service import AuthService
from .auth_utils import create_token
from src.app.database import DbSession

auth_router = APIRouter() 

@auth_router.post(
    "/auth/sign-up",
    response_model=UserResponse,
)
async def create_user(
    session: DbSession,
    user_create_data: RegisterRequest
):
    new_user = await AuthService(session).create_user(user_create_data)
    return new_user

@auth_router.post(
    "/auth/login",
    response_model=TokenResponse
)
async def login_user(
    response: Response,
    session: DbSession,
    user_login_data: LoginRequest
):
    token_response = await AuthService(session).login_user(user_login_data)
    
    response.set_cookie(key="access_token", value = token_response.access_token, httponly=True)
    return token_response