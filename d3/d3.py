from typing import List

from more_itertools import ilen

width = len("#.#......#.......#..#.#..#.....")
tree = "#"

filename = "puzzle.txt"


def read_input() -> List[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def is_tree(maze: List[str], row: int, column: int) -> bool:
    reduced_column = column % width
    return maze[row][reduced_column] == tree


def tree_number(maze: List[str], height: int, down_slope: int,
                right_slope: int):
    tree_number = 0
    for step, row in enumerate(range(0, height, down_slope)):
        column = step * right_slope
        if is_tree(maze, row, column):
            tree_number += 1

    return tree_number


maze = read_input()
height = len(maze)

right_slope = 3
down_slope = 1

slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)]

result = 1
for right_slope, down_slope in slopes:
    result *= tree_number(maze, height, down_slope, right_slope)

print(result)
