# pash
Run shell commands from pyhton

Available on pypi [pash-py](https://pypi.org/project/pash-py/)

```python
from shell import Shell

# Create a shell instance    
sh = Shell(suppress_printing=True)

# create a command
cmd = sh.ls("-la") | sh.grep("-ie", "main") > "test.txt"
cmd2 = sh.cat() << "this is a line obviously\n"

# you could use sh.command(command, *args) if the function you want not present in the module
# or submit a pull request if you want it incorporated

# run the command
cmd()
cmd2()

# print the command output
print(cmd.stdout()) # print(cmd.stderr())
print(cmd2.stdout()) # print(cmd.stderr())
```
