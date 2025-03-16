from src.domain.types.statuses import UserStatus


def test_user_status_values():
    assert UserStatus.active == "active"
    assert UserStatus.banned == "banned"
