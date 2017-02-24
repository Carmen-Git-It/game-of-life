from grid import Grid

class GameOfLife:
    """ A game of life instance."""

    def __init__(self, game_grid):
        """ Initializes a new game of life.

        @param GameOfLife self: this game of life
        @param Grid game_grid: the gameboard
        """
        self._grid = game_grid
        self._width = game_grid.get_width()
        self._height = game_grid.get_height()
        self._steps = 0
        self._generated_cells = 0

    def __str__(self):
        """ Returns a string of the current state of the game_grid.

        @param GameOfLife self: this GameOfLife
        @rtype: str
        """
        string = ""
        for j in range(0, self._height):
            for i in range(0, self._width):
                string += self._grid.get_cell(i, j).__str__() + " "
            string += "\n"
        string += "\n"
        return string

    def _refresh_cell(self, x_index, y_index):
        """ Returns the new state of a Cell based on neighbour cells.

        @param GameOfLife self: this GameOfLife
        @param int x_index: the x index of the cell to check
        @param int y_index: the y index of the cell to check
        @rtype: bool
        """
        left, right, bot, top = x_index - 1, x_index + 1, y_index - 1, y_index + 1
        alive_count = 0
        for i in range(left, right + 1):
            for j in range(bot, top + 1):
                if self._grid.get_state(i, j) and (i != x_index or j != y_index):
                    alive_count += 1
        if alive_count < 2:
            return False
        elif alive_count > 3:
            return False
        elif alive_count == 3:
            self._generated_cells += 1
            return True
        else:
            result = self._grid.get_state(x_index, y_index)
            if result:
                self._generated_cells += 1
            return result

    def step(self):
        """ Takes one step in the Game of Life"""
        new_grid = Grid(None, self._width, self._height)
        for i in range(0, self._width):
            for j in range(0, self._height):
                new_grid.set_cell(self._refresh_cell(i, j), i, j)
        self._grid = new_grid
        self._steps += 1

    def get_steps(self):
        """ Returns the number of steps taken so far.

        @param GameOfLife self: this GameOfLife
        @rtype: int"""
        return self._steps

    def get_grid(self):
        """ Returns the Grid of this GameOfLife

        @param GameOfLife self: this GameOfLife
        @rtype: Grid
        """
        return self._grid

    def cells_generated(self):
        """ Returns the number of cells generated.

        @param GameOfLife self: this GameOfLife
        @rtype: int
        """
        return self._generated_cells
