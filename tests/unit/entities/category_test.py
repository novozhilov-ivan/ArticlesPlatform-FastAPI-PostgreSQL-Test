from src.domain.entities.category import CategoryEntity


def test_create_category():
    assert CategoryEntity(name="some_category")


def test_category_equal_by_name():
    categories_set = set()
    category_1 = CategoryEntity(name="some_category")
    category_2 = CategoryEntity(name="some_category")

    assert category_1 == category_2

    categories_set.add(category_1)
    assert len(categories_set) == 1
    categories_set.add(category_2)
    assert len(categories_set) == 1

    received_category, *_ = categories_set
    assert received_category.oid == category_1.oid
