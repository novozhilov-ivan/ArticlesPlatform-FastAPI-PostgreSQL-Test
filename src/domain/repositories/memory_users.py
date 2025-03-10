from dataclasses import dataclass, field

from src.domain.entities.user import UserEntity
from src.domain.repositories.interfaces import IUsersRepository


@dataclass
class MemoryUsersRepository(IUsersRepository):
    _storage: set[UserEntity] = field(default_factory=set)

    async def create(self, user: UserEntity) -> None:
        if user not in self._storage:
            self._storage.add(user)

    async def get_by_nickname(self, nickname: str) -> UserEntity | None:
        if nickname not in self._storage:
            return None
        return next(user for user in self._storage if user == nickname)
