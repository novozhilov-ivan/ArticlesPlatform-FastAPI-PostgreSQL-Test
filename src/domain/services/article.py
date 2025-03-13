from dataclasses import dataclass
from uuid import UUID

from src.domain.entities.article import ArticleEntity
from src.domain.repositories.interfaces import (
    IArticlesRepository,
)


@dataclass
class ArticleService:
    articles_repository: IArticlesRepository

    async def write(self, article: ArticleEntity) -> None:
        await self.articles_repository.create(article)

    async def get_list(self) -> set[ArticleEntity]:
        return await self.articles_repository.list()

    async def delete_by_oid(self, oid: UUID) -> None:
        await self.articles_repository.delete_by_oid(oid)

    async def get_by_oid(self, oid: UUID) -> ArticleEntity | None:
        return await self.articles_repository.get_by_oid(oid)
