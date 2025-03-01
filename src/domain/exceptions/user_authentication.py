from dataclasses import dataclass

from src.domain.exceptions.base import ArticlePlatformException


@dataclass
class UserAuthenticationServiceException(ArticlePlatformException):
    @property
    def message(self) -> str:
        return "User authentication service exception occurred."


@dataclass
class InvalidCredentialsException(UserAuthenticationServiceException):
    nickname: str

    @property
    def message(self) -> str:
        return "Invalid credentials nickname or password."


@dataclass
class UserIsBannedException(UserAuthenticationServiceException):
    nickname: str

    @property
    def message(self) -> str:
        return f"User {self.nickname} is banned."
