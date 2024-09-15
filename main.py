from minesweeper_module.minesweeper import Minesweeper


def input_game_size():
    while True:
        # Get user input for rows, columns, and mines
        rows, cols, mines = map(int, input("rows, cols, mines: ").split())
        # Validate input: all values must be positive and mines cannot be equal to the total number of cells
        if all(v > 0 for v in (rows, cols, mines)) and mines != rows * cols:
            break

        print("Print valid values (all > 0) and mines != rows * cols")

    return rows, cols, mines


def input_cell_coord(game: Minesweeper):
    # Get user input for the row and column to interact with
    try:
        row, col = map(int, input("row, col: ").split())
        assert 0 <= row < game.board.rows and 0 <= col < game.board.cols
    except (ValueError, AssertionError):
        print("f")

    f = input("Flag (Print anything if you want to put a flag): ")

    return row, col, f


def play():
    """
    Main function to start and run the Minesweeper game.
    """
    # rows, cols, mines = input_game_size()

    # Create a Minesweeper game instance with the specified parameters
    game: Minesweeper = Minesweeper(5, 5, 1)

    while not game.is_game_over:
        # Clear the console and display remaining bombs
        # print("\033[H\033[J", end="")
        print(f"Bombs left: {game.bombs_left}")
        print(game.count)
        game.board.draw_board()

        row, col, f = input_cell_coord(game)

        game.game_cycle(row, col, f)


if __name__ == "__main__":
    play()
