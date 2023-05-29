from abc import ABC, abstractmethod
from pathlib import Path
from typing import Self
from pydantic import BaseModel


class Command(BaseModel):
    cmd: str
    status: int = -1


class AbstractExecutor(ABC):
    command: Command
    path: Path

    def setup(self: Self, command: Command, path: Path) -> Self:
        self.command = command
        self.path = path
        return self

    @abstractmethod
    def execute(self: Self) -> Self:
        ...
