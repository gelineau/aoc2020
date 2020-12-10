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
        break

invalid_number = number


def find_sequence(invalid_number, input):
    sums_so_far = {} # key = sum, value = corresponding sequence
    for number in input:

        new_sums_so_far = {}
        for existing_sum, existing_numbers in list(sums_so_far.items()) + [
            (0, [])]:
            if number + existing_sum == invalid_number:
                return(existing_numbers + [number])

            if number + existing_sum < invalid_number:
                new_sums_so_far[number + existing_sum] = existing_numbers + [
                    number]

        sums_so_far = new_sums_so_far


sequence = find_sequence(invalid_number, input)
print(min(sequence) + max(sequence))
