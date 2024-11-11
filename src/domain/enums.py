from enum import StrEnum


class UserRoles(StrEnum):
    admin: str = "admin"
    user: str = "user"


class UserStatus(StrEnum):
    active: str = "active"
    banned: str = "banned"
