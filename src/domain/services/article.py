from dataclasses import dataclass

from src.domain.entities.article import ArticleEntity
from src.domain.repositories.interfaces import (
    IArticlesRepository,
    ICategoriesRepository,
)


@dataclass
class ArticleService:
    articles_repository: IArticlesRepository
    category_repository: ICategoriesRepository

    async def write(self, article: ArticleEntity) -> None:
        await self.category_repository.create_many(*article.categories)
        await self.articles_repository.create(article)

    async def get_list(self, page: int, offset: int) -> set[ArticleEntity]:
        return await self.articles_repository.list(page, offset)
