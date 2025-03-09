from src.domain.entities.article import ArticleEntity
from src.domain.entities.association import ArticleCategoryAssociationEntity
from src.domain.entities.category import CategoryEntity
from src.domain.repositories.interfaces import (
    IArticlesRepository,
)
from src.domain.repositories.memory_article import MemoryArticlesRepository
from src.domain.repositories.memory_association import (
    MemoryArticleCategoryAssociationsRepository,
)
from src.domain.repositories.memory_categories import MemoryCategoriesRepository


async def test_get_by_oid_article_in_empty_repository(
    article: ArticleEntity,
    articles_repository: IArticlesRepository,
):
    assert not await articles_repository.get_by_oid(article.oid)


async def test_get_by_name_exist_category_in_repository(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    articles_repository.storage = {article}

    exist_article = await articles_repository.get_by_oid(article.oid)

    assert exist_article
    assert exist_article == article


async def test_create_article_in_empty_repository(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    await articles_repository.create(article)

    exist_article, *_ = articles_repository.storage

    assert exist_article
    assert exist_article == article


async def test_create_article_is_idempotent(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    await articles_repository.create(article)
    await articles_repository.create(article)

    assert len(articles_repository.storage) == 1

    exist_article, *_ = articles_repository.storage

    assert exist_article
    assert exist_article == article


async def test_create_article_with_category(
    article: ArticleEntity,
    category: CategoryEntity,
    association: ArticleCategoryAssociationEntity,
    articles_repository: MemoryArticlesRepository,
    categories_repository: MemoryCategoriesRepository,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    article.categories = {category}
    await articles_repository.create(article)

    exist_article, *_ = articles_repository.storage
    exist_category, *_ = categories_repository.storage
    exist_association, *_ = associations_repository.storage

    assert exist_article
    assert exist_article == article
    assert exist_category
    assert exist_category == category
    assert exist_association
    assert exist_association == association


async def test_create_article_with_category_is_idempotent(
    article: ArticleEntity,
    category: CategoryEntity,
    association: ArticleCategoryAssociationEntity,
    articles_repository: MemoryArticlesRepository,
    categories_repository: MemoryCategoriesRepository,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    article.categories = {category}
    await articles_repository.create(article)
    await articles_repository.create(article)

    assert len(articles_repository.storage) == 1
    assert len(articles_repository.storage) == 1
    assert len(associations_repository.storage) == 1

    exist_article, *_ = articles_repository.storage
    exist_category, *_ = categories_repository.storage
    exist_association, *_ = associations_repository.storage

    assert exist_article
    assert exist_article == article
    assert exist_category
    assert exist_category == category
    assert exist_association
    assert exist_association == association


async def test_get_list_article_from_repository(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    articles_repository.storage = {article}

    articles_list = await articles_repository.list()
    assert articles_list == {article}
    assert articles_list == articles_repository.storage


async def test_delete_by_oid_exist_article_and_association(
    article: ArticleEntity,
    association: ArticleCategoryAssociationEntity,
    articles_repository: MemoryArticlesRepository,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    articles_repository.storage = {article}
    associations_repository.storage = {association}

    await articles_repository.delete_by_oid(article.oid)

    assert not articles_repository.storage
    assert not associations_repository.storage


async def test_delete_by_oid_non_exist_article_in_repository(
    article: ArticleEntity,
    articles_repository: MemoryArticlesRepository,
):
    await articles_repository.delete_by_oid(article.oid)


async def test_load_exist_categories_in_article(
    article: ArticleEntity,
    category: CategoryEntity,
    association: ArticleCategoryAssociationEntity,
    articles_repository: MemoryArticlesRepository,
    categories_repository: MemoryCategoriesRepository,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    categories_repository.storage = {category}
    associations_repository.storage = {association}

    article = await articles_repository.load_categories(article)

    assert article.categories == {category}


async def test_load_non_exist_categories_in_article(
    article: ArticleEntity,
    association: ArticleCategoryAssociationEntity,
    articles_repository: MemoryArticlesRepository,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    associations_repository.storage = {association}

    article = await articles_repository.load_categories(article)

    assert not article.categories
