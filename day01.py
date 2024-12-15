from utils import get_day
from collections import Counter

puzzle_input = get_day("01", str.split)
left_list = sorted(int(x[0]) for x in puzzle_input)
right_list = sorted(int(x[1]) for x in puzzle_input)

# part 1, total distance
print(sum(abs(left - right) for left, right in zip(left_list, right_list)))

counter = Counter(right_list)

# part 2, similarity score
print(sum(num * counter[num] for num in left_list))
