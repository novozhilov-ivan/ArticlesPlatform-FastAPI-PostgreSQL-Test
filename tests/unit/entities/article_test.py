from src.domain.entities.article import ArticleEntity
from src.domain.entities.user import UserEntity


def test_create_article(user: UserEntity):
    assert ArticleEntity(
        author_oid=user.oid,
        title="some_title",
        text="some_text",
    )


def test_article_equal_by_oid(user: UserEntity):
    article_1 = ArticleEntity(
        author_oid=user.oid, title="article_1", text="article_1"
    )
    article_2 = ArticleEntity(
        author_oid=user.oid, title="article_2", text="article_2"
    )
    article_1.oid = article_2.oid

    articles_set = set()
    articles_set.add(article_1)
    assert len(articles_set) == 1
    articles_set.add(article_2)
    assert len(articles_set) == 1

    received_article = next(iter(articles_set))
    assert received_article.oid == article_1.oid


def test_article_compare_with_uuid(user: UserEntity):
    article = ArticleEntity(author_oid=user.oid, title="Title", text="Text")
    assert article == article.oid


def test_article_compare_with_other(user: UserEntity):
    article = ArticleEntity(author_oid=user.oid, title="Title", text="Text")
    other = 42
    result = article.__eq__(other)
    assert result is NotImplemented
    assert article != other


def test_article_str_and_repr(user: UserEntity):
    title = "Article Title"
    article = ArticleEntity(author_oid=user.oid, title=title, text="Some text")
    assert str(article) == title
    assert repr(article) == title


def test_article_hash(user: UserEntity):
    article = ArticleEntity(author_oid=user.oid, title="Title", text="Text")
    assert hash(article) == hash(article.oid)
