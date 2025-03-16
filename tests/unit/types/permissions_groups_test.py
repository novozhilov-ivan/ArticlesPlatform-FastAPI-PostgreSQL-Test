from src.domain.types.permissions import Permission
from src.domain.types.permissions_groups import PermissionGroups


def test_user_permissions_group():
    assert PermissionGroups.user_permissions == frozenset(
        {
            Permission.delete_own_article,
            Permission.edit_own_article,
            Permission.delete_own_comment,
            Permission.create_article,
            Permission.create_comment,
        }
    )


def test_admin_permissions_group():
    assert PermissionGroups.admin_permissions == frozenset(
        {
            Permission.delete_any_article,
            Permission.edit_any_article,
            Permission.delete_any_comment,
            Permission.view_complaints,
            Permission.manage_complaints,
            Permission.manage_users,
            Permission.ban_users,
            Permission.delete_own_article,
            Permission.edit_own_article,
            Permission.delete_own_comment,
            Permission.create_article,
            Permission.create_comment,
        },
    )


def test_permissions_hierarchy():
    assert PermissionGroups.user_permissions.issubset(
        PermissionGroups.admin_permissions
    )
