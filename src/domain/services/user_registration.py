from dataclasses import dataclass

from src.domain.entities.user import UserEntity
from src.domain.exceptions.user_registration import (
    PasswordTooWeakException,
    UserNicknameAlreadyExistException,
)
from src.domain.repositories.interfaces import IUsersRepository
from src.domain.services.password_hasher import PasswordHasherService
from src.domain.specifications.password import PasswordCompositeSpec


@dataclass
class UserRegistrationService:
    users_repository: IUsersRepository
    password_hasher: PasswordHasherService

    async def _validate_nickname(self, nickname: str) -> None:
        if await self.users_repository.get_by_nickname(nickname):
            raise UserNicknameAlreadyExistException(nickname)

    @staticmethod
    async def _validate_password(plain_password: str) -> None:
        if not (specification := PasswordCompositeSpec(plain_password)):
            raise PasswordTooWeakException(meta=specification.on_fail_message)

    async def register_user(self, nickname: str, plain_password: str) -> None:
        await self._validate_nickname(nickname)
        await self._validate_password(plain_password)

        await self.users_repository.create(
            user=UserEntity(
                nickname=nickname,
                hashed_password=self.password_hasher.hash_password(plain_password),
            ),
        )
