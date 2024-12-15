from typing import List
from utils import get_day

puzzle_input = get_day("02", lambda x: x.split(" "))
for i, report in enumerate(puzzle_input):
    puzzle_input[i] = list(map(int, report))


def is_report_safe(report: List[int]) -> bool:
    pairs = list(zip(report, report[1:]))

    return all(0 < abs(y - x) < 4 for x, y in pairs) and (all(x > y for x, y in pairs) or all(x < y for x, y in pairs))


# part 1, total of safe reports
print(sum(is_report_safe(report) for report in puzzle_input))


def add_tolerance(report: List[int]) -> bool:
    return any(is_report_safe(report[:i] + report[i+1:]) for i in range(len(report)))


# part 2, total of safe reports with tolerance
print(sum(add_tolerance(report) for report in puzzle_input))
