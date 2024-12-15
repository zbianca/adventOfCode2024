def get_day(day, mapper=lambda x: x):
    with open(f"resources/day{day}.txt", "r") as f:
        content = f.read().splitlines()
    return list(map(mapper, content))


def get_string(day):
    with open(f"resources/day{day}.txt", "r") as f:
        return f.read()
