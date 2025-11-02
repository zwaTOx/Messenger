import json
from typing import List
from fastapi import WebSocket

from src.app.repositories.chat_users_repository import ChatUserRepository
from src.app.database import DbSession


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, user_id: int):
        if user_id in self.active_connections:
            existing_connection = self.active_connections[user_id]
            try:
                await existing_connection.close()
            except Exception as e:
                pass
            finally:
                del self.active_connections[user_id]
        await websocket.accept()
        self.active_connections[user_id] = websocket
    
    def disconnect(self, websocket: WebSocket, user_id: int):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_personal_message(self, payload: dict, user_id: int):
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_json(payload)

    async def broadcast_to_chat(self, session: DbSession, chat_id: int, message_data: dict):
        disconnected_users = []
        chat_user_repo = ChatUserRepository(session)
        chat_members = await chat_user_repo.get_all(chat_id=chat_id)
        for member in chat_members:
            user_id = member.user_id
            print(f'id: {user_id}')
            if user_id in self.active_connections:
                try:
                    print(f'Sended')
                    await self.active_connections[user_id].send_json(message_data)
                except Exception:
                    print(f'Dissconnect')
                    disconnected_users.append(user_id)
    
        for user_id in disconnected_users:
            if user_id in self.active_connections:
                del self.active_connections[user_id]

ws_manager = ConnectionManager()
