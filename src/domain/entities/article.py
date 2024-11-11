from dataclasses import dataclass

from black.cache import field

from src.domain.entities.base import BaseEntity
from src.domain.entities.category import CategoryEntity


@dataclass(eq=False, kw_only=True)
class ArticleEntity(BaseEntity):
    title: str
    text: str
    categories: set[CategoryEntity] = field(default_factory=set)
