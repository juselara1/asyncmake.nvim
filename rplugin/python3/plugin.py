import re
from pathlib import Path
from typing import Callable, List
from pynvim import plugin, command, function
from pynvim.api import Nvim
from asyncmake.search.searcher import Searcher
from asyncmake.search.base import SearchConfig
from asyncmake.parse.base import ParseConfig, Rule
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
            max_depth=5,
        )
        self.parse_config = ParseConfig(
            rule_pattern=re.compile(r"^(?P<rule>[a-zA-Z\-_%]+):")
        )

    @command(name="Make", nargs="*", sync=False, range="")  # type: ignore
    def make(self, args: Args, range=None):
        cmd = " ".join(args)
        self.nvim.api.exec2(f"MakeStartMsg {cmd}", {})
        self.search_config.start_path = Path(str(self.nvim.call("getcwd")))
        self.searcher.search()

        self.executor.setup(command=Command(cmd=cmd), path=self.searcher.path).execute()
        if self.executor.command.status == 0:
            self.nvim.api.exec2(f"MakeEndMsg {cmd}", {})
        else:
            self.nvim.api.exec2(
                f"MakeErr {cmd} with status {self.executor.command.status}", {}
            )

    @command("MakeParsedOpts", nargs=0, sync=True, range="")
    def make_parsed_opts(self, args: Args, range=None) -> str:
        fn_rule: Callable[[Rule], str] = lambda rule: rule.name
        self.search_config.start_path = Path(str(self.nvim.call("getcwd")))
        self.searcher.search()
        file = load(self.searcher.path / "Makefile")
        parsed_file = parse(file, self.parse_config)
        rules = map(fn_rule, parsed_file.rules)
        self.nvim.out_write(" ".join(rules) + "\n")
