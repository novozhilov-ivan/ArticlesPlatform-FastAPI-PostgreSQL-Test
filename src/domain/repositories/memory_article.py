from dataclasses import dataclass, field
from uuid import UUID

from src.domain.entities.article import ArticleEntity
from src.domain.repositories.interfaces import IArticlesRepository
from src.domain.repositories.memory_association import (
    MemoryArticleCategoryAssociationsRepository,
)


@dataclass(kw_only=True)
class MemoryArticlesRepository(IArticlesRepository):
    storage: set[ArticleEntity] = field(default_factory=set)
    associations_repository: MemoryArticleCategoryAssociationsRepository

    async def create(self, article: ArticleEntity) -> None:
        if article in self.storage:
            return
        self.storage.add(article)

    async def get_by_oid(self, oid: UUID) -> ArticleEntity | None:
        return next((article for article in self.storage if article == oid), None)

    async def list(self) -> set[ArticleEntity]:
        return self.storage

    async def delete_by_oid(self, oid: UUID) -> None:
        article = next(
            (article for article in self.storage if article.oid == oid),
            None,
        )
        if article:
            self.storage.remove(article)
