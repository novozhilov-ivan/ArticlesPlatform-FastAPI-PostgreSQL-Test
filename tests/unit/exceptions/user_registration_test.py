from src.domain.exceptions.user_registration import (
    ArticlePlatformRegistrationException,
    NicknameAlreadyExistException,
    PasswordConstraintException,
)


def test_article_platform_registration_exception():
    expected_message = "Article Platform registration error occurred."
    exception = ArticlePlatformRegistrationException()

    assert exception.message == expected_message


def test_nickname_already_exist_exception():
    nickname = "test_user"
    expected_message = (
        "Article Platform registration error occurred. "
        f"User nickname: {nickname} already exist."
    )

    exception = NicknameAlreadyExistException(nickname=nickname)

    assert exception.message == expected_message
    assert exception.nickname == nickname


def test_password_constraint_exception():
    meta = "Password must be at least 8 characters."
    expected_message = (
        "Article Platform registration error occurred. " f"Password too weak. {meta}"
    )

    exception = PasswordConstraintException(meta=meta)

    assert exception.message == expected_message
    assert exception.meta == meta
