# pash
Run shell commands from pyhton

```python
from shell import Shell
    
if __name__ == "__main__":
    sh = Shell(suppress_printing=True)
    cmd = sh.ls("-la") | sh.grep("-ie", "main") > "test.txt"
    cmd2 = sh.cat() << "this is a line obviously\n"
    
    result = cmd.run()
    result2 = cmd.run()

    print(result.stdout())
    print(result2.stdout())
```
