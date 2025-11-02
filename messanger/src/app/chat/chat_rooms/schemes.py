from pydantic import BaseModel, ConfigDict

class CreateRoomRequest(BaseModel):
    name: str
    info: str
    isPrivate: bool