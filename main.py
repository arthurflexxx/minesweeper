from minesweeper import Minesweeper
from board import Board


def play():
    """
    Main function to start and run the Minesweeper game.
    """
    while True:
        # Get user input for rows, columns, and mines
        rows, cols, mines = map(int, input("rows, cols, mines: ").split())
        # Validate input: all values must be positive and mines cannot be equal to the total number of cells
        if all(v > 0 for v in (rows, cols, mines)) and mines != rows * cols:
            break

        print("Print valid values (all > 0) and mines != rows * cols")

    # Create a Minesweeper game instance with the specified parameters
    game: Minesweeper = Minesweeper(Board(rows, cols, mines))

    while True:
        # Clear the console and display remaining bombs
        print("\033[H\033[J", end="")
        print(f"Bombs left: {game.bombs_left}")

        # Check for win condition
        if game.check_win():
            game.game_end(win=True)
            break

        game.board.draw_board()

        # Get user input for the row and column to interact with
        try:
            row, col = map(int, input("row, col: ").split())
            assert 0 <= row < game.board.rows and 0 <= col < game.board.cols
        except (ValueError, AssertionError):
            continue

        if not game.first_move:
            # Check if the player wants to flag a cell
            f = input("Flag (Print anything if you want to put a flag): ")
            if f and (row, col) not in game.visited:
                game.toggle_flag(row, col)
            else:
                if game.check_step_on_mine(row, col):
                    game.game_end()
                    break
                game.reveal(row, col)
        else:
            game.make_first_move(row, col)
            continue


if __name__ == "__main__":
    play()
