from typing import Set, Iterator, Tuple

filename = "d1-p1.txt"


def read_input() -> Set[int]:
    with open(filename, "r", encoding="utf-8") as file:
        return set(int(value) for value in file)


def find_two_numbers(input: Set[int], sum: int) -> Iterator[int]:
    for value1 in input:
        if (sum - value1) in input:
            yield value1


input = read_input()


def find_three_numbers(input: Set[int], sum: int) -> Iterator[
    Tuple[int, int, int]]:
    for value1 in input.copy():
        input.remove(value1)
        results = find_two_numbers(input, sum - value1)
        yield from ((value1, value2, sum - value1 - value2) for value2 in results)

results = find_three_numbers(input, 2020)
print(list(a * b * c for (a, b, c) in results))
