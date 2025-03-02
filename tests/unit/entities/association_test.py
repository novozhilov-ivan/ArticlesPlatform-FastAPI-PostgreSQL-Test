from src.domain.entities.article import ArticleEntity
from src.domain.entities.association import ArticleCategoryAssociationEntity
from src.domain.entities.category import CategoryEntity


def test_initialize_association_entity(
    article: ArticleEntity,
    category: CategoryEntity,
):
    assert ArticleCategoryAssociationEntity(
        article_oid=article.oid,
        category_oid=category.oid,
    )
