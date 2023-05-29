import os
from asyncmake.exec.base import AbstractExecutor
from typing import Self


class MakeExecutor(AbstractExecutor):
    def execute(self: Self) -> Self:
        cur_dir = os.getcwd()
        os.chdir(self.path)
        status = os.system(f"make {self.command.cmd}")
        os.chdir(cur_dir)
        self.command.status = status
        return self
