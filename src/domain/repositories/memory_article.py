from dataclasses import dataclass, field
from uuid import UUID

from src.domain.entities.article import ArticleEntity
from src.domain.repositories.interfaces import (
    IArticlesRepository,
    ICategoriesRepository,
)
from src.domain.repositories.memory_association import (
    MemoryArticleCategoryAssociationsRepository,
)


@dataclass(kw_only=True)
class MemoryArticlesRepository(IArticlesRepository):
    categories_repository: ICategoriesRepository
    associations_repository: MemoryArticleCategoryAssociationsRepository
    storage: set[ArticleEntity] = field(default_factory=set)

    async def create(self, article: ArticleEntity) -> None:
        if article in self.storage:
            return
        self.storage.add(article)
        await self.categories_repository.create_many(article.categories)
        await self.associations_repository.create_many(article)

    async def load_categories(self, article: ArticleEntity) -> ArticleEntity:
        categories_names = (
            await self.associations_repository.get_categories_names_by_article_oid(
                article.oid
            )
        )
        for category_name in categories_names:
            category = await self.categories_repository.get_by_name(category_name)
            if category:
                article.categories.add(category)

        return article

    async def get_by_oid(self, oid: UUID) -> ArticleEntity | None:
        try:
            article = next(article for article in self.storage if article == oid)
        except StopIteration:
            return None

        return await self.load_categories(article)

    async def list(self) -> set[ArticleEntity]:
        return self.storage

    async def delete_by_oid(self, oid: UUID) -> None:
        try:
            article = next(article for article in self.storage if article.oid == oid)
        except StopIteration:
            return

        self.storage.remove(article)
        await self.associations_repository.remove_by_article_oid(oid)
