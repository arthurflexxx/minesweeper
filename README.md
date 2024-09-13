# Simple Python implementation of the Minesweeper game.

To start a game you need to run the main.py
```
python main.py
```
_____

+ At the start of the game, enter the desired rows, columns, and mines.
+ **Optional:** To fix the game size, remove the while loop in `main.py` and set the desired size directly in the Minesweeper constructor `game: Minesweeper = Minesweeper(Board(rows, cols, mines))`.
```python
def play():
    while True:
        rows, cols, mines = map(int, input("rows, cols, mines: ").split())

        if all(v > 0 for v in (rows, cols, mines)) and mines != rows * cols:
            break

        print("Print valid values (all > 0) and mines != rows * cols")

    game: Minesweeper = Minesweeper(Board(rows, cols, mines))
```

The game field looks like this

![3Gs99WftHDA](https://github.com/user-attachments/assets/c5f29fb5-a6fa-4f50-bb6e-4ab1f851fac6)

When you open a cell

![image](https://github.com/user-attachments/assets/15c54074-2b50-4284-9466-856c0565ccca)

You also can put a flag on any cell

![image](https://github.com/user-attachments/assets/971ec8be-e0b3-4e50-818a-0fadc2de73ae)


You can customize the appearance of the game cells by modifying the `CellStatus` enum in `cell.py`:
```python
class CellStatus(Enum):
    CLOSED = "[■]"
    REVEALED = "[ ]"
    FLAGGED = "[F]"
    MINE = "[*]"
    MINES_AROUND = "[{mines}]"
```
______
The example of integrating Minesweeper logic in a project is in `main.py`
