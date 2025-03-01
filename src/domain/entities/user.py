from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.enums import UserRoles, UserStatus


@dataclass(eq=False, kw_only=True)
class UserEntity(BaseEntity):
    nickname: str
    password: str
    role: UserRoles = UserRoles.user
    status: UserStatus = UserStatus.active

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.__str__() == other.lower()
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__str__() == other.__str__()

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __str__(self) -> str:
        return self.nickname.lower()

    __repr__ = __str__
