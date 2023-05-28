from pathlib import Path
from re import Pattern
from typing import Sequence, Tuple
from pydantic import BaseModel


class Rule(BaseModel):
    name: str
    span: Tuple[int, int, int]


class ParsedFile(BaseModel):
    rules: Sequence[Rule]


class MakeFile(BaseModel):
    path: Path
    lines: Sequence[str]


class ParseConfig(BaseModel):
    rule_pattern: Pattern
