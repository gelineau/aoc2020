from d5 import get_row, get_column


def test_row():
    code = "FBFBBFF"
    expected_row = 44

    actual_row = get_row(code)

    assert actual_row == expected_row


def test_column():
    code = "RLR"
    expected_column = 5

    actual_column = get_column(code)

    assert actual_column == expected_column
