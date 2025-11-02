import json
from typing import List
from fastapi import WebSocket


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

    async def broadcast_to_all(self, message: dict):
        disconnected_users = []
        
        for user_id, connection in self.active_connections.items():
            try:
                await connection.send_text(json.dumps(message))
            except Exception:
                disconnected_users.append(user_id)
        
        for user_id in disconnected_users:
            if user_id in self.active_connections:
                del self.active_connections[user_id]

ws_manager = ConnectionManager()
