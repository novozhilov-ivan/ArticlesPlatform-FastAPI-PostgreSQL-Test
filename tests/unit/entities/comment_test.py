from dataclasses import replace
from uuid import uuid4

from src.domain.entities.article import ArticleEntity
from src.domain.entities.comment import CommentEntity
from src.domain.entities.user import UserEntity


def test_create_comment(user: UserEntity, article: ArticleEntity):
    assert CommentEntity(
        article_oid=article.oid,
        author_oid=user.oid,
        text="text",
    )


def test_comment_eq_with_other_comment(comment: CommentEntity):
    other_comment = replace(
        comment,
        oid=uuid4(),
    )

    assert comment != other_comment


def test_comment_eq_with_other(comment: CommentEntity):
    other = 42

    assert comment != other
    assert comment.__eq__(other) is NotImplemented
