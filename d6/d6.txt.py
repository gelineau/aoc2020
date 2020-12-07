from typing import Iterator, Dict, List, Set

filename = "puzzle.txt"


def read_input() -> Iterator[List[str]]:
    with open(filename, "r", encoding="utf-8") as file:
        group_lines = []
        for line in file:
            line = line.strip()
            if line:
                group_lines.append(line)
            else:
                yield group_lines
                group_lines = []
    yield group_lines


def calculate_group_intersection(group: List[str]) -> Set[str]:
    answers = [set(answer) for answer in group]
    first_answer, *other_answers = answers
    return first_answer.intersection(*other_answers)


input = list(read_input())

concatenated_groups = [''.join(group) for group in input]

print(sum(len(set(group)) for group in concatenated_groups))

intersections = [calculate_group_intersection(group) for group in input]

print(sum(len(intersection) for intersection in intersections))
