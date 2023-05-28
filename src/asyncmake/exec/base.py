from abc import ABC, abstractmethod
from typing import Self
from pydantic import BaseModel


class Command(BaseModel):
    cmd: str
    status: int = -1


class AbstractExecutor(ABC):
    command: Command

    def setup(self: Self, command: Command) -> Self:
        self.command = command
        return self

    @abstractmethod
    def execute(self: Self) -> Self:
        ...
