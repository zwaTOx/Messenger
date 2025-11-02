from fastapi import HTTPException, status
from src.app.exceptions.base import AppHTTPException

class UserAlreadyExistsException(AppHTTPException):
    def __init__(self, detail="Пользователь с таким email уже существует"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
    
class PasswordMismatchException(AppHTTPException):
    def __init__(self, detail="Пароли не совпадают"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

class InvalidUserCredentialsException(AppHTTPException):
    def __init__(self, detail="Неверные данные пользователя"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

class TokenException(AppHTTPException):
    def __init__(self, detail="Ошибка в токене"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)