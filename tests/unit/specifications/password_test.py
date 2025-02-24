import pytest

from src.domain.specifications.password import (
    PasswordCompositeSpec,
    PasswordLengthSpec,
    PasswordSpec,
)


def test_password_length_spec():
    spec = PasswordLengthSpec(plain_password="super_secret")
    assert spec

    if spec:
        assert spec

    assert spec._valid_min_length()
    assert spec._valid_max_length()


def test_password_length_spec_on_short_password():
    spec = PasswordLengthSpec(plain_password="short")
    assert not spec

    if not spec:
        assert not spec

    assert not spec._valid_min_length()
    assert spec._valid_max_length()


def test_password_length_spec_on_long_password():
    spec = PasswordLengthSpec(plain_password="too_long" * 10)
    assert not spec

    if not spec:
        assert not spec

    assert spec._valid_min_length()
    assert not spec._valid_max_length()


def test_password_length_spec_on_fail_message():
    min_len, max_len = PasswordLengthSpec._min_len, PasswordLengthSpec._max_len
    on_fail_message = (
        f"Password length cannot be: less then {min_len} characters and"
        f" more then {max_len} characters!"
    )

    spec = PasswordLengthSpec(plain_password="1")
    assert spec.on_fail_message == on_fail_message


def test_password_composite_spec():
    spec = PasswordCompositeSpec(plain_password="super_secret")
    assert spec


def test_password_composite_spec_on_fail_message_for_valid_password():
    spec = PasswordCompositeSpec(plain_password="super_secret")
    assert spec.on_fail_message == PasswordCompositeSpec._on_fail_message_template


@pytest.mark.parametrize(
    "password",
    [
        "short",
        "too_long" * 10,
    ],
)
def test_password_composite_spec_on_fail_message_for_invalid_password(password: str):
    composite_spec = PasswordCompositeSpec(plain_password=password)
    specs_list: tuple[type[PasswordSpec], ...] = composite_spec._specifications

    result_of_specs_list: tuple[PasswordSpec, ...] = tuple(
        spec(plain_password=password) for spec in specs_list
    )
    not_passed_specs_on_fail_messages_list: list[str] = [
        spec.on_fail_message for spec in result_of_specs_list if not spec
    ]
    not_passed_specs_joined_on_fail_message: str = "\n".join(
        not_passed_specs_on_fail_messages_list,
    )
    result_composite_on_fail_message = (
        f"{composite_spec._on_fail_message_template}"
        f"{not_passed_specs_joined_on_fail_message}"
    )

    assert composite_spec.on_fail_message == result_composite_on_fail_message
