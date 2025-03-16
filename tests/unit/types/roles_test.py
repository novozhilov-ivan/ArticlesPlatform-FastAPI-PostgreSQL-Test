from src.domain.types.roles import Role


def test_role_values():
    assert Role.admin == "admin"
    assert Role.user == "user"
