import time
from collections import deque

from board import Board
from cell import Cell


class Minesweeper:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.bombs_left = board.bombs

        self.first_move = True
        self.is_game_over = False
        self.start_time = time.time()
        self.play_time = 0
        self.visited = set()

    def make_first_move(self, row, col):
        self.board.place_mines(exception_=(row, col))
        self.first_move = False
        self.reveal(row, col)

    def reveal(self, row, col):
        queue = deque()
        queue.append((row, col))

        while queue:
            cur_row, cur_col = queue.popleft()
            cell: Cell = self.board.get_cell(cur_row, cur_col)

            if cell.mines_around:
                cell.cell_reveal()
            else:
                for i in range(cur_row - 1, cur_row + 2):
                    for j in range(cur_col - 1, cur_col + 2):
                        if (
                            0 <= i < self.board.rows
                            and 0 <= j < self.board.cols
                            and (i, j) not in self.visited
                        ):
                            cell.cell_reveal()
                            queue.append((i, j))

            self.visited.add((cur_row, cur_col))

    def toggle_flag(self, row, col):
        if (row, col) not in self.board.flags and self.bombs_left > 0:
            self.board.flags.add((row, col))
            self.bombs_left -= 1
        else:
            self.bombs_left += 1
            self.board.flags.remove((row, col))

    def check_step_on_mine(self, row, col):
        if (row, col) in self.board.mines:
            return True
        return False

    def check_win(self):
        if (
            self.board.flags == self.board.mines and self.board.mines
        ) or self.board.rows * self.board.cols == len(self.visited) + len(
            self.board.mines
        ):
            return True
        return False

    def game_end(self, win=False, win_by_flags=False, show_mines=True):
        self.is_game_over = True
        if not win_by_flags and show_mines:
            self.board.show_mines()

        self.play_time = int(time.time() - self.start_time) // 1
        print(f"Play time: {self.play_time} seconds\n")
        self.board.draw_board()

        if win:
            return "Win"
        return "Lose"
