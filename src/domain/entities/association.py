from dataclasses import dataclass
from uuid import UUID

from src.domain.entities.base import BaseEntity


@dataclass(kw_only=True)
class ArticleCategoryAssociationEntity(BaseEntity):
    article_oid: UUID
    category_oid: UUID
