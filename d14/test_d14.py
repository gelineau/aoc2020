from d14 import Program, apply


def test_apply():
    value = 11
    mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'

    expected = 73

    program = Program(mask=mask)
    program.make_value_mask()
    program.make_unchanged_mask()

    actual = apply(value, program.unchanged_mask, program.value_mask)

    assert actual == expected