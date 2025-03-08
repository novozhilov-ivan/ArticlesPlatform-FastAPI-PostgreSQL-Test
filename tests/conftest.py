import pytest

from src.domain.entities.article import ArticleEntity
from src.domain.entities.association import ArticleCategoryAssociationEntity
from src.domain.entities.category import CategoryEntity
from src.domain.entities.user import UserEntity


@pytest.fixture(scope="session")
def user() -> UserEntity:
    return UserEntity(
        nickname="nickname",
        password="plain_password",
    )


@pytest.fixture(scope="session")
def category() -> CategoryEntity:
    return CategoryEntity(name="name")


@pytest.fixture(scope="session")
def article(user: UserEntity) -> ArticleEntity:
    return ArticleEntity(
        author_oid=user.oid,
        title="some_title",
        text="some_text",
    )


@pytest.fixture(scope="session")
def association(
    article: ArticleEntity,
    category: CategoryEntity,
) -> ArticleCategoryAssociationEntity:
    return ArticleCategoryAssociationEntity(
        article_oid=article.oid,
        category_name=category.name,
    )
