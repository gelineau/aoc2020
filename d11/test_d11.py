from typing import List

import d11d2
from d11d1 import calculate_seat_number, read_input


def test_should_work_with_test_puzzle():
    filename = "test_puzzle.txt"
    input = read_input(filename)
    actual = calculate_seat_number(input)
    assert actual == 37



def test_should_work_with_puzzle_input():
    filename = "puzzle.txt"
    input = read_input(filename)
    actual = calculate_seat_number(input)
    assert actual == 2277

def test_should_work_with_part2_and_test_puzzle():
    filename = "test_puzzle.txt"
    input = read_input(filename)
    actual = d11d2.calculate_seat_number(input)
    assert actual == 26

def test_should_work_with_part2_and_puzzle_input():
    filename = "puzzle.txt"
    input = read_input(filename)
    actual = d11d2.calculate_seat_number(input)
    assert actual == 2066