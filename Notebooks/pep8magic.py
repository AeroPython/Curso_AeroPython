# IPython magic to check for PEP8 compliance.
# Author: Juan Luis Cano <juanlu001@gmail.com>

"""IPython magic to check for PEP8 compliance.

To use it, type

```%load_ext pep8magic```

and then

```%%pep8
if 6*9==42:print("Something fundamentally wrong..."  )
```

to see PEP8 failures.

"""

import pep8 as _pep8


def pep8(line, cell):
    lines = cell.splitlines(True)
    lines[-1] += '\n'
    fchecker = _pep8.Checker(lines=lines,
                             show_source=True)
    report = fchecker.check_all()
    if report == 0:
        print("This code is PEP8-compliant!")


def load_ipython_extension(ipython):
    ipython.register_magic_function(pep8, magic_kind='cell')
