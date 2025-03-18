from typing import Final

from src.domain.types.permissions import Permission


class RolesPermissions:
    user: Final[frozenset[Permission]] = frozenset(
        {
            Permission.delete_own_article,
            Permission.edit_own_article,
            Permission.delete_own_comment,
            Permission.create_article,
            Permission.create_comment,
        },
    )

    admin: Final[frozenset[Permission]] = frozenset(
        {
            Permission.delete_any_article,
            Permission.edit_any_article,
            Permission.delete_any_comment,
            Permission.view_complaints,
            Permission.manage_complaints,
            Permission.manage_users,
            Permission.ban_users,
        }
        | user,
    )
