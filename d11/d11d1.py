from copy import deepcopy
from typing import List, Tuple

from more_itertools import ilen

empty_seat = "L"
occupied_seat = "#"
floor = "."

deltas = [(dx, dy) for dx in range(-1,2) for dy in range(-1, 2) if not (dx == 0 and dy==0)]

def read_input(filename) -> List[List[str]]:
    with open(filename, "r", encoding="utf-8") as file:
        return [[char for char in line.strip()]
                for line in file]

def count_occupied_neighbours(input, row, column):
    return ilen(1
                for drow, dcolumn in deltas if input[row+drow][column+dcolumn] == occupied_seat)


def evolve(input: List[List[str]], width: int, height: int)  -> Tuple[List[List[str]], bool]:
    new_input = deepcopy(input)
    changed = False
    for row in range(1, height-1):
        for column in range(1, width-1):
            cell = input[row][column]
            if cell == floor:
                continue

            occupied_neighbours_number = count_occupied_neighbours(input, row, column)
            if occupied_neighbours_number == 0 and cell != occupied_seat:
                new_input[row][column] = occupied_seat
                changed = True

            if occupied_neighbours_number >= 4 and cell != empty_seat:
                new_input[row][column] = empty_seat
                changed = True

    return new_input, changed


def count_occupied_seats(input)-> int:
    return ilen(1 for row in input for cell in row if cell == occupied_seat )


def calculate_seat_number(input: List[List[str]]):
    width = len(input[0])
    height = len(input)

    input = add_borders(input, width)

    width += 2
    height += 2

    while True:
        input, changed = evolve(input, width, height)
        if not changed:
            return count_occupied_seats(input)


def add_borders(input, width):
    input = [[floor for _ in range(width + 2)]] + [[floor] + line + [floor] for
                                                   line in input] + [[floor for
                                                                     _ in range(
            width + 2)]]
    return input


if __name__ == "__main__":
    filename = "test_puzzle.txt"
    input = read_input(filename)
    actual = calculate_seat_number(input)
    print(actual)