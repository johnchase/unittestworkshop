from utw.basics import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_numbers_none():
    try:
        add_numbers(None, 3)
    except ValueError as e:
        assert str(e) == "All arguments a, b, and c must be provided"
    else:
        assert False, "Expected ValueError not raised"
