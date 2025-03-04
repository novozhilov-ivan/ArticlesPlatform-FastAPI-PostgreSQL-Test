from dataclasses import replace

from src.domain.entities.category import CategoryEntity
from src.domain.repositories.interfaces import ICategoriesRepository
from src.domain.repositories.memory_categories import MemoryCategoriesRepository


async def test_get_by_name_category_in_empty_repository(
    category: CategoryEntity,
    categories_repository: ICategoriesRepository,
):
    assert not await categories_repository.get_by_name(category.name)


async def test_get_by_name_exist_category_in_repository(category: CategoryEntity):
    categories_repository = MemoryCategoriesRepository({category})

    exist_category = await categories_repository.get_by_name(category.name)

    assert exist_category
    assert exist_category == category


async def test_create_many_categories_with_one_category(
    category: CategoryEntity,
    categories_repository: ICategoriesRepository,
):
    await categories_repository.create_many(category)

    exist_category = await categories_repository.get_by_name(category.name)

    assert exist_category
    assert exist_category == category


async def test_create_many_categories_with_many_unique_categories(
    category: CategoryEntity,
    categories_repository: MemoryCategoriesRepository,
):
    unique_categories = {
        replace(category, name=f"{category.name}{digit_name_prefix}")
        for digit_name_prefix in range(3)
    }

    await categories_repository.create_many(*unique_categories)

    assert unique_categories == categories_repository._storage


async def test_create_many_is_create_category_idempotent_with_same_name_cases(
    category: CategoryEntity,
    categories_repository: MemoryCategoriesRepository,
):
    categories = (category for _ in range(5))
    await categories_repository.create_many(*categories)

    assert len(categories_repository._storage) == 1


async def test_create_many_is_create_category_idempotent_with_diff_names_cases(
    category: CategoryEntity,
    categories_repository: MemoryCategoriesRepository,
):
    await categories_repository.create_many(category)

    different_name_cases = {"namE", "NAme", "NAME"}
    categories = (replace(category, name=name) for name in different_name_cases)

    await categories_repository.create_many(*categories)

    assert len(categories_repository._storage) == 1
    exist_category, *_ = categories_repository._storage
    assert exist_category == category
    assert exist_category.name == category.name
