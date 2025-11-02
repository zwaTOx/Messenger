from pydantic import BaseModel, EmailStr, ConfigDict

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    verify_password: str
    # username: str

class TokenRefreshRequest(BaseModel):
    refresh_token: str

class TokenResponse(BaseModel):
    access_token: str
    # refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    user_id: int
    email: str
    # username: str
    model_config = ConfigDict(
        from_attributes=True
    )