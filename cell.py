from enum import Enum
from dataclasses import dataclass


class CellStates(Enum):
    """Represents the different states of a cell."""

    CLOSED = "[■]"
    REVEALED = "[ ]"
    FLAGGED = "[F]"
    MINE = "[*]"
    MINES_AROUND = "[{mines}]"


@dataclass()
class Cell:
    row: int  # y coord
    col: int  # x coord

    mines_around: int = 0
    is_revealed: bool = False
    is_flagged: bool = False
    is_mine: bool = False

    status: CellStates = CellStates.CLOSED.value

    def get_display(self):
        """Returns the string representation of the cell for display purposes."""
        if self.is_revealed or self.is_flagged:
            return self.status
        return CellStates.CLOSED.value

    def toggle_flag(self):
        self.is_flagged = not self.is_flagged
        self.status = CellStates.FLAGGED.value if self.is_flagged else CellStates.CLOSED.value

    def reveal(self):
        """Reveals the cell and updates its status based on its contents."""
        self.is_revealed = True

        if self.is_mine:
            self.status = CellStates.MINE.value
        elif self.mines_around:
            self.status = CellStates.MINES_AROUND.value.format(mines=self.mines_around)
        else:
            self.status = CellStates.REVEALED.value
