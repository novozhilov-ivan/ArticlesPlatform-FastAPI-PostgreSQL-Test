from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.gateways.postgresql.models.base import ORMBase
from src.gateways.postgresql.models.mixins import MixinUUIDOid


if TYPE_CHECKING:
    from src.gateways.postgresql.models.article import ORMArticle


class ORMCategory(ORMBase, MixinUUIDOid):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)

    articles: Mapped[set["ORMArticle"]] = relationship(
        secondary="articles_categories_associations",
        back_populates="categories",
        collection_class=set,
    )
