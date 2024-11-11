from dataclasses import dataclass

from src.domain.entities.base import BaseEntity


@dataclass(eq=False, kw_only=True)
class CategoryEntity(BaseEntity):
    name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.name.lower() == other.name.lower()

    def __hash__(self) -> int:
        return hash(self.name.lower())
