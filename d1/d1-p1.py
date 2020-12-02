from typing import Set

filename = "d1/d1-p1.txt"

def read_input()->Set[int]:
    with open(filename, "r", encoding="utf-8") as file:
        return set(int(value) for value in file)

input = read_input()

for value1 in input:
    if (2020 - value1) in input:
        print(f"value1: {value1}, value2: {2020 - value1}, product: {value1*(2020 - value1)}")
