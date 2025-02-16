from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.gateways.postgresql.models.base import ORMBase
from src.gateways.postgresql.models.mixins import MixinUpdatedAt, MixinUUIDOid


if TYPE_CHECKING:
    from src.gateways.postgresql.models.category import ORMCategory
    from src.gateways.postgresql.models.user import ORMUser


class ORMArticle(ORMBase, MixinUUIDOid, MixinUpdatedAt):  # type: ignore[misc]
    __tablename__ = "articles"

    author_oid: Mapped[UUID] = mapped_column(ForeignKey("users.oid"))
    title: Mapped[str]
    text: Mapped[str]

    author: Mapped["ORMUser"] = relationship(back_populates="articles")
    categories: Mapped[set["ORMCategory"]] = relationship(
        secondary="articles_categories_associations",
        back_populates="articles",
        collection_class=set,
    )
