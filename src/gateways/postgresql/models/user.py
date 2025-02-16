from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.gateways.postgresql.models.base import ORMBase
from src.gateways.postgresql.models.mixins import MixinUpdatedAt, MixinUUIDOid


if TYPE_CHECKING:
    from src.gateways.postgresql.models.article import ORMArticle


class ORMUser(ORMBase, MixinUUIDOid, MixinUpdatedAt):  # type: ignore[misc]
    __tablename__ = "users"

    nickname: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    articles: Mapped[set["ORMArticle"]] = relationship(
        back_populates="author",
        collection_class=set,
    )
