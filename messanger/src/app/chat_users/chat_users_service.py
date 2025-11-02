from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models.chat_users import UserRights
from src.app.repositories.chat_users_repository import ChatUserRepository
from .schemes import InviteUserRequest
from src.app.exceptions.chat_exceptions import PermissionException

class ChatUsersService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.chat_repo = ChatUserRepository(session)

    async def verify_inv_perms(self, user_id):
        chat_member = await self.chat_repo.get(user_id=user_id)
        if not chat_member or chat_member.rights not in [UserRights.GOD.value, UserRights.ADMIN.value]:
            raise PermissionException
        return chat_member

    async def invite_user(self, user_id: int, chat_id: int, user_inv_data: InviteUserRequest):
        chat_member = await self.verify_inv_perms(user_id)
        # await 

