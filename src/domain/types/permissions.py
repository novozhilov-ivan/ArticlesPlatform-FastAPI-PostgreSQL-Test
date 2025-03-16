from enum import auto, StrEnum


class Permission(StrEnum):
    delete_any_article = auto()
    delete_own_article = auto()
    edit_any_article = auto()
    edit_own_article = auto()
    create_article = auto()

    delete_any_comment = auto()
    delete_own_comment = auto()
    create_comment = auto()

    manage_complaints = auto()
    view_complaints = auto()

    manage_users = auto()
    ban_users = auto()
