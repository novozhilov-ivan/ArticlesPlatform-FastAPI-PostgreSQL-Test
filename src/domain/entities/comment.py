from dataclasses import dataclass
from uuid import UUID

from src.domain.entities.base import BaseEntity


@dataclass(kw_only=True)
class CommentEntity(BaseEntity):
    author_oid: UUID
    text: str
