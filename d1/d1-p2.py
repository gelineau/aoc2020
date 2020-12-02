from itertools import combinations
from typing import Set, Iterator, Tuple

filename = "d1/d1-p1.txt"


def read_input() -> Set[int]:
    with open(filename, "r", encoding="utf-8") as file:
        return set(int(value) for value in file)


input = read_input()


def find_three_numbers(input: Set[int], sum: int) -> Iterator[
    Tuple[int, int, int]]:
    for value1, value2 in combinations(input, 2):
        if sum - value1 - value2 in input:
            yield value1, value2, sum - value1 - value2


results = find_three_numbers(input, 2020)
print(set(a * b * c for a, b, c in results))
