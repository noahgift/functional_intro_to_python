"""Attempt to transpile every notebook snippet via depyler.

Records per-snippet success/failure into ``rust/notebooks/transpile_report.txt``
and writes successful outputs into ``rust/notebooks/<section>/<cell>.rs``.

This is a best-effort signal: many teaching snippets use features depyler
cannot yet handle (REPL-style bare expressions, references to prior-cell
state, pandas/numpy). The point is to track progress and surface what
the depyler subset covers today.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

SNIPPETS = Path("notebooks/_snippets")
OUT_ROOT = Path("rust/notebooks")
REPORT = OUT_ROOT / "transpile_report.txt"


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    rows: list[str] = []
    ok = fail = 0
    for snippet in sorted(SNIPPETS.rglob("*.py")):
        rel = snippet.relative_to(SNIPPETS)
        out = OUT_ROOT / rel.with_suffix(".rs")
        out.parent.mkdir(parents=True, exist_ok=True)
        proc = subprocess.run(
            ["depyler", "transpile", str(snippet), "-o", str(out)],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0 and out.exists():
            rows.append(f"OK   {rel}")
            ok += 1
        else:
            rows.append(f"FAIL {rel}")
            fail += 1
            out.unlink(missing_ok=True)
    REPORT.write_text("\n".join(rows) + f"\n\nTotal: {ok} ok, {fail} fail\n")
    print(f"transpile: {ok} ok, {fail} fail → {REPORT}")


if __name__ == "__main__":
    main()
