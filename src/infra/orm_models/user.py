from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.orm_models.article import ORMArticle
from src.infra.orm_models.base import ORMBase
from src.infra.orm_models.mixins import MixinUpdatedAt, MixinUUIDOid


class ORMUser(ORMBase, MixinUUIDOid, MixinUpdatedAt):  # type: ignore[misc]
    __tablename__ = "users"

    nickname: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    articles: Mapped[list[ORMArticle]] = relationship(back_populates="owner")
