import pytest

from src.domain.entities.user import UserEntity
from src.domain.exceptions.user_registration import (
    NicknameAlreadyExistException,
    PasswordConstraintException,
)
from src.domain.repositories.interfaces import IUsersRepository
from src.domain.services.user_registration import UserRegistrationService


async def test_register_user_success(
    user_registration_service: UserRegistrationService,
    users_repository: IUsersRepository,
    user: UserEntity,
):
    await user_registration_service.register(
        nickname=user.nickname,
        plain_password=user.password,
    )

    assert await users_repository.get_by_nickname(user.nickname)


async def test_register_user_by_exist_nickname_exception(
    user_registration_service: UserRegistrationService,
    users_repository: IUsersRepository,
    user: UserEntity,
):
    await users_repository.create(user)

    with pytest.raises(NicknameAlreadyExistException):
        await user_registration_service.register(
            nickname=user.nickname,
            plain_password=user.password,
        )


@pytest.mark.parametrize(
    "bad_password",
    [
        "weak",
        "too_long" * 42,
    ],
)
async def test_register_user_password_constraint_exception(
    user_registration_service: UserRegistrationService,
    user: UserEntity,
    bad_password: str,
):
    with pytest.raises(PasswordConstraintException):
        await user_registration_service.register(
            nickname=user.nickname,
            plain_password=bad_password,
        )
