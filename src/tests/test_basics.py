import pytest

from utw.basics import add_numbers, divide, parse_age


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, -1, -2),
        (1.5, 2.5, 4.0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add_numbers(a, b) == expected


def test_divide_valid():
    assert divide(10, 2) == 5


def test_divide_raises_zero_division():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(5, 0)


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("25", 25),
        ("  42  ", 42),
        ("0", 0),
        ("130", 130),
    ],
)
def test_parse_age_valid(input_str, expected):
    assert parse_age(input_str) == expected


@pytest.mark.parametrize("input_str", ["", "abc", "42.5", "-10", "150", "twenty"])
def test_parse_age_invalid(input_str):
    with pytest.raises(ValueError):
        parse_age(input_str)
