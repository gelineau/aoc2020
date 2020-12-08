from dataclasses import dataclass
from typing import List, Tuple
from parse import compile
import networkx

filename = "puzzle.txt"


def read_input() -> List[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


@dataclass
class Constraint:
    container_color: str
    contained_colors: List[Tuple[int, str]]


def get_number_and_color(part: str) -> Tuple[int, str]:
    if part.endswith("bags"):
        part = part[:-1]

    parsing_template = compile(
        "{number:d} {color} bag")

    # print(part)
    parsed_line = parsing_template.parse(part).named
    return parsed_line["number"], parsed_line["color"]


def decode_line(line: str) -> Constraint:
    # print(line)
    container_color, contained_part = line.rstrip(".\n").split(" bags contain ")

    if contained_part == "no other bags":
        contained_colors = []
    else:
        parts = contained_part.split(", ")
        contained_colors = [get_number_and_color(part) for part in parts]

    return Constraint(container_color, contained_colors)


input = read_input()

constraints = [decode_line(line) for line in input]

graph = networkx.DiGraph()

for constraint in constraints:
    graph.add_node(constraint.container_color)
    for number, contained_color in constraint.contained_colors:
        graph.add_node(contained_color)
        graph.add_edge(constraint.container_color, contained_color,
                       count=number)

origin = 'shiny gold'
ancestors = len(
    networkx.dfs_tree(graph.reverse(), source=origin).reverse().nodes)
print(ancestors - 1)  # shiny gold is included in ancestors


def count_bags(origin: str, graph) -> int:
    contained_bags = graph.out_edges(origin)
    count = 1
    for _, contained_bag in contained_bags:
        count += graph[origin][contained_bag]['count'] * count_bags(
            contained_bag, graph)

    return count


print(count_bags(origin, graph) - 1)  # shiny gold bag is included in count_bags
