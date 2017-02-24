DEAD = 1

class Cell:
    """ A cell for Game of Life, has state either alive or dead."""

    def __init__(self, state):
        """ Initializes the Cell.

        @param Cell self: this Cell
        @param int state: the state of the cell, 1 = DEAD; 2 = ALIVE; 3 = DEAD; 4 = ALIVE; etc.
        @rtype: None
        """
        self._state = state

    def __str__(self):
        """ Returns a string representation of the cell.

        @param Cell self: this Cell.
        """
        if self._state < 2:
            return "-"
        else:
            return "Q"

    def get_state(self):
        """ Returns the state of this cell.

        @param Cell self: this Cell
        @rtype: int"""
        return self._state
