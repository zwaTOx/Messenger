from pydantic import BaseModel

class InviteUserRequest(BaseModel):
    email: str