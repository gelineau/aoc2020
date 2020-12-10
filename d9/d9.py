from typing import List, Iterator
from collections import Counter

filename = "puzzle.txt"


def read_input() -> Iterator[int]:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield int(line)

input = list(read_input())





for index, number in enumerate(input[25:], start=25):
    found = False
    window = set(input[index-25:index])
    if all((number - candidate) not in window for candidate in window if candidate != number / 2):
        print(number, "is not a sum")

