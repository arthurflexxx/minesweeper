import time
from collections import deque

from board import Board
from cell import Cell


class Minesweeper:
    def __init__(self, board: Board) -> None:
        """Initializes the Minesweeper game with a given board."""
        self.board = board
        self.bombs_left = board.bombs

        self.first_move = True
        self.is_game_over = False
        self.start_time = time.time()  # Start time of the game
        self.play_time = 0  # Game duration
        self.visited = set()  # Set to keep track of revealed cells

    def make_first_move(self, row, col):
        """
        Handles the first move of the game. Places mines and reveals the starting cell.
        """
        self.board.place_mines(exception=(row, col))
        self.first_move = False
        self.reveal(row, col)

    def reveal(self, row, col):
        """
        Reveals a cell and its adjacent empty cells using the breadth-first search (bfs) algorithm.
        """
        queue = deque()
        queue.append((row, col))

        while queue:
            cur_row, cur_col = queue.popleft()
            cell: Cell = self.board.get_cell(cur_row, cur_col)

            if cell.mines_around:  # If the cell has adjacent mines, just reveal it
                cell.reveal()
            else:
                # If the cell is empty, reveal it and add its neighbors to the queue
                for i in range(cur_row - 1, cur_row + 2):
                    for j in range(cur_col - 1, cur_col + 2):
                        if (
                            0 <= i < self.board.rows
                            and 0 <= j < self.board.cols
                            and (i, j) not in self.visited
                        ):
                            cell.reveal()
                            queue.append((i, j))

            self.visited.add((cur_row, cur_col))

    def toggle_flag(self, row, col):
        if (row, col) not in self.board.flags and self.bombs_left > 0:
            # Add a flag if it's not already flagged and there are bombs left
            self.board.flags.add((row, col))
            self.bombs_left -= 1
        else:
            # Remove the flag if it's already flagged
            self.bombs_left += 1
            self.board.flags.remove((row, col))

    def check_step_on_mine(self, row, col):
        return (row, col) in self.board.mines  # Return True if the cell is a mine

    def check_win(self):
        return (
            self.board.flags == self.board.mines and self.board.mines
        ) or self.board.rows * self.board.cols == len(self.visited) + len(
            self.board.mines
        )  # Return True if all mines are flagged or all non-mine cells are revealed

    def game_end(self, win=False, win_by_flags=False, show_mines=True):
        """
        Ends the game, displaying the results and the board.
        """
        print("\033[H\033[J", end="")  # Clear the console
        self.is_game_over = True

        # Show mines if the player lost or won but not by flagging all mines
        if not win_by_flags and show_mines:
            self.board.show_mines()

        self.play_time = int(time.time() - self.start_time) // 1  # Calculate play time
        print("Win" if win else "Lose")
        print(f"Play time: {self.play_time} seconds\n")
        self.board.draw_board()

        return "Win" if win else "Lose"
