from pydantic import BaseModel, ConfigDict

class CreateMessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    message_id: int
    message: str
    chat_id: int
    user_id: int
    model_config = ConfigDict(
        from_attributes=True
    )