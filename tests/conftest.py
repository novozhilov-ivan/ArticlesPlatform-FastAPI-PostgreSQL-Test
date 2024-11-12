from uuid import uuid4

import pytest

from src.domain.entities.user import UserEntity


@pytest.fixture(scope="session")
def user():
    return UserEntity(
        oid=uuid4(),
        nickname="some_nickname",
        password="some_password",
    )
