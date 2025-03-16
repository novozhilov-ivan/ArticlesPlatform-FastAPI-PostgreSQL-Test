from dataclasses import dataclass

from src.domain.entities.user import UserEntity
from src.domain.exceptions.user_authentication import (
    InvalidCredentialsException,
    UserIsBannedException,
)
from src.domain.repositories.interfaces import IUsersRepository
from src.domain.services.password_hasher import PasswordHasherService
from src.domain.types.statuses import UserStatus


@dataclass
class UserAuthenticationService:
    users_repository: IUsersRepository
    password_hasher: PasswordHasherService

    async def authenticate(self, nickname: str, password: str) -> UserEntity:
        user = await self.users_repository.get_by_nickname(nickname)

        if not user:
            raise InvalidCredentialsException(nickname)

        if user.status == UserStatus.banned:
            raise UserIsBannedException(nickname)

        if not self.password_hasher.verify_password(
            plain_password=password,
            hashed_password=user.password,
        ):
            raise InvalidCredentialsException(nickname)

        return user
