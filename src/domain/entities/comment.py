from dataclasses import dataclass
from uuid import UUID

from src.domain.entities.base import BaseEntity


@dataclass(kw_only=True)
class CommentEntity(BaseEntity):
    author_oid: UUID
    article_oid: UUID
    text: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.oid == other.oid

    def __hash__(self) -> int:
        return hash(self.oid)
