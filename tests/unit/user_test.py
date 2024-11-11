from src.domain.entities.user import UserEntity


def test_create_user():
    assert UserEntity(nickname="some_nickname", password="password")


def test_user_equal_by_lower_nickname():
    user_1 = UserEntity(nickname="some_nickname", password="1")
    user_2 = UserEntity(nickname="SOME_nickname", password="1")
    users_set = set()

    assert user_1 == user_2

    users_set.add(user_1)
    users_set.add(user_2)

    added_user, *_ = users_set

    assert added_user.oid == user_1.oid
