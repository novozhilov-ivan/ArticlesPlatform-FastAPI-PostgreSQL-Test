from enum import StrEnum


class UserRoles(StrEnum):
    admin = "admin"
    user = "user"


class UserStatus(StrEnum):
    active = "active"
    banned = "banned"
