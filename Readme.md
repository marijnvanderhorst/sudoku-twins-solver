# Sudoku Twins Solver
Recursive solver in Python with backtracking to solve the following Sudoku Twins puzzle that was included with the 
Dutch newspaper _De Volkskrant_ on Friday 13 October.

In such a Sudoku Twin, the center 3 columns are shared by both the left and right twin. Solving the puzzle then comes
down to solving the two 9x9 sudoku's individually as normal, as long as we ensure the center 3 columns have the same
values in the left and right "twins".

```text
┌───┬───┬───┰───┬───┬───╔═══╦═══╦═══╗───┬───┬───┰───┬───┬───┐
│   ┊ 8 ┊   ┃   ┊ 1 ┊   ║   ┊   ┊   ║   ┊   ┊   ┃ 2 ┊ 5 ┊   │
│ 5 ┊   ┊   ┃ 9 ┊   ┊   ║ 4 ┊   ┊   ║   ┊ 1 ┊   ┃   ┊   ┊   │
│ 6 ┊   ┊ 2 ┃ 3 ┊   ┊   ║   ┊   ┊   ║ 2 ┊   ┊   ┃   ┊   ┊ 6 │
├━━━┊━━━┊━━━╂━━━┊━━━┊━━━║━━━┊━━━┊━━━║━━━┊━━━┊━━━╂━━━┊━━━┊━━━┤
│ 8 ┊ 2 ┊   ┃   ┊   ┊ 6 ║   ┊   ┊ 9 ║   ┊   ┊   ┃   ┊   ┊   │
│   ┊   ┊   ┃   ┊ 2 ┊ 1 ║ 3 ┊   ┊ 6 ║ 4 ┊ 5 ┊   ┃   ┊   ┊   │
│   ┊   ┊   ┃   ┊   ┊   ║ 8 ┊   ┊   ║ 9 ┊   ┊   ┃   ┊ 1 ┊ 3 │
├━━━┊━━━┊━━━╂━━━┊━━━┊━━━║━━━┊━━━┊━━━║━━━┊━━━┊━━━╂━━━┊━━━┊━━━┤
│ 7 ┊   ┊   ┃   ┊   ┊ 3 ║   ┊   ┊   ║   ┊   ┊ 3 ┃ 8 ┊   ┊ 2 │
│   ┊   ┊   ┃   ┊ 7 ┊   ║   ┊   ┊ 3 ║   ┊   ┊ 5 ┃   ┊   ┊ 4 │
│   ┊ 6 ┊ 3 ┃   ┊   ┊   ║   ┊   ┊   ║   ┊ 4 ┊   ┃   ┊ 3 ┊   │
└───┴───┴───┸───┴───┴───╚═══╩═══╩═══╝───┴───┴───┸───┴───┴───┘

```

## Prerequisites
Just Python 3

## Execute
```bash
python3 main.py
```

