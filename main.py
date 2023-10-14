from typing import List

# Sudoku twin as printed in De Volkskrant of Friday 13 October.
sudoku = [
    [None, 8, None, None, 1, None, None, None, None, None, None, None, 2, 5, None],
    [5, None, None, 9, None, None, 4, None, None, None, 1, None, None, None, None],
    [6, None, 2, 3, None, None, None, None, None, 2, None, None, None, None, 6],
    [8, 2, None, None, None, 6, None, None, 9, None, None, None, None, None, None],
    [None, None, None, None, 2, 1, 3, None, 6, 4, 5, None, None, None, None],
    [None, None, None, None, None, None, 8, None, None, 9, None, None, None, 1, 3],
    [7, None, None, None, None, 3, None, None, None, None, None, 3, 8, None, 2],
    [None, None, None, None, 7, None, None, None, 3, None, None, 5, None, None, 4],
    [None, 6, 3, None, None, None, None, None, None, None, 4, None, None, 3, None],
]


def to_strings(start=0, width=15, delim=' | ', line_start='| ', line_end=" |") -> List[str]:
    """
    Format the current state of the sudoku to a list of strings, one for each row in the sudoku.
    :param start: Index of the most-left column that will be included in the output.
    :param width: Index of the most-right column that will be included in the output.
    :param delim: Character(s) to insert in-between each cell value.
    :param line_start: Character(s) to print at the start of each line/row.
    :param line_end: Character(s) to print at the end of each line/row.
    :return:
    """
    rows = []

    for y in range(9):
        vals = [sudoku[y][x + start] for x in range(width)]
        strs = [str(val) if val is not None else '-' for val in vals]
        row = delim.join(strs)

        rows.append(line_start + row + line_end)

    return rows


def ps(start=0, width=15, delim=' | ', line_start='| ', line_end=" |") -> None:
    """
    Print sudoku to stdout. For arguments, see :func:`to_strings`
    """
    for row in to_strings(start, width, delim, line_start, line_end):
        print(row)


def contains_in_row(x, y, val) -> bool:
    in_left = val in [sudoku[y][i] for i in range(9)]
    in_right = val in [sudoku[y][i + 6] for i in range(9)]

    if x < 6:
        return in_left
    elif x > 8:
        return in_right
    else:
        return in_left or in_right


def contains_in_col(x, val) -> bool:
    col = [sudoku[y][x] for y in range(9)]

    return val in col


def contains_in_block(x, y, val) -> bool:
    x0 = int(x / 3) * 3
    y0 = int(y / 3) * 3
    box = []
    for i in range(3):
        for j in range(3):
            box.append(sudoku[y0 + j][x0 + i])

    return val in box


def is_allowed(x, y, val) -> bool:
    return not contains_in_row(x, y, val) and not contains_in_col(x, val) and not contains_in_block(x, y, val)


def solve() -> bool:
    """Recursively solve the twin-sudoku by assigning a number one by one to empty cells. After assigning a number,
    we check whether it causes any conflicts/faults in the sudoku values (rows, columns, blocks).
    When these checks pass, recursively check whether this assignment leads to a solution or not.
    """
    for y in range(9):
        for x in range(15):
            if sudoku[y][x] is not None:
                continue

            for i in range(9):
                val = i + 1

                if not is_allowed(x, y, val):
                    continue

                sudoku[y][x] = val

                if solve():
                    return True
                else:
                    sudoku[y][x] = None
            return False
    return True


def main():
    print("Input sudoku twin:")
    ps(0, 15)

    print("Solving...")
    if not solve():
        print("No solution")

    print("Found solution :)")
    print("Left sudoku:")
    ps(0, 9)
    print("Right sudoku:")
    ps(6, 9)
    print("Combined:")
    ps()

    print("Writing to solution.csv...")
    with open('solution.csv', 'w') as solution:
        for row in to_strings(0, 15, ',', '', ''):
            solution.write(row + '\n')


if __name__ == '__main__':
    main()
