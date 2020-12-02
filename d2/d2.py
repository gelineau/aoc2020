from dataclasses import dataclass
from typing import Iterator, Callable, List

from more_itertools import ilen

filename = "puzzle.txt"
from parse import compile


@dataclass
class PasswordData:
    min_char_number: int
    max_char_number: int
    char: str
    password: str


def read_input(filename: str) -> Iterator[PasswordData]:
    parsing_template = compile(
        "{min_char_number:d}-{max_char_number:d} {char}: {password}")

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parsed_line = parsing_template.parse(line).named
            yield PasswordData(**parsed_line)


def is_valid_p1(result: PasswordData) -> bool:
    char_number = result.password.count(result.char)
    return result.min_char_number <= char_number <= result.max_char_number


def xor(a: bool, b: bool) -> bool:
    return a + b == 1


def is_valid_p2(result: PasswordData) -> bool:
    first_position_matches = result.password[
                                 result.min_char_number - 1] == result.char
    second_position_matches = result.password[
                                  result.max_char_number - 1] == result.char
    return xor(first_position_matches, second_position_matches)


def valid_result_number(input: List[PasswordData],
                        validation_function: Callable[
                            [PasswordData], bool]) -> int:
    return ilen(result for result in input if validation_function(result))


input = list(read_input(filename))
for validation_function in (is_valid_p1, is_valid_p2):
    print(valid_result_number(input, validation_function))
