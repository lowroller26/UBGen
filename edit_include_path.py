import re
import subprocess
import os

CWD = os.getcwd()

from pathlib import Path
import re

def main(fileno):
    print(fileno)
    path = Path(f"mutants/{fileno}.c")
    text = path.read_text()

    text = re.sub(
        r'#include\s*[<"]csmith\.h[>"]',
        f'#include "{CWD}/csmith_install/include/csmith-2.3.0/csmith.h"',
        text,
        count=1,
    )

    path.write_text(text)

for root, dirs, files in os.walk("mutants"):
    for file in files:
        name, ext = os.path.splitext(file)
        main(name)
