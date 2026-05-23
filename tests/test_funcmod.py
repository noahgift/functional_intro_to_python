"""Unit + property tests for funclib.funcmod."""

from hypothesis import given
from hypothesis import strategies as st

from funclib.funcmod import BJJ_BELTS, count_belts, list_of_belts_in_bjj


def test_list_of_belts_in_bjj() -> None:
    assert list_of_belts_in_bjj() == ["white", "blue", "purple", "brown", "black"]


def test_count_belts() -> None:
    assert count_belts() == 5


def test_belts_are_rank_ordered() -> None:
    assert BJJ_BELTS[0] == "white"
    assert BJJ_BELTS[-1] == "black"


@given(st.integers(min_value=0, max_value=50))
def test_list_is_pure_and_independent_of_call_count(_n: int) -> None:
    """list_of_belts_in_bjj is pure: identical output every call."""
    first = list_of_belts_in_bjj()
    for _ in range(_n):
        assert list_of_belts_in_bjj() == first


@given(st.integers(min_value=1, max_value=20))
def test_count_belts_is_invariant(_n: int) -> None:
    """count_belts always returns the canonical belt count."""
    for _ in range(_n):
        assert count_belts() == len(BJJ_BELTS)


def test_returned_list_is_a_copy_not_shared_state() -> None:
    """Mutating the returned list must not affect later calls."""
    first = list_of_belts_in_bjj()
    first.append("rainbow")
    assert list_of_belts_in_bjj() == list(BJJ_BELTS)
