# Simple Python implementation of the Minesweeper game.

+ At the start of the game, enter the desired rows, columns, and mines.
+ **Optional:** To fix the game size, set the desired size directly in the Minesweeper constructor `game: Minesweeper = Minesweeper(rows, cols, mines)`.
```python
def play():
    """
    Main function to start and run the Minesweeper game.
    """
    rows, cols, mines = input_game_size()

    # Create a Minesweeper game instance with the specified parameters
    game: Minesweeper = Minesweeper(rows, cols, mines)
```
_____
The game field looks like this

![3Gs99WftHDA](https://github.com/user-attachments/assets/c5f29fb5-a6fa-4f50-bb6e-4ab1f851fac6)

When you reveal a cell

![image](https://github.com/user-attachments/assets/15c54074-2b50-4284-9466-856c0565ccca)

You also can put a flag on any cell

![image](https://github.com/user-attachments/assets/971ec8be-e0b3-4e50-818a-0fadc2de73ae)

_____
You can customize the appearance of the game cells by modifying the `CellStatus` enum in `cell.py`:
```python
class CellStatus(Enum):
    CLOSED = "[■]"
    REVEALED = "[ ]"
    FLAGGED = "[F]"
    MINE = "[*]"
    MINES_AROUND = "[{mines}]"
```

