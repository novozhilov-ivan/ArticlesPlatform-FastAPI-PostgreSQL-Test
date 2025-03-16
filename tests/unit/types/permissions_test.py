from src.domain.types.permissions import Permission


def test_permission_values():
    assert Permission.delete_any_article == "delete_any_article"
    assert Permission.delete_own_article == "delete_own_article"
    assert Permission.edit_any_article == "edit_any_article"
    assert Permission.edit_own_article == "edit_own_article"
    assert Permission.create_article == "create_article"

    assert Permission.delete_any_comment == "delete_any_comment"
    assert Permission.delete_own_comment == "delete_own_comment"
    assert Permission.create_comment == "create_comment"

    assert Permission.manage_complaints == "manage_complaints"
    assert Permission.view_complaints == "view_complaints"

    assert Permission.manage_users == "manage_users"
    assert Permission.ban_users == "ban_users"
