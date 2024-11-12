from sqlalchemy.orm import Mapped, relationship

from src.infra.orm_models.article import ORMArticle
from src.infra.orm_models.base import ORMBase
from src.infra.orm_models.mixins import MixinUUIDOid


class ORMCategory(ORMBase, MixinUUIDOid):
    __tablename__ = "categories"

    name: Mapped[str]

    articles: Mapped[list[ORMArticle]] = relationship(
        secondary="articles_categories_associations",
        back_populates="categories",
    )

    article_association: Mapped[list[ORMArticle]] = relationship(
        back_populates="categories",
    )
