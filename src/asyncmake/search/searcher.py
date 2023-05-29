import re
from pathlib import Path
from re import Match
from typing import Callable, Self
from asyncmake.search.base import AbstractSearcher

class Searcher(AbstractSearcher):
    def search(self: Self) -> Self:
        fn_match: Callable[[Path], Match | None] = lambda path: re.search(self.config.pattern, path.stem)
        cur_depth = 1
        cur_path = self.config.start_path
        files = map(fn_match, cur_path.glob("*"))
        matches = list(filter(lambda x: x is not None, files))
        while not matches and cur_depth != self.config.max_depth:
            cur_path = cur_path / ".."
            cur_depth += 1
            files = map(fn_match, cur_path.glob("*"))
            matches = list(filter(lambda x: x is not None, files))
        if matches:
            self.path = cur_path.resolve()

        return self
