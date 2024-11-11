from src.domain.entities.article import ArticleEntity


def test_create_article():
    assert ArticleEntity(title="some_title", text="some_text")
