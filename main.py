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
    while True:
        # Get user input for the row and column of the cell to interact with
        row, col = map(int, input("row, col: ").split())
        if 0 <= row < game.board.rows and 0 <= col < game.board.cols:
            f = input("Flag (Print anything if you want to put a flag): ")
            break
    return row, col, f


def play():
    """
    Main function to start and run the Minesweeper game.
    """
    rows, cols, mines = input_game_size()

    # Create a Minesweeper game instance with the specified parameters
    game: Minesweeper = Minesweeper(rows, cols, mines)

    while not game.is_game_over:
        # Clear the console and display remaining bombs
        print("\033[H\033[J", end="")
        print(f"Bombs left: {game.bombs_left}")
        game.board.draw_board()

        row, col, f = input_cell_coord(game)
        a = game.game_cycle(row, col, f)
        game.show_end_game_stats(a)


if __name__ == "__main__":
    play()
