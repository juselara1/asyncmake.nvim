from pathlib import Path
from asyncmake.exec.base import Command
from asyncmake.exec.make import MakeExecutor


class TestExecutor:
    def test_make(self):
        path = Path("test/data")
        command = Command(cmd="rule1")
        executor = MakeExecutor().setup(command=command, path=path).execute()
        assert executor.command.status == 0
        command = Command(cmd="rule_2")
        executor.setup(command=command, path=path).execute()
        assert executor.command.status == 0
