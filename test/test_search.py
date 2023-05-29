import re
from pathlib import Path
from asyncmake.search.base import SearchConfig
from asyncmake.search.searcher import Searcher


class TestSearcher:
    def test_parse(self):
        start_path = Path("test/data/a/b/c/")
        if not start_path.exists():
            start_path.mkdir(parents=True)
        config = SearchConfig(
            start_path=start_path, pattern=re.compile(r"Makefile"), max_depth=-1
        )
        searcher = Searcher().setup(search_config=config).search()
        assert searcher.path.stem == "data"
