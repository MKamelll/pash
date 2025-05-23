import subprocess
import sys
from typing import Self

class Cmd:
    def __init__(self, cmd: str, args: list[str]) -> None:
        self.command: list[str] = []
        self.command.append(cmd)
        self._stdout: str = ""
        self._stderr: str = ""
        self._input: str = ""
        for arg in args:
            self.command.append(arg)
        self.process : subprocess.Popen[str] | None = None
    
    def __call__(self) -> str:
        self.process = subprocess.Popen(self.command,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if self.process:
            self._stdout, self._stderr = self.process.communicate(input=self._input)
            if len(self._stderr.strip()) > 0:
                print(self._stderr, file=sys.stderr)
                exit(self.process.returncode)
        return self._stdout
    
    def __or__(self, other: Self) -> Self:
        self()
        other._input = self._stdout
        other()
        return other    
