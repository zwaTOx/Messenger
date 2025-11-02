from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.app.database import init_db

from src.app.auth.router import auth_router
from src.app.chat_rooms.router import chat_rooms_router
from src.app.chat_users.router import chat_users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Server is starting')
    await init_db()
    yield
    print('Server is shutting down')

app = FastAPI(
    title='AI Task Traker',
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get('/')
async def ping():
    return {'msg': 'pong'}

app.include_router(auth_router,
    prefix='/api')
app.include_router(chat_rooms_router,
    prefix='/api')
app.include_router(chat_users_router,
    prefix='/api')