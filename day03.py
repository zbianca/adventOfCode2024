import re
from utils import get_string

puzzle_input = get_string("03")
matches = re.findall(r'mul\(\d+,\d+\)', puzzle_input)


def multiply_ints(a_match: str) -> int:
    a, b = map(int, re.search(r'(\d+)\,(\d+)', a_match).group(1, 2))
    return a * b


# part 1, total from multiplications
print(sum(multiply_ints(a_match) for a_match in matches))

matches_and_instructions = re.findall(
    r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', puzzle_input)

total = 0
act = True
for command in matches_and_instructions:
    if command == 'do()':
        act = True
    elif command == "don't()":
        act = False
    elif act:
        total += multiply_ints(command)

# part 2, total from enabled multiplications
print(total)
