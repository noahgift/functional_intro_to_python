"""Teaching module — Brazilian Jiu-Jitsu belt utilities.

Pure-Python, depyler-transpilable. Every public function carries an
icontract pre/postcondition and is exercised by hypothesis property
tests under ``tests/``.
"""

from typing import Final

import icontract

BJJ_BELTS: Final[tuple[str, ...]] = ("white", "blue", "purple", "brown", "black")


@icontract.ensure(lambda result: len(result) == 5)
def list_of_belts_in_bjj() -> list[str]:
    """Return the ordered list of adult belts in Brazilian Jiu-Jitsu.

    Contract:
      - Ensures: returns exactly the five canonical adult belts, in rank order.
    """
    return ["white", "blue", "purple", "brown", "black"]


@icontract.ensure(lambda result: result == 5)
def count_belts() -> int:
    """Count the BJJ belts.

    Contract:
      - Ensures: result equals the number of canonical BJJ belts (5).
    """
    return len(list_of_belts_in_bjj())
