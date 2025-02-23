from dataclasses import dataclass

from src.domain.exceptions.base import ArticlePlatformException


@dataclass
class ArticlePlatformRegistrationException(ArticlePlatformException):
    @property
    def message(self) -> str:
        return "Article Platform registration error occurred."


@dataclass
class UserNicknameAlreadyExistException(ArticlePlatformRegistrationException):
    nickname: str

    @property
    def message(self) -> str:
        return f"{super().message} User nickname: {self.nickname} already exist."


@dataclass
class PasswordTooWeakException(ArticlePlatformRegistrationException):
    meta: str

    @property
    def message(self) -> str:
        return f"{super().message} Password too weak. {self.meta}"
