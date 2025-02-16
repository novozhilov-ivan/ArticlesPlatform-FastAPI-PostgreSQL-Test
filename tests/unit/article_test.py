from src.domain.entities.article import ArticleEntity
from src.domain.entities.user import UserEntity


def test_create_article(user: UserEntity):
    assert ArticleEntity(
        author_oid=user.oid,
        title="some_title",
        text="some_text",
    )
