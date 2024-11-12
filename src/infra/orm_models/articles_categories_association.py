from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from src.infra.orm_models.article import ORMArticle
from src.infra.orm_models.base import ORMBase
from src.infra.orm_models.category import ORMCategory
from src.infra.orm_models.mixins import MixinUUIDOid


class ORMArticlesCategoriesAssociation(ORMBase, MixinUUIDOid):
    __tablename__ = "articles_categories_associations"
    __table_args__ = UniqueConstraint(
        "articles",
        "categories",
        name="unique_categories_for_articles",
    )

    # ассоциация между ORMArticlesCategoriesAssociation и Article
    articles: Mapped[list[ORMArticle]] = relationship(
        back_populates="article_association",
    )
    # ассоциация между ORMArticlesCategoriesAssociation и Category
    categories: Mapped[set[ORMCategory]] = relationship(
        back_populates="category_association",
    )
