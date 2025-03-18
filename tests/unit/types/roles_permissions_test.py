from src.domain.types.permissions import Permission
from src.domain.types.roles_permissions import RolesPermissions


def test_user_permissions():
    assert RolesPermissions.user == frozenset(
        {
            Permission.delete_own_article,
            Permission.edit_own_article,
            Permission.delete_own_comment,
            Permission.create_article,
            Permission.create_comment,
        },
    )


def test_admin_permissions():
    assert RolesPermissions.admin == frozenset(
        {
            Permission.delete_any_article,
            Permission.edit_any_article,
            Permission.delete_any_comment,
            Permission.view_complaints,
            Permission.manage_complaints,
            Permission.manage_users,
            Permission.ban_users,
        }
        | RolesPermissions.user,
    )


def test_user_permissions_subset_of_admin():
    assert RolesPermissions.user.issubset(RolesPermissions.admin)
