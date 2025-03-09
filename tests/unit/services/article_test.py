from src.domain.entities.article import ArticleEntity
from src.domain.repositories.memory_article import MemoryArticlesRepository
from src.domain.services.article import ArticleService


async def test_write(
    article: ArticleEntity,
    article_service: ArticleService,
    articles_repository: MemoryArticlesRepository,
):
    await article_service.write(article)

    assert articles_repository.storage == {article}


async def test_get_list_with_article(
    article: ArticleEntity,
    article_service: ArticleService,
    articles_repository: MemoryArticlesRepository,
):
    articles_repository.storage = {article}

    articles_list = await article_service.get_list()

    assert articles_list == articles_repository.storage
