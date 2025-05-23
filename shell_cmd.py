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
        self._has_run = False
        self._suppress_printing = False
        for arg in args:
            self.command.append(arg)
        self.process : subprocess.Popen[str] | None = None
    
    def __call__(self) -> str:
        if self._has_run:
            return self._stdout
        self._has_run = True
        self.process = subprocess.Popen(self.command,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if self.process:
            self._stdout, self._stderr = self.process.communicate(input=self._input)
            if len(self._stderr.strip()) > 0:
                print(self._stderr, file=sys.stderr)
                exit(self.process.returncode)
            if not self._suppress_printing:
                print(self._stdout, end="")
        return self._stdout
    
    def __or__(self, other: Self) -> Self:
        self._suppress_printing = True
        self()
        other._input = self._stdout
        self._suppress_printing = False
        return other
    
    def __gt__(self, other: str) -> Self:
        self._suppress_printing = True
        self()
        with open(other, "w") as f:
            f.write(self._stdout)
        self._suppress_printing = False
        return self
    
    def __rshift__(self, other: str) -> Self:
        self._suppress_printing = True
        self()
        with open(other, "a") as f:
            f.write(self._stdout)
        self._suppress_printing = False
        return self
    
    def __lt__(self, other: str) -> Self:
        self._suppress_printing = True
        with open(other, "r") as f:
            self._input = f.read()
        self._suppress_printing = False
        return self
    
    def __lshift__(self, other: str) -> Self:
        self._suppress_printing = True
        self._input = other
        return self
    
    def __xor__(self, other: str) -> Self:
        self._suppress_printing = True
        self()
        with open(other, "w") as f:
            f.write(self._stderr)
        self._suppress_printing = False
        return self

    def __and__(self, other: str) -> Self:
        self._suppress_printing = True
        self()
        with open(other, "w") as f:
            f.write(self._stdout)
            f.write(self._stderr)
        self._suppress_printing = False
        return self
