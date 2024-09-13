from minesweeper import Minesweeper
from board import Board


def play():
    while True:
        rows, cols, mines = map(int, input("rows, cols, mines: ").split())

        if all(v > 0 for v in (rows, cols, mines)) and mines != rows * cols:
            break

        print("Print valid values (all > 0) and mines != rows * cols")

    game: Minesweeper = Minesweeper(Board(rows, cols, mines))
    while not game.is_game_over:
        print("\033[H\033[J", end="")
        print(f"Bombs left: {game.bombs_left}")

        if game.check_win():
            game.game_end(win=True)
            break

        game.board.draw_board()

        try:
            row, col = map(int, input("row, col: ").split())
            assert 0 <= row < game.board.rows and 0 <= col < game.board.cols
        except (ValueError, AssertionError):
            continue

        if game.first_move:
            game.make_first_move(row, col)
            continue

        f = input("Flag (Print anything if you want to put a flag): ")
        if f and (row, col) not in game.visited:
            game.toggle_flag(row, col)
        else:
            if game.check_step_on_mine(row, col):
                game.game_end()
                break
            game.reveal(row, col)


if __name__ == "__main__":
    play()
