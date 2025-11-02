from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models.chat_users import UserRights
from src.app.repositories.chat_users_repository import ChatUserRepository
from src.app.repositories.user_repository import UserRepository
from .schemes import InviteUserRequest
from src.app.exceptions.chat_exceptions import PermissionException, ConflictException

class ChatUsersService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.chat_user_repo = ChatUserRepository(session)
    
    async def verify_perms(self, user_id: int, chat_id: int, rights=None):
        if rights is None:
            rights = [UserRights.GOD, UserRights.ADMIN]
        
        chat_member = await self.chat_user_repo.get(user_id=user_id, chat_id=chat_id)
        print(chat_member.rights, rights)
        print(type(chat_member.rights), type(rights), type(UserRights.GOD.value))
        if not chat_member or chat_member.rights not in rights:
            raise PermissionException
        return chat_member

    async def get_chat_members(self, user_id: int, chat_id: int):
        await self.verify_perms(user_id, chat_id)
        chat_members = await self.chat_user_repo.get_all(chat_id=chat_id)
        return chat_members

    async def invite_user(self, user_id: int, chat_id: int, user_inv_data: InviteUserRequest):
        chat_member = await self.verify_perms(user_id, chat_id)
        founded_user = await UserRepository(self.session).get(email=user_inv_data.email)
        if not founded_user:
            raise ValueError("User not found")
        existing_member = await self.chat_user_repo.get(
            user_id=founded_user.user_id, chat_id=chat_id)
        if existing_member:
            raise ConflictException
        member = await self.chat_user_repo.create(chat_id=chat_id, user_id=founded_user.user_id, rights='USER')
        return member

