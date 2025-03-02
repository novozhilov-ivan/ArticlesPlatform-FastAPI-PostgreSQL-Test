from dataclasses import dataclass, field
from uuid import UUID

from src.domain.entities.base import BaseEntity
from src.domain.entities.category import CategoryEntity


@dataclass(eq=False, kw_only=True)
class ArticleEntity(BaseEntity):
    author_oid: UUID
    title: str
    text: str
    categories: set[CategoryEntity] = field(default_factory=set)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UUID):
            return self.oid == other
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.oid == other.oid

    def __hash__(self) -> int:
        return hash(self.oid)

    def __str__(self) -> str:
        return self.title

    __repr__ = __str__
