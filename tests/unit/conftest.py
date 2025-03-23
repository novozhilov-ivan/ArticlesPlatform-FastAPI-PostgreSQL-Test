from dataclasses import replace

import pytest

from src.domain.entities.user import UserEntity
from src.domain.repositories.interfaces import (
    IArticlesRepository,
    ICategoriesRepository,
    ICommentsRepository,
    IUsersRepository,
)
from src.domain.repositories.memory_article import MemoryArticlesRepository
from src.domain.repositories.memory_association import (
    MemoryArticleCategoryAssociationsRepository,
)
from src.domain.repositories.memory_categories import MemoryCategoriesRepository
from src.domain.repositories.memory_comments import MemoryCommentsRepository
from src.domain.repositories.memory_users import MemoryUsersRepository
from src.domain.services.article import ArticleService
from src.domain.services.password_hasher import PasswordHasherService
from src.domain.services.user_authentication import UserAuthenticationService
from src.domain.services.user_registration import UserRegistrationService


@pytest.fixture
def users_repository() -> IUsersRepository:
    return MemoryUsersRepository()


@pytest.fixture
def categories_repository() -> ICategoriesRepository:
    return MemoryCategoriesRepository()


@pytest.fixture
def articles_repository(
    associations_repository: MemoryArticleCategoryAssociationsRepository,
    categories_repository: ICategoriesRepository,
    comments_repository: ICommentsRepository,
) -> IArticlesRepository:
    return MemoryArticlesRepository(
        categories_repository=categories_repository,
        associations_repository=associations_repository,
        comments_repository=comments_repository,
    )


@pytest.fixture
def associations_repository() -> MemoryArticleCategoryAssociationsRepository:
    return MemoryArticleCategoryAssociationsRepository()


@pytest.fixture
def comments_repository() -> ICommentsRepository:
    return MemoryCommentsRepository()


@pytest.fixture(scope="session")
def password_hasher() -> PasswordHasherService:
    return PasswordHasherService()


@pytest.fixture(scope="session")
def user_plain_password(user: UserEntity) -> str:
    return user.password


@pytest.fixture(scope="session")
def hashed_password(
    password_hasher: PasswordHasherService,
    user_plain_password: str,
) -> str:
    return password_hasher.hash_password(user_plain_password)


@pytest.fixture(scope="session")
def user_with_hashed_password(
    user: UserEntity,
    hashed_password: str,
) -> UserEntity:
    return replace(user, password=hashed_password)


@pytest.fixture
def user_registration_service(
    users_repository: IUsersRepository,
    password_hasher: PasswordHasherService,
) -> UserRegistrationService:
    return UserRegistrationService(
        users_repository=users_repository,
        password_hasher=password_hasher,
    )


@pytest.fixture
def user_authentication_service(
    users_repository: IUsersRepository,
    password_hasher: PasswordHasherService,
) -> UserAuthenticationService:
    return UserAuthenticationService(
        users_repository=users_repository,
        password_hasher=password_hasher,
    )


@pytest.fixture
def article_service(articles_repository: IArticlesRepository) -> ArticleService:
    return ArticleService(articles_repository)
