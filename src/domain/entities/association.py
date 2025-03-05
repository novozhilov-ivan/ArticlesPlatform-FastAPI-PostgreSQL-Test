from dataclasses import dataclass
from operator import eq
from uuid import UUID

from src.domain.entities.base import BaseEntity


@dataclass(kw_only=True)
class ArticleCategoryAssociationEntity(BaseEntity):
    article_oid: UUID
    category_name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return eq(
            (self.article_oid, self.category_name.lower()),
            (other.article_oid, other.category_name.lower()),
        )

    def __hash__(self) -> int:
        return hash((self.article_oid, self.category_name.lower()))
