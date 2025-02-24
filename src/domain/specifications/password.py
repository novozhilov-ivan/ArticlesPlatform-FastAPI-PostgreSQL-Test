from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import ClassVar

from src.domain.specifications.interfaces import ISpecification, PasswordSpec


@dataclass
class PasswordLengthSpec(PasswordSpec, ISpecification):
    _min_len: ClassVar[int] = 6
    _max_len: ClassVar[int] = 40
    _on_fail_message_template: ClassVar[str] = (
        "Password length cannot be:"
        " less then {min_len} characters and"
        " more then {max_len} characters!"
    )

    @property
    def on_fail_message(self) -> str:
        return self._on_fail_message_template.format(
            min_len=self._min_len,
            max_len=self._max_len,
        )

    def _valid_min_length(self) -> bool:
        return len(self.plain_password) >= self._min_len

    def _valid_max_length(self) -> bool:
        return len(self.plain_password) <= self._max_len

    def __bool__(self) -> bool:
        return self._valid_min_length() and self._valid_max_length()


@dataclass
class PasswordCompositeSpec(PasswordSpec, ISpecification):
    plain_password: str
    _specifications: tuple[type[PasswordSpec], ...] = field(
        default_factory=lambda: (PasswordLengthSpec,),
    )
    _on_fail_message_template: ClassVar[str] = (
        "Password format restrictions are not passed.\n"
    )

    def _init_all_specifications(self) -> Iterable:
        return (
            specification(plain_password=self.plain_password)
            for specification in self._specifications
        )

    def __bool__(self) -> bool:
        return all(self._init_all_specifications())

    @property
    def on_fail_message(self) -> str:
        failed_messages = [
            spec.on_fail_message
            for spec in self._init_all_specifications()
            if not spec
        ]
        return f"{self._on_fail_message_template}{'\n'.join(failed_messages)}"
