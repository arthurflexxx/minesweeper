import random

from .cell import Cell


class Board:
    def __init__(self, rows, cols, bombs) -> None:
        """
        Initializes the Minesweeper board.

        Args:
            rows (int): Number of rows on the board. (y coord)
            cols (int): Number of columns on the board. (x coord)
            bombs (int): Number of mines to place on the board.
        """
        self.rows = rows
        self.cols = cols
        self.bombs = bombs

        self.mines = set()
        self.flags = set()

        # Create a 2D list of cells, representing the board
        self.cells = [[Cell(i, j) for j in range(self.cols)] for i in range(self.rows)]

    def get_cell(self, row, col) -> Cell:
        return self.cells[row][col]

    def place_mines(self, exception: tuple | None = None):
        """
        Places mines randomly on the board, avoiding a specified cell.

        Args:
            exception (tuple | None, optional): Tuple representing (row, col) of a cell
                to exclude from mine placement. Defaults to None.
        """
        while len(self.mines) < self.bombs:
            col = random.randint(0, self.cols - 1)
            row = random.randint(0, self.rows - 1)

            if (row, col) != exception:
                self.get_cell(row, col).is_mine = True
                self.mines.add((row, col))

        self.count_mines()

    def count_mines(self):
        """Counts the number of mines around for each cell on the board."""
        for row, col in self.mines:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if (
                        0 <= i < self.rows
                        and 0 <= j < self.cols
                        and (i, j) != (row, col)
                    ):
                        self.get_cell(i, j).mines_around += 1

    def show_mines(self):
        for i, j in self.mines:
            self.get_cell(i, j).reveal()

    def draw_board(self):
        # Calculate the maximum number of digits needed for row numbers
        max_row_digits = len(str(self.rows - 1))

        # Print the column numbers
        print(
            " " * (max_row_digits + 1) + " ".join(f"{i:>{2}}" for i in range(self.cols))
        )

        # Print each row of the board
        for i, _ in enumerate(self.cells):
            # Print the row number
            print(f"{i:>{max_row_digits}} ", end="")
            for cell in _:
                print(cell.get_display(), end="")
            print("")
        print("\n")


if __name__ == "__main__":
    a = Board(9, 19, 6)
    a.place_mines()
    # a.count_mines()
    # a.show_mines()
    # a.reveal_all()
    a.draw_board()
