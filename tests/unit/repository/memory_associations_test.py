from src.domain.entities.article import ArticleEntity
from src.domain.entities.association import ArticleCategoryAssociationEntity
from src.domain.entities.category import CategoryEntity
from src.domain.repositories.memory_association import (
    MemoryArticleCategoryAssociationsRepository,
)


async def test_create_many_associations_from_empty_categories_article(
    article: ArticleEntity,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    await associations_repository.create_many(article)
    assert not associations_repository.storage


async def test_create_many_associations_with_category_in_article(
    article: ArticleEntity,
    category: CategoryEntity,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    article.categories.add(category)

    await associations_repository.create_many(article)
    association, *_ = associations_repository.storage

    assert association.article_oid == article
    assert association.category_name == category


async def test_get_categories_names_by_article_oid(
    association: ArticleCategoryAssociationEntity,
    article: ArticleEntity,
    category: CategoryEntity,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    associations_repository.storage = {association}

    category_names = (
        await (
            associations_repository.get_categories_names_by_article_oid(article.oid)
        )
    )

    assert category_names == {category.name}


async def test_get_articles_oids_by_category_name(
    association: ArticleCategoryAssociationEntity,
    article: ArticleEntity,
    category: CategoryEntity,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    associations_repository.storage = {association}

    articles_oids = await associations_repository.get_articles_oids_by_category_name(
        category_name=category.name,
    )

    assert articles_oids == {article.oid}


async def test_remove_by_article_oid(
    association: ArticleCategoryAssociationEntity,
    article: ArticleEntity,
    associations_repository: MemoryArticleCategoryAssociationsRepository,
):
    associations_repository.storage = {association}

    await associations_repository.remove_by_article_oid(article_oid=article.oid)

    assert not associations_repository.storage
