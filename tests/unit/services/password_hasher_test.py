from src.domain.services.password_hasher import PasswordHasherService


def test_hash_password_returns_string(
    plain_password: str,
    hashed_password: str,
):
    assert isinstance(hashed_password, str)
    assert hashed_password != plain_password


def test_verify_password_correct(
    plain_password: str,
    hashed_password: str,
    password_hasher: PasswordHasherService,
):
    assert password_hasher.verify_password(plain_password, hashed_password)


def test_verify_password_incorrect(
    hashed_password: str,
    password_hasher: PasswordHasherService,
):
    another_plain_password = "another_plain_password"

    assert not password_hasher.verify_password(
        another_plain_password,
        hashed_password,
    )


def test_hash_password_generates_different_hashes(
    hashed_password: str,
    password_hasher: PasswordHasherService,
):
    another_plain_password = "another_plain_password"
    another_hashed_password = password_hasher.hash_password(another_plain_password)

    assert another_hashed_password != hashed_password
