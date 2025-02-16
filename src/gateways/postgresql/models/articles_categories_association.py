from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.gateways.postgresql.models.base import ORMBase
from src.gateways.postgresql.models.mixins import MixinUUIDOid


class ORMArticlesCategoriesAssociation(ORMBase, MixinUUIDOid):
    __tablename__ = "article_category_associations"
    __table_args__ = (
        UniqueConstraint(
            "article_oid",
            "category_oid",
            name="unique_category_for_article",
        ),
    )

    article_oid: Mapped[UUID] = mapped_column(ForeignKey("articles.oid"))
    category_oid: Mapped[UUID] = mapped_column(ForeignKey("categories.oid"))
