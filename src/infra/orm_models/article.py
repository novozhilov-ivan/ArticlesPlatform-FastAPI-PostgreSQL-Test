from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.orm_models.base import ORMBase
from src.infra.orm_models.category import ORMCategory
from src.infra.orm_models.mixins import MixinUpdatedAt, MixinUUIDOid
from src.infra.orm_models.user import ORMUser


class ORMArticle(ORMBase, MixinUUIDOid, MixinUpdatedAt):
    __tablename__ = "articles"

    owner_oid: Mapped[UUID] = mapped_column(ForeignKey(column="users.oid"))
    title: Mapped[str]
    text: Mapped[str]

    owner: Mapped[ORMUser] = relationship(back_populates="articles")
    categories: Mapped[set[ORMCategory]] = relationship(
        secondary="articles_categories_associations",
        back_populates="articles",
    )
    category_association: Mapped[set[ORMCategory]] = relationship(
        back_populates="articles",
    )
