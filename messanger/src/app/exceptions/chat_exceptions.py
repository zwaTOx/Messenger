from fastapi import status
from src.app.exceptions.base import AppHTTPException

class PermissionException(AppHTTPException):
    def __init__(self, detail="Недостаточно прав для выполнения действия"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

class ConflictException(AppHTTPException):
    def __init__(self, detail="Пользователь уже существует в данном чате"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
