from src.domain.entities.article import ArticleEntity
from src.domain.entities.association import ArticleCategoryAssociationEntity
from src.domain.entities.category import CategoryEntity


def test_initialize_association_entity(
    article: ArticleEntity,
    category: CategoryEntity,
):
    assert ArticleCategoryAssociationEntity(
        article_oid=article.oid,
        category_name=category.name,
    )


def test_hash_association_entity(association: ArticleCategoryAssociationEntity):
    assert hash(association) == hash(
        (
            association.article_oid,
            association.category_name.lower(),
        )
    )
    assert hash(association) == hash(
        ArticleCategoryAssociationEntity(
            article_oid=association.article_oid,
            category_name=association.category_name.lower(),
        )
    )


def test_eq_association_entity_with_other(
    association: ArticleCategoryAssociationEntity,
):
    other = ArticleCategoryAssociationEntity(
        article_oid=association.article_oid,
        category_name=association.category_name.lower(),
    )
    assert association == other


def test_eq_association_entity_with_not_association_object(
    association: ArticleCategoryAssociationEntity,
):
    other = 42
    assert association != other
    assert association.__eq__(other) is NotImplemented
