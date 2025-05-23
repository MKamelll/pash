# pash
Run shell commands from pyhton

```python
from shell import Shell
    
if __name__ == "__main__":
    sh = Shell()
    result = sh.ls("-la") | sh.grep("-ie", "main") > "test.txt"
    result()
```
