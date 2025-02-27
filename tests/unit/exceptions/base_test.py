from src.domain.exceptions.base import ArticlePlatformException


def test_article_platform_exception():
    expected_message = "Article Platform exception occurred."

    exception = ArticlePlatformException()

    assert exception.message == expected_message
