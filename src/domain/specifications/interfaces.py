from abc import ABC, abstractmethod


class ISpecification(ABC):
    @abstractmethod
    def __bool__(self) -> bool:
        raise NotImplementedError
