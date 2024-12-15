from typing import List
from utils import get_day

puzzle_input = get_day("04", lambda str: [c for c in str])
height = range(0, len(puzzle_input))
width = range(0, len(puzzle_input[0]))


DIRECTIONS = [
    (0, 1), (0, -1),   # horizontal
    (1, 0), (-1, 0),   # vertical
    (1, 1), (-1, -1),  # diagonal \
    (1, -1), (-1, 1)   # diagonal /
]


def get_directions(y, x):
    return [
        [
            ([y + dy*1, x + dx*1], 'M'),
            ([y + dy*2, x + dx*2], 'A'),
            ([y + dy*3, x + dx*3], 'S')
        ]
        for dy, dx in DIRECTIONS
    ]


def is_in_bound(combo):
    y, x = combo[0]
    return y in height and x in width


def letter_matches(combo):
    y, x = combo[0]
    letter = combo[1]
    return puzzle_input[y][x] == letter


def sum_xmas():
    return sum(
        1 for y in height
        for x in width
        if puzzle_input[y][x] == 'X'
        for mas in get_directions(y, x)
        if all(is_in_bound(combo) and letter_matches(combo) for combo in mas)
    )


# part 1, total of XMAS
print(sum_xmas())


def get_diagonals(y, x):
    return [
        [
            ([y + dy*1, x + dx*1], 'A'),
            ([y + dy*2, x + dx*2], 'S')
        ]
        for dy, dx in DIRECTIONS[4:]
    ]


def has_second_mas(s, y, x):
    [s_y, s_x] = s
    return (puzzle_input[s_y][x] == 'M' and puzzle_input[y][s_x] == 'S') or (puzzle_input[s_y][x] == 'S' and puzzle_input[y][s_x] == 'M')


def mark_a_done(a):
    [a_y, a_x] = a
    puzzle_input[a_y][a_x] = 'O'


def sum_x_of_mas():
    return sum(
        1 for y in height
        for x in width
        if puzzle_input[y][x] == 'M'
        for mas in get_diagonals(y, x)
        if (all(is_in_bound(combo) and letter_matches(combo) for combo in mas)
            and has_second_mas(mas[1][0], y, x)
            and (mark_a_done(mas[0][0]) or True))
    )


# part 2, total of X-MAS
print(sum_x_of_mas())
