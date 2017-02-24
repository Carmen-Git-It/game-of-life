class Cell:
    """ A cell for Game of Life, has state either alive or dead."""

    def __init__(self, state):
        """ Initializes the Cell.

        @param Cell self: this Cell
        @param bool state: the state of the cell, False = dead; True = alive
        @rtype: None
        """
        self._state = state

    def __str__(self):
        """ Returns a string representation of the cell.

        @param Cell self: this Cell.
        """
        if self._state == False:
            return "-"
        else:
            return "Q"

    def get_state(self):
        """ Returns the state of this cell.

        @param Cell self: this Cell
        @rtype: bool"""
        return self._state
