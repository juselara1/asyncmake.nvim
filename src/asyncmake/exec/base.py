from abc import ABC, abstractmethod
from pathlib import Path
from pydantic import BaseModel


class Command(BaseModel):
    cmd: str
    status: int = -1


class AbstractExecutor(ABC):
    command: Command
    path: Path

    def setup(self, command: Command, path: Path) -> "AbstractExecutor":
        self.command = command
        self.path = path
        return self

    @abstractmethod
    def execute(self) -> "AbstractExecutor":
        ...
