from typing import List, Dict, Iterator

from more_itertools import ilen

filename = "puzzle.txt"


def read_input() -> Iterator[Dict[str, str]]:
    with open(filename, "r", encoding="utf-8") as file:
        passport_lines = ""
        for line in file:
            line = line[:-1]  # remove trailing \n
            if line:
                passport_lines = f"{passport_lines} {line}"
            else:
                yield make_key_value_dict(passport_lines)
                passport_lines = ""


def make_key_value_dict(line: str) -> Dict[str, str]:
    print(line)
    key_value_dict = {}
    key_value_pairs = line.split()
    for key_value_pair in key_value_pairs:
        print(key_value_pair)
        key, value = key_value_pair.split(':')
        key_value_dict[key] = value
    return key_value_dict


required_keys = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", }


def is_valid_number(string, min_number=None, max_number=None, size=None):
    if size is not None and len(string) != size:
        return False

    try:
        number = int(string)
        return (min_number is None or min_number <= number) and (
                    max_number is None or number <= max_number)
    except ValueError:
        return False


def is_valid_height(string):
    if string.endswith("cm"):
        return is_valid_number(string[:-2], 150, 193)
    if string.endswith("in"):
        return is_valid_number(string[:-2], 59, 76)
    return False


def is_valid_hcl(string):
    if len(string) != 7:
        return False

    if string[0] != "#":
        return False

    return all(
        ("0" <= char <= "9") or ("a" <= char <= "f") for char in string[1:])


def is_valid(passport):
    if not all(required_key in passport for required_key in required_keys):
        return False

    verifications = (
        is_valid_number(passport["byr"], 1920, 2002, 4),
        is_valid_number(passport["iyr"], 2010, 2020, 4),
        is_valid_number(passport["eyr"], 2020, 2030, 4),
        is_valid_height(passport["hgt"]),
        is_valid_hcl(passport["hcl"]),
        passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        is_valid_number(passport['pid'], size=9)
    )

    return all(verifications)


def valid_number(passports: Iterator[Dict[str, str]]):
    return ilen(passport for passport in passports if is_valid(passport))


passports = read_input()
print(valid_number(passports))
