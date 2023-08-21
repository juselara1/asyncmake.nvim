from abc import ABC, abstractmethod
from pathlib import Path
from re import Pattern
from pydantic import BaseModel


class SearchConfig(BaseModel):
    start_path: Path
    pattern: Pattern
    max_depth: int


class AbstractSearcher(ABC):
    config: SearchConfig
    path: Path

    def setup(self, search_config: SearchConfig) -> "AbstractSearcher":
        self.config = search_config
        return self

    @abstractmethod
    def search(self) -> "AbstractSearcher":
        ...
