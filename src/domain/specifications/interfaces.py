from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar


class ISpecification(ABC):
    @abstractmethod
    def __bool__(self) -> bool:
        raise NotImplementedError


@dataclass
class PasswordSpec(ISpecification, ABC):
    plain_password: str
    _on_fail_message_template: ClassVar[str]

    @property
    @abstractmethod
    def on_fail_message(self) -> str:
        raise NotImplementedError
