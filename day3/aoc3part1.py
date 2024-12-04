import re


def aoc3part1() -> None:
    total = 0
    with open("input.txt", "r") as puzzle_input:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", puzzle_input.read())
        for (m1, m2) in matches:
            total += int(m1) * int(m2)
    puzzle_input.close()
    print(total)


if __name__ == '__main__':
    aoc3part1()
