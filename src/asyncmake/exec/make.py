import os
from asyncmake.exec.base import AbstractExecutor
from typing import Self


class MakeExecutor(AbstractExecutor):
    def execute(self: Self) -> Self:
        status = os.system(f"make {self.command.cmd}")
        self.command.status = status
        return self
