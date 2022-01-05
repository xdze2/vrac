
from dataclasses import dataclass
from types import new_class
from typing import Dict
from enum import Enum, auto
from pprint import pprint
from collections import defaultdict
from itertools import permutations, islice

import random



class Color(Enum):
    Blue = auto()
    Red = auto()
    Orange = auto()
    White = auto()

    def __repr__(self):
        return self.name



class Dir(Enum):
    Top = auto()
    Bottom = auto()
    Left = auto()
    Right = auto()

    def __repr__(self):
        return self.name


@dataclass
class Card:
    colors: Dict[Dir, Color] =  None 

    @classmethod
    def clockwise(cls, top: Color, right: Color, bottom: Color, left: Color):
        return Card(
            {
                Dir.Top: top,
                Dir.Right: right,
                Dir.Bottom: bottom,
                Dir.Left: left
            }
        )


class Grid:
    """   
    0 1 2
    3 4 5
    6 7 8
    """ 
    pass 


def to_linear_idx(i, j):
    k = i*3 + j
    return k


links = defaultdict(dict)
for i in range(3):
    for j in range(3):
        k = to_linear_idx(i, j)

        if i + 1 < 3:
            links[k][Dir.Bottom] = to_linear_idx(i + 1, j)
        if i - 1 >= 0:
            links[k][Dir.Top] = to_linear_idx(i - 1, j)

        if j + 1 < 3:
            links[k][Dir.Right] = to_linear_idx(i, j + 1)
        if j - 1 >= 0:
            links[k][Dir.Left] = to_linear_idx(i, j - 1)
        

pprint(links)

opposites = {
    Dir.Left: Dir.Right,
    Dir.Right: Dir.Left,
    Dir.Bottom: Dir.Top,
    Dir.Top: Dir.Bottom,
}

colors = [Color.Red, Color.Blue, Color.White, Color.Orange]
cards_deck = [
    Card.clockwise(*u)
    for u in 
    islice(
        permutations(colors, 4),
        9
    )
]

print(cards_deck)




def is_link_valid(grid, k_a, direction_a, k_b, direction_b):
    color_a = grid[k_a].colors.get(direction_a)
    color_b = grid[k_b].colors.get(direction_b)
    return color_a == color_b


link_list = [
    (k_a, d_a, k_b, opposites[d_a])
    for k_a, neigh in links.items()
    for d_a, k_b in neigh.items()
]

print(link_list)

def is_grid_valid(grid: Grid) -> bool:
    return all(
        is_link_valid(grid, k_a, d_a, k_b, d_b)
        for k_a, d_a, k_b, d_b in link_list
    )



print('---')
n = 0
for a_grid in permutations(cards_deck, 9):

    n += 1
    if n % 1000 == 0:
        print(n)

    if is_grid_valid(a_grid):
        print("a solution")
        print(a_grid)
        break


