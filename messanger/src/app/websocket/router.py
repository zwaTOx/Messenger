from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query

from src.app.auth.dependencies import CurrentUser
from .manager import ws_manager
from .dependencies import get_websocket_user

ws_router = APIRouter()

@ws_router.websocket("/ws/connect")
async def connect_to_ws(
    websocket: WebSocket, 
    token: str = Query(...)
    # user: CurrentUser
    ):
    # await websocket.accept()
    # headers = dict(websocket.headers)
    # token = headers.get("authorization") or headers.get("Authorization")
    try:
        user = await get_websocket_user(token)
        # print(user)
        user_id = user.user_id
        await ws_manager.connect(websocket, user_id)
        await ws_manager.send_personal_message({"type": "welcome", "user_id": user_id}, user_id)
        while True:
            data = await websocket.receive_json()
            await ws_manager.send_personal_message({"type": "echo", "payload": data}, user_id)
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)