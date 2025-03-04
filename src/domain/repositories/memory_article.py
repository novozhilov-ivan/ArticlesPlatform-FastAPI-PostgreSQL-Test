from dataclasses import dataclass, field
from uuid import UUID

from src.domain.entities.article import ArticleEntity
from src.domain.repositories.interfaces import IArticlesRepository


@dataclass
class MemoryArticlesRepository(IArticlesRepository):
    _storage: set[ArticleEntity] = field(default_factory=set)

    async def create(self, article: ArticleEntity) -> None:
        if article not in self._storage:
            self._storage.add(article)

    async def get_by_oid(self, oid: UUID) -> ArticleEntity | None:
        return next((article for article in self._storage if article == oid), None)

    async def list(self) -> set[ArticleEntity]:
        return self._storage

    async def delete_by_oid(self, oid: UUID) -> None:
        article = next(
            (article for article in self._storage if article.oid == oid),
            None,
        )
        if article:
            self._storage.remove(article)
