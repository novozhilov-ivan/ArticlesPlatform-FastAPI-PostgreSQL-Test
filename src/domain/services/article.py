from dataclasses import dataclass

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
