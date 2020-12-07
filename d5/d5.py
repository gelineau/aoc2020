from typing import Iterator

filename = "puzzle.txt"


def read_input() -> Iterator[str]:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


input = read_input()


def get_row(code: str) -> int:
    return int(code.replace('F', '0').replace('B', '1'), base=2)


def get_column(code: str) -> int:
    return int(code.replace('L', '0').replace('R', '1'), base=2)


def get_seat_id(code: str) -> int:
    return get_row(code[:7]) * 8 + get_column(code[-3:])

ids = list(get_seat_id(code) for code in input)

# part 1
result = max(ids)
print(result)

# part 2

ids.sort()

for id, next in zip(ids, ids[1:]):
    if id != next - 1:
        print(id + 1)
