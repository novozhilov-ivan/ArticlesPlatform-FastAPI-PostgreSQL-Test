from src.domain.entities.article import ArticleEntity


def test_create_article(user):
    assert ArticleEntity(
        owner_oid=user.oid,
        title="some_title",
        text="some_text",
    )
