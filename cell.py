from enum import Enum
from dataclasses import dataclass


class CellStatus(Enum):
    CLOSED = "[■]"
    REVEALED = "[ ]"
    FLAGGED = "[F]"
    MINE = "[*]"
    MINES_AROUND = "[{mines}]"


@dataclass()
class Cell:
    row: int
    col: int

    mines_around: int = 0
    is_revealed: bool = False
    is_mine: bool = False
    status: CellStatus = CellStatus.CLOSED.value

    def get_display(self):
        if self.is_revealed:
            return self.status

        return CellStatus.CLOSED.value

    def cell_reveal(self):
        self.is_revealed = True

        if self.is_mine:
            self.status = CellStatus.MINE.value
        elif self.mines_around:
            self.status = CellStatus.MINES_AROUND.value.format(mines=self.mines_around)
        else:
            self.status = CellStatus.REVEALED.value
