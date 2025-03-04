from abc import ABC, abstractmethod
from collections.abc import Sequence
from uuid import UUID

from src.domain.entities.article import ArticleEntity
from src.domain.entities.category import CategoryEntity
from src.domain.entities.comment import CommentEntity
from src.domain.entities.user import UserEntity


class IArticlesRepository(ABC):
    @abstractmethod
    async def create(self, article: ArticleEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_oid(self, oid: UUID) -> ArticleEntity | None:
        raise NotImplementedError

    @abstractmethod
    async def list(self) -> set[ArticleEntity]:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_oid(self, oid: UUID) -> None:
        raise NotImplementedError


class ICategoriesRepository(ABC):
    @abstractmethod
    async def create_many(self, *categories: CategoryEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_name(self, name: str) -> CategoryEntity | None:
        raise NotImplementedError


class IUsersRepository(ABC):
    @abstractmethod
    async def get_by_nickname(self, nickname: str) -> UserEntity | None:
        raise NotImplementedError

    @abstractmethod
    async def create(self, user: UserEntity) -> None:
        raise NotImplementedError


class ICommentsRepository(ABC):
    @abstractmethod
    async def get_all_article_comments_by_article_oid(
        self,
        oid: UUID,
    ) -> Sequence[CommentEntity]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, comment: CommentEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_by_oid(self, oid: CommentEntity) -> None:
        raise NotImplementedError
