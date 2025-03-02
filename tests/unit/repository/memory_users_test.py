from dataclasses import replace

from src.domain.entities.user import UserEntity
from src.domain.repositories.interfaces import IUsersRepository


async def test_user_creation_in_repository(
    user: UserEntity,
    users_repository: IUsersRepository,
):
    await users_repository.create(user)

    repository_user = await users_repository.get_by_nickname(user.nickname)

    assert repository_user is not None
    assert repository_user.oid == user.oid


async def test_idempotent_user_creation_in_repository(
    user: UserEntity,
    users_repository: IUsersRepository,
):
    await users_repository.create(user)
    user_with_same_nickname_in_upper_case: UserEntity = replace(
        user,
        nickname=user.nickname.upper(),
    )
    await users_repository.create(user_with_same_nickname_in_upper_case)

    repository_user = await users_repository.get_by_nickname(user.nickname)

    assert repository_user is not None
    assert repository_user.oid == user.oid


async def test_get_user_by_nickname_from_repository(
    user: UserEntity,
    users_repository: IUsersRepository,
):
    assert await users_repository.get_by_nickname(user.nickname) is None

    await users_repository.create(user)

    repository_user = await users_repository.get_by_nickname(user.nickname)

    assert repository_user is not None
    assert repository_user.oid == user.oid
