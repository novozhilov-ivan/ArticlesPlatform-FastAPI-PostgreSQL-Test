from src.domain.exceptions.user_authentication import (
    InvalidCredentialsException,
    UserAuthenticationServiceException,
    UserIsBannedException,
)


def test_invalid_credentials_exception():
    exception = InvalidCredentialsException(nickname="test_user")
    assert exception.message == "Invalid credentials nickname or password."


def test_user_is_banned_exception():
    exception = UserIsBannedException(nickname="banned_user")
    assert exception.message == "User banned_user is banned."


def test_user_auth_service_exception():
    exception = UserAuthenticationServiceException()
    assert exception.message == "User authentication service exception occurred."
