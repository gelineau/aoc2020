from dataclasses import dataclass, field
from typing import Iterator, Dict, List, Tuple
from parse import compile

from collections import defaultdict

filename = "puzzle.txt"


@dataclass
class Program:
    mask: str = ""
    instructions: List[Tuple[int, int]] = field(default_factory=list)
    unchanged_mask: int = 0
    value_masks: List[int] = field(default_factory=list)

    def make_unchanged_mask(self):
        self.unchanged_mask = int(
            ''.join('1' if char != '0' else '0' for char in self.mask), base=2)

    def make_value_masks(self):
        self.value_masks = list(self._make_value_masks(self.mask))

    def _make_value_masks(self, mask):
        if 'X' not in mask:
            yield int(mask, base=2)
            return

        index = mask.index('X')
        mask0 = mask[:index] + '0' + mask[index + 1:]
        mask1 = mask[:index] + '1' + mask[index + 1:]
        yield from self._make_value_masks(mask0)
        yield from self._make_value_masks(mask1)


def read_input() -> Iterator[Program]:
    parsing_template = compile(
        "mem[{address:d}] = {value:d}")

    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline()[len('mask = '):].strip()
        program = Program(mask=line)
        for line in file:
            line = line.strip()
            if line.startswith("mem"):
                parsed_line = parsing_template.parse(line).named
                address = parsed_line['address']
                value = parsed_line['value']
                program.instructions.append((address, value))

            else:
                program.make_unchanged_mask()
                program.make_value_masks()
                yield program
                program = Program(mask=line[len('mask = '):])

        program.make_unchanged_mask()
        program.make_value_masks()
        yield program


def apply(value, unchanged_mask, value_mask) -> int:
    unchanged = (value & ~unchanged_mask)
    changed = (unchanged_mask & value_mask)

    return unchanged | changed


input = list(read_input())

print(input)
memory = defaultdict(int)

for program in input:
    for address, value in program.instructions:
        for delta, value_mask in enumerate(program.value_masks):
            new_value = apply(address, program.unchanged_mask, value_mask)
            memory[new_value] = value

print(sum(memory.values()))
