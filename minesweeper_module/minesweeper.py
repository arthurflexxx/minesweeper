import time
from collections import deque

from .board import Board, Cell


class Minesweeper:
    def __init__(self, rows, cols, mines) -> None:
        """Initializes the Minesweeper game with a given board."""
        self.board = Board(rows, cols, mines)
        self.bombs_left = mines

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
                self.visited.add((cur_row, cur_col))
            else:
                # If the cell is empty, reveal it and add its neighbors to the queue
                for i in range(cur_row - 1, cur_row + 2):
                    for j in range(cur_col - 1, cur_col + 2):
                        if (
                            0 <= i < self.board.rows
                            and 0 <= j < self.board.cols
                            and (i, j) not in self.visited
                        ):
                            self.board.get_cell(i, j).reveal()
                            self.visited.add((i, j))
                            queue.append((i, j))

    def game_cycle(self, row, col, put_flag=False):
        """
        Handles a single game cycle, processing player's move and updating game state.

        Args:
            row (int): y coord
            col (int): x coord
            put_flag (bool, optional): Whether to place a flag on the cell. Defaults to False.

        Returns:
            None. Updates the game state directly.
        """
        if self.first_move:
            self.make_first_move(row, col)
            return self.check_win()

        if put_flag:
            self.toggle_flag(row, col)
        else:
            if self.check_step_on_mine(row, col):
                return self.game_end()
            self.reveal(row, col)

        return self.check_win()

    def toggle_flag(self, row, col):
        self.board.get_cell(row, col).toggle_flag()
        if (row, col) not in self.board.flags and self.bombs_left > 0:
            # Add a flag if it's not already flagged and there are bombs left
            self.board.flags.add((row, col))
            self.bombs_left -= 1
        else:
            # Remove the flag if it's already flagged
            self.board.flags.remove((row, col))
            self.bombs_left += 1

    def check_step_on_mine(self, row, col):
        return (row, col) in self.board.mines  # Return True if the cell is a mine

    def check_win(self):
        if self.board.flags == self.board.mines and self.board.mines:
            return self.game_end(win=True, win_by_flags=True)
        elif self.board.rows * self.board.cols == len(self.visited) + len(
            self.board.mines
        ):
            return self.game_end(win=True)

    def show_end_game_stats(self, game_status):
        # print("\033[H\033[J", end="")  # Clear the console
        print(game_status)
        print(f"Play time: {self.play_time} seconds\n")
        self.board.draw_board()

    def game_end(self, win=False, win_by_flags=False):
        """
        Ends the game, displaying the results and the board.
        """
        self.is_game_over = True
        self.play_time = int(time.time() - self.start_time) // 1  # Calculate play time

        # Show mines if the player lost or won but not by flagging all mines
        if not win_by_flags:
            self.board.show_mines()

        return "Win" if win else "Lose"
