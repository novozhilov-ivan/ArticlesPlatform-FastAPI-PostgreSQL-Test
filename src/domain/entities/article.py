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
