from dataclasses import dataclass, field
from uuid import UUID

from src.domain.entities.comment import CommentEntity
from src.domain.repositories.interfaces import ICommentsRepository


@dataclass
class MemoryCommentsRepository(ICommentsRepository):
    storage: set[CommentEntity] = field(default_factory=set)

    async def get_list_by_article_oid(self, article_oid: UUID) -> set[CommentEntity]:
        return {
            comment for comment in self.storage if comment.article_oid == article_oid
        }

    async def create(self, comment: CommentEntity) -> None:
        if comment in self.storage:
            return
        self.storage.add(comment)

    async def delete_by_oid(self, oid: UUID) -> None:
        self.storage = {comment for comment in self.storage if comment.oid != oid}
