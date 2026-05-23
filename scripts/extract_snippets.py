"""Extract Python code cells from the Section 1-4 notebooks into snippet files.

Skips cells containing IPython magics (lines starting with ``%`` or ``!``)
and pure-expression cells that don't survive linting. Each surviving cell
is emitted as ``notebooks/_snippets/section_N/cell_NN.py`` so it can be
linted, type-checked, and (optionally) transpiled with ``depyler``.
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

NOTEBOOKS = {
    1: "notebooks/Functional_Introduction_To_Python_Section_1(Introductory_Concepts).ipynb",
    2: "notebooks/Functional_Introduction_To_Python_Section_2(Functions).ipynb",
    3: "notebooks/Functional_Introduction_To_Python_Section_3(Control_Structures).ipynb",
    4: "notebooks/Functional_Introduction_To_Python_Section_4(Intermediate_Topics).ipynb",
}

MAGIC = re.compile(r"^\s*[%!]")
OUT_ROOT = Path("notebooks/_snippets")


def cell_is_clean(src: str) -> bool:
    """Clean = no IPython magics/shell lines AND parses as valid Python."""
    if any(MAGIC.match(line) for line in src.splitlines()):
        return False
    try:
        ast.parse(src)
    except SyntaxError:
        return False
    return True


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    total = kept = 0
    for section, path in NOTEBOOKS.items():
        nb = json.loads(Path(path).read_text())
        sec_dir = OUT_ROOT / f"section_{section}"
        sec_dir.mkdir(exist_ok=True)
        idx = 0
        for cell in nb.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            total += 1
            src = "".join(cell.get("source", []))
            if not src.strip():
                continue
            if not cell_is_clean(src):
                continue
            idx += 1
            out = sec_dir / f"cell_{idx:02d}.py"
            header = f'"""Section {section}, cell {idx} — extracted from {Path(path).name}."""\n\n'
            out.write_text(header + src.rstrip() + "\n")
            kept += 1
    print(f"extracted {kept} of {total} code cells into {OUT_ROOT}")


if __name__ == "__main__":
    main()
