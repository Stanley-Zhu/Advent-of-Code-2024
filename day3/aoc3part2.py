import re


def aoc3part2() -> None:
    total = 0
    enabled = True
    with open("input.txt", "r") as puzzle_input:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))", puzzle_input.read())
        for match in matches:
            # print(matches)

            # matched do(); enable mul instruction
            if match[3] == "do()":
                enabled = True
            # matched don't(); disable mul instruction
            elif match[2] == "don't()":
                enabled = False
            # perform mul instruction based on enabled flag
            else:
                if enabled:
                    total += int(match[0]) * int(match[1])

    puzzle_input.close()
    print(total)


if __name__ == '__main__':
    aoc3part2()
