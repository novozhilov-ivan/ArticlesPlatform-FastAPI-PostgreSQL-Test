from dataclasses import replace

import pytest

from src.domain.entities.user import UserEntity
from src.domain.enums import UserStatus
from src.domain.exceptions.user_authentication import (
    InvalidCredentialsException,
    UserIsBannedException,
)
from src.domain.repositories.interfaces import IUsersRepository
from src.domain.services.user_authentication import UserAuthenticationService


async def test_authenticate_valid_user(
    user: UserEntity,
    user_with_hashed_password: UserEntity,
    users_repository: IUsersRepository,
    user_authentication_service: UserAuthenticationService,
):
    await users_repository.create(user_with_hashed_password)

    authenticated_user = await user_authentication_service.authenticate(
        nickname=user.nickname,
        password=user.password,
    )

    assert authenticated_user == user
    assert authenticated_user.oid == user.oid


async def test_authenticate_invalid_password(
    user_with_hashed_password: UserEntity,
    users_repository: IUsersRepository,
    user_authentication_service: UserAuthenticationService,
):
    await users_repository.create(user_with_hashed_password)

    with pytest.raises(InvalidCredentialsException):
        await user_authentication_service.authenticate(
            nickname=user_with_hashed_password.nickname,
            password="wrong_password",
        )


async def test_authenticate_banned_user(
    user: UserEntity,
    users_repository: IUsersRepository,
    user_authentication_service: UserAuthenticationService,
):
    banned_user = replace(user, status=UserStatus.banned)
    await users_repository.create(banned_user)

    with pytest.raises(UserIsBannedException):
        await user_authentication_service.authenticate(
            nickname=user.nickname,
            password=user.password,
        )


async def test_authenticate_nonexistent_user(
    user_authentication_service: UserAuthenticationService,
):
    with pytest.raises(InvalidCredentialsException):
        await user_authentication_service.authenticate(
            nickname="nonexistent",
            password="password",
        )
