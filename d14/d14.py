from dataclasses import dataclass, field
from typing import Iterator, Dict, List, Tuple
from parse import compile


filename = "puzzle.txt"

@dataclass
class Program:
    mask: str = ""
    instructions: List[Tuple[int, int]] = field(default_factory=list)
    unchanged_mask : int = 0
    value_mask : int = 0
    def make_unchanged_mask(self):
        self.unchanged_mask =  int(''.join('1' if char == 'X' else '0' for char in self.mask), base=2)

    def make_value_mask(self):
        self.value_mask = int(
            ''.join('0' if char == 'X' else char  for char in self.mask), base=2)


def read_input() -> Iterator[Program]:
    parsing_template = compile(
        "mem[{address:d}] = {value:d}")

    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline()[len('mask = '):].strip()
        program = Program(mask = line)
        for line in file:
            line = line.strip()
            if line.startswith("mem"):
                parsed_line = parsing_template.parse(line).named
                address = parsed_line['address']
                value = parsed_line['value']
                program.instructions.append((address, value))

            else:
                program.make_unchanged_mask()
                program.make_value_mask()
                yield program
                program = Program(mask=line[len('mask = '):])

        program.make_unchanged_mask()
        program.make_value_mask()
        yield program


def apply(value, unchanged_mask, value_mask)->int:
    return (value & unchanged_mask) | value_mask




input = list(read_input())
memory = {
}
for program in input:
    for address, value in program.instructions:
        new_value = apply(value, program.unchanged_mask, program.value_mask)
        memory[address] = new_value

print(sum(memory.values()))