import re
from pathlib import Path
from asyncmake.parse.parser import load, parse
from asyncmake.parse.base import ParseConfig, ParsedFile


class TestParser:
    def test_parse(self):
        parse_config = ParseConfig(rule_pattern=re.compile(r"^(?P<rule>\w+):"))
        file = load(Path("test/data/Makefile"))
        parsed_file = parse(file, parse_config)
        assert isinstance(parsed_file, ParsedFile)
        assert parsed_file.rules[0].name == "rule1" and parsed_file.rules[0].span == (
            2,
            0,
            6,
        )

        assert parsed_file.rules[1].name == "rule_2" and parsed_file.rules[1].span == (
            5,
            0,
            7,
        )
