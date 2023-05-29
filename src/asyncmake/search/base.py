from abc import ABC, abstractmethod
from pathlib import Path
from re import Pattern
from typing import Self
from pydantic import BaseModel


class SearchConfig(BaseModel):
    start_path: Path
    pattern: Pattern
    max_depth: int


class AbstractSearcher(ABC):
    config: SearchConfig
    path: Path

    def setup(self: Self, search_config: SearchConfig) -> Self:
        self.config = search_config
        return self

    @abstractmethod
    def search(self: Self) -> Self:
        ...
