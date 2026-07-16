from typing import Optional
from coordinates import Coordinates

class Snake:
    # TODO Create attributes here. ALL ATTRIBUTES MUST BE PRIVATE.
    
         
    def __init__(self) -> None:
        # TODO Initialize the snake's attributes to record that its
        # current location is the starting location: the topleft of the
        # game board, facing to the right.
        """OIntiliaze the snake's attributes to recod that its currebnt location
        aka the top left of the game board, facing the right"""
        # private attributes

        self._segments: list[Coordinates] =  [
                Coordinates(0, 0),
                Coordinates(0, 1),
                Coordinates(0, 2),
                Coordinates(0, 3),

        ]
        # initliaze facing direction
        
        self._direction: str = "right" 

        # keep the previous tail location
        self._previous_tail: Coordinates = self._segments[0]

    def get_coordinates_list(self) -> list[Coordinates]:
        # TODO Return a list of coordinates. Each coordinates object in the list
        # should represent the location of one of the snake's segments. (Hint:
        # if your Snake class already has an attribute for this exact purpose,
        # then simply return the attribute).
        # (See coordinates.py for the definition of the Coordinates POD type)

        return list(self._segments)

    # TODO Create other methods here (you WILL need some other methods to
    # accomplish all the objectives of the assignment).
    
    def move(self) -> None:
        """ move the snake one step in the current direction. index 0 is the 
        tail is the head, and tail is at the end"""

        head = self._segments[-1]

        # save previous tail location beofre it moves
        self.previous_tail = self._segments[0]
        # compute the new head location (wrap on a 10x10 board)
        if self._direction == "up":
            new_head = Coordinates((head.row - 1) % 10, head.column)
        elif self._direction == "down":
            new_head = Coordinates((head.row + 1) % 10, head.column)
        elif self._direction == "left":
            new_head = Coordinates(head.row, (head.column - 1) % 10)
        else: # right
            new_head = Coordinates(head.row, (head.column + 1) % 10)

        # insert new head at start of list and remove the tail (aka last segment)
        self._segments.append(new_head)

        # remove the last segmeent 
        self._segments.pop(0)
    
    def grow(self) -> None:
        # makes the snake grow longer by adding a new segment at the tail
        # the new segement should be wherte the tail used to be prior
        tail = self._previous_tail
        self._segments.insert(0, Coordinates(tail.row, tail.column))

    def set_direction(self, new_direction: str) -> None:
        """ CXhange the diorection of the snake, and prevent reversing directly
        into itself"""
        nd = new_direction.lower()
        opposite = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left"
        }
            
        # only update if not reversing
        if nd in opposite and nd != opposite[self._direction]:
            self._direction = nd

    def get_head(self) -> Coordinates:
        # return the coordinates of the snakes head
        return self._segments[-1]

    def check_self_collision(self) -> bool:
        # return true if the snakes head collides with the body
        head = self.get_head()
        for segment in self._segments[:-1]:
            if segment.row == head.row and segment.column == head.column:
                return True

        return False
      



