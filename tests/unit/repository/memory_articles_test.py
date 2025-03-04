from src.domain.entities.article import ArticleEntity
from src.domain.repositories.interfaces import IArticlesRepository
from src.domain.repositories.memory_article import MemoryArticlesRepository


async def test_get_by_oid_article_in_empty_repository(
    article: ArticleEntity,
    articles_repository: IArticlesRepository,
):
    assert not await articles_repository.get_by_oid(article.oid)


async def test_get_by_name_exist_category_in_repository(article: ArticleEntity):
    articles_repository = MemoryArticlesRepository({article})

    exist_article = await articles_repository.get_by_oid(article.oid)

    assert exist_article
    assert exist_article == article


async def test_create_article_in_empty_repository(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    await articles_repository.create(article)

    exist_article, *_ = articles_repository._storage

    assert exist_article
    assert exist_article == article


async def test_create_article_is_idempotent(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    await articles_repository.create(article)
    await articles_repository.create(article)

    assert len(articles_repository._storage) == 1

    exist_article, *_ = articles_repository._storage

    assert exist_article
    assert exist_article == article


async def test_get_list_article_from_repository(article: ArticleEntity):
    articles_repository = MemoryArticlesRepository({article})

    articles_list = await articles_repository.list()
    assert articles_list == {article}
    assert articles_list == articles_repository._storage


async def test_delete_by_oid_exist_article_in_repository(article: ArticleEntity):
    articles_repository = MemoryArticlesRepository({article})

    await articles_repository.delete_by_oid(article.oid)

    assert not articles_repository._storage


async def test_delete_by_oid_non_exist_article_in_repository(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    await articles_repository.delete_by_oid(article.oid)

    assert not articles_repository._storage
