from functools import lru_cache
from typing import List, Iterator
from collections import Counter

filename = "puzzle.txt"


def read_input() -> Iterator[int]:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield int(line)


def calculate_differences(input):
    input = [0] + sorted(input)

    return (Counter(next_adapter - adapter for adapter, next_adapter in
                    zip(input, input[1:])))

@lru_cache
def count_arrangements(initial_joltage, adapters):
    if not adapters:
        return 1

    if adapters[0] - initial_joltage > 3:
        return 0

    return count_arrangements(adapters[0], adapters[1:]) + (count_arrangements(
        initial_joltage, adapters[1:]) if len(adapters) > 1 else 0)


if __name__ == "__main__":
    input = sorted(read_input())
    input.append(input[-1] + 3)

    differences = calculate_differences(input)
    print(differences)

    print(differences[1] * differences[3])

    arrangements = count_arrangements(0, tuple(input))
    print(arrangements)
