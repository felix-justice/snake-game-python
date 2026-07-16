# A Coordinates object represents a row, column pair. That is, it represents
# a specific space on the game board. For example, the top-left space on
# the game board could be represented by a Coordinates object with row=0,
# column=0. The topright could be represented by a Coordinates object with
# row=0, column=9
class Coordinates:
    # This attribute records a row index in the game board. 0 corresponds to
    # the top row in the game board. 9 corresponds to the bottom row.
    row: int
    
    # This attribute records a column index in the game board. 0 corresponds to
    # the leftmost column in the game board. 9 corresponds to the rightmost
    # column.
    column: int

    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
