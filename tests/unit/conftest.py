import pytest

from src.domain.repositories.interfaces import IUsersRepository
from src.domain.repositories.memory import MemoryUserRepository
from src.domain.services.password_hasher import PasswordHasherService
from src.domain.services.user_registration import UserRegistrationService


@pytest.fixture
def users_repository() -> IUsersRepository:
    return MemoryUserRepository()


@pytest.fixture(scope="session")
def password_hasher() -> PasswordHasherService:
    return PasswordHasherService()


@pytest.fixture(scope="package")
def user_registration_service(
    users_repository: IUsersRepository,
    password_hasher: PasswordHasherService,
) -> UserRegistrationService:
    return UserRegistrationService(
        users_repository=users_repository,
        password_hasher=password_hasher,
    )
