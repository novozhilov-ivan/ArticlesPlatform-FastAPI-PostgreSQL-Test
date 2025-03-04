from dataclasses import dataclass, field

from src.domain.entities.category import CategoryEntity
from src.domain.repositories.interfaces import ICategoriesRepository


@dataclass
class MemoryCategoriesRepository(ICategoriesRepository):
    _storage: set[CategoryEntity] = field(default_factory=set)

    async def create_many(self, categories: set[CategoryEntity]) -> None:
        for category in categories:
            if category in self._storage:
                continue
            self._storage.add(category)

    async def get_by_name(self, name: str) -> CategoryEntity | None:
        return next(
            (category for category in self._storage if category == name),
            None,
        )
