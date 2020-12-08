from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple, Optional, Iterator
from parse import compile


filename = "puzzle.txt"

@dataclass
class Command:
    index: int
    command: str
    argument: int
    accumulator: Optional[int] = None

def read_input() -> List[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def decode_input(input) -> Iterator[Command]:
    parsing_template = compile(
        "{command} {argument:d}")

    for index, line in enumerate(input):
        decoded_line =  parsing_template.parse(line).named
        yield Command(index, decoded_line['command'], decoded_line['argument'])



input = read_input()

commands = list(decode_input(input))


def test_program(commands: List[Command])->Tuple[bool, int]:
    accumulator = 0
    index = 0
    while True:
        if index >= len(commands):
            is_loop = False
            break

        command = commands[index]
        if command.accumulator is not None:
            is_loop= True
            break
        if command.command == 'acc':
            accumulator += command.argument

        command.accumulator = accumulator
        if command.command == 'jmp':
            index += command.argument
        else:
            index += 1
    return is_loop, accumulator

print(test_program(deepcopy(commands)))


# part 2

for index, command in enumerate(commands):
    modified_commands = deepcopy(commands)
    if command.command == "jmp":
        modified_commands[index].command = "nop"
    elif command.command == "nop":
        modified_commands[index].command = "jmp"
    else:
        continue

    is_loop, accumulator = test_program(modified_commands)
    print(index, is_loop, accumulator)

    if not is_loop:
        print(accumulator)
        break


