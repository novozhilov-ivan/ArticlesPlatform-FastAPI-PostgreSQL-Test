from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from src.domain.entities.base import BaseEntity


if TYPE_CHECKING:
    from src.domain.entities.article import ArticleEntity


@dataclass(eq=False, kw_only=True)
class CategoryEntity(BaseEntity):
    name: str
    articles: set["ArticleEntity"] = field(default_factory=set)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str):
            return self.__str__() == other.lower()
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__str__() == other.__str__()

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __str__(self) -> str:
        return self.name.lower()

    __repr__ = __str__
