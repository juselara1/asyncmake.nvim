import re
from pathlib import Path
from typing import List
from pynvim import plugin, command
from pynvim.api import Nvim
from asyncmake.search.searcher import Searcher
from asyncmake.search.base import SearchConfig
from asyncmake.parse.base import ParseConfig
from asyncmake.parse.parser import parse, load
from asyncmake.exec.base import Command
from asyncmake.exec.make import MakeExecutor

Args = List[str]

@plugin
class AsyncMake:
    search_config: SearchConfig
    parse_config: ParseConfig

    def __init__(self, nvim: Nvim):
        self.nvim = nvim
        self.load_config()
        self.searcher = Searcher().setup(search_config=self.search_config)
        self.executor = MakeExecutor()

    def load_config(self):
        self.search_config = SearchConfig(
                start_path=Path(str(self.nvim.call("getcwd"))),
                pattern=re.compile(r"Makefile"),
                max_depth=5
            )
        self.parse_config = ParseConfig(
                rule_pattern=re.compile(r"^(?P<rule>\w+):")
                )

    @command(name="MakeFn", nargs="*", sync=True, range="") # type: ignore
    def make(self, args: Args, range=None):
        cmd = " ".join(args)
        self.search_config.start_path = Path(str(self.nvim.call("getcwd")))
        self.searcher.search()
        self.executor.setup(command=Command(cmd=cmd), path=self.searcher.path).execute()
