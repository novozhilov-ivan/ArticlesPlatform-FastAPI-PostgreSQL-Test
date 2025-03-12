from src.domain.entities.article import ArticleEntity
from src.domain.entities.comment import CommentEntity
from src.domain.repositories.memory_comments import MemoryCommentsRepository


async def test_comment_create_in_empty_repository(
    comment: CommentEntity,
    comments_repository: MemoryCommentsRepository,
):
    await comments_repository.create(comment)

    assert comments_repository.storage == {comment}


async def test_comment_create_idempotent_in_repository(
    comment: CommentEntity,
    comments_repository: MemoryCommentsRepository,
):
    await comments_repository.create(comment)
    await comments_repository.create(comment)

    assert comments_repository.storage == {comment}


async def test_get_list_by_article_oid_from_empty_repository(
    article: ArticleEntity,
    comments_repository: MemoryCommentsRepository,
):
    comment_list = await comments_repository.get_list_by_article_oid(article.oid)

    assert not comment_list


async def test_get_list_by_article_oid_from_repository(
    article: ArticleEntity,
    comment: CommentEntity,
    comments_repository: MemoryCommentsRepository,
):
    comments_repository.storage = {comment}

    comment_list = await comments_repository.get_list_by_article_oid(article.oid)

    assert comment_list == {comment}


async def test_delete_by_oid_in_empty_repository_have_no_effect(
    comment: CommentEntity,
    comments_repository: MemoryCommentsRepository,
):
    assert not comments_repository.storage

    await comments_repository.delete_by_oid(comment.oid)

    assert not comments_repository.storage


async def test_delete_by_oid_in_repository(
    comment: CommentEntity,
    comments_repository: MemoryCommentsRepository,
):
    comments_repository.storage = {comment}

    await comments_repository.delete_by_oid(comment.oid)

    assert not comments_repository.storage
