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


async def test_delete_by_oid(
    article: ArticleEntity,
    article_service: ArticleService,
    articles_repository: MemoryArticlesRepository,
):
    articles_repository.storage = {article}

    await article_service.delete_by_oid(article.oid)

    assert not articles_repository.storage


async def test_get_by_oid_non_exist_article(
    article: ArticleEntity,
    article_service: ArticleService,
):
    article_from_service = await article_service.get_by_oid(article.oid)

    assert article_from_service is None


async def test_get_by_oid_exist_article(
    article: ArticleEntity,
    article_service: ArticleService,
    articles_repository: MemoryArticlesRepository,
):
    articles_repository.storage = {article}

    article_from_service = await article_service.get_by_oid(article.oid)

    assert article_from_service == article
