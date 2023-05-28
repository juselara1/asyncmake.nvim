import re
from re import Match
from pathlib import Path
from typing import Callable, Tuple
from asyncmake.parse.base import ParsedFile, Rule, MakeFile, ParseConfig


def load(path: Path) -> MakeFile:
    with open(path, "r") as f:
        file = MakeFile(path=path, lines=f.readlines())
    return file


def parse(file: MakeFile, parse_config: ParseConfig) -> ParsedFile:
    fn_parse: Callable[[str], Match | None] = lambda line: re.search(
        parse_config.rule_pattern, line
    )
    fn_rule: Callable[[Tuple[int, Match]], Rule] = lambda case: Rule(
        name=case[1].group("rule"), span=(case[0], *case[1].span())
    )
    matches = map(fn_parse, file.lines)
    matches = ((i, match) for i, match in enumerate(matches) if match is not None)
    rules = list(map(fn_rule, matches))
    return ParsedFile(rules=rules)
