from dataclasses import dataclass, field
from uuid import UUID

from src.domain.entities.article import ArticleEntity
from src.domain.entities.association import ArticleCategoryAssociationEntity


@dataclass
class MemoryArticleCategoryAssociationsRepository:
    storage: set[ArticleCategoryAssociationEntity] = field(default_factory=set)

    async def create_many(self, article: ArticleEntity) -> None:
        for category in article.categories:
            self.storage.add(
                ArticleCategoryAssociationEntity(
                    article_oid=article.oid,
                    category_name=category.name,
                ),
            )

    async def get_categories_names_by_article_oid(
        self,
        article_oid: UUID,
    ) -> set[str]:
        return {
            association.category_name
            for association in self.storage
            if association.article_oid == article_oid
        }

    async def get_articles_oids_by_category_name(
        self,
        category_name: str,
    ) -> set[UUID]:
        return {
            association.article_oid
            for association in self.storage
            if association.category_name == category_name
        }

    async def remove_by_article_oid(self, article_oid: UUID) -> None:
        self.storage = {
            association
            for association in self.storage
            if association.article_oid != article_oid
        }
