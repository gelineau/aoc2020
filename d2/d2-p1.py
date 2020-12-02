from dataclasses import dataclass
from typing import Iterator

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


def is_valid(result: PasswordData) -> bool:
    char_number = result.password.count(result.char)
    return result.min_char_number <= char_number <= result.max_char_number


def valid_result_number(input: Iterator[PasswordData]) -> int:
    return len([1 for result in input if is_valid(result)])


input = read_input(filename)
print(valid_result_number(input))
