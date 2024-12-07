def find_xmas() -> int:
    xmas_count = 0
    check = "XMAS"
    with open("input.txt", "r") as xmas_string:
        xmas_array = xmas_string.read().split("\n")
        to_visit = []
        visited = []
        max_row, max_col = len(xmas_array), len(xmas_array[0])
        for row in range(max_row):
            for col in range(max_col):
                curr = xmas_array[row][col]
                if (row, col) not in visited:
                    visited.append((row, col))

    return xmas_count


if __name__ == '__main__':
    find_xmas()
