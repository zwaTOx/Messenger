from datetime import timezone, timedelta, datetime
from src.core.auth_token_config import auth_token_settings
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_token(data: str):
    to_encode = data.copy() 
    expire = datetime.now(timezone.utc) + timedelta(minutes=auth_token_settings.JWT_EXP_MIN)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, key=auth_token_settings.JWT_SECRET_KEY, algorithm=auth_token_settings.JWT_ALG)
    return encode_jwt

def hash_password(password: str):
    # return pwd_context.hash(password)
    return password

def verify_password(plain_pass: str, hashed_password: str):
    # return pwd_context.verify(plain_pass, hashed_password)
    return plain_pass == hashed_password