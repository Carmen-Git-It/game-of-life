from cell import Cell

DEAD = 1


class Grid:
    """ Stores a 2-dimensional array of Cells either alive or dead."""

    def __init__(self, grid=None, width=10, height=10):
        """ Initializes the grid. If a grid is provided, ignores width and height values.
        Else: Constructs an empty grid with width and height values provided.

        @param int width: the width of width to be generated
        @param List[List[]] grid: the 2-dimensional array storing the grid of cells
        """
        cell_null = Cell(1)
        if grid:
            self._width = len(grid)
            self._height = len(grid[0])
            self._grid = grid
            for i in range(0, self._width):
                for j in range(0, self._height):
                    self._grid[i][j] = Cell(self._grid[i][j])
        else:
            self._width = width
            self._height = height
            self._grid = [cell_null] * width
            for i in range(0, height):
                self._grid[i] = [cell_null] * height

    def get_width(self):
        """ Returns the width of the grid.

        @param Grid self: this Grid
        @rtype: int
        """
        return self._width

    def get_height(self):
        """ Returns the height of the grid.

        @param Grid self: this Grid
        @rtype: int
        """
        return self._height

    def set_cell(self, state, x_index, y_index):
        """ Sets a cell in the grid at x_index, y_index.

        @param Grid self: this Grid
        @param int state: the new state of the cell
        @param int x_index: the width index to insert into
        @param int y_index: the height index to insert into
        """
        self._grid[x_index][y_index] = Cell(state)

    def get_cell(self, x_index, y_index):
        """ Return the cell from the requested indices.

        @param Grid self: this Grid
        @param int x_index: the width index of the cell to get
        @param int y_index: the height index of the cell to get
        @rtype: Cell
        """
        return self._grid[x_index][y_index]

    def get_state(self, x_index, y_index):
        """ Returns the state of the cell in a given index.

        @param GameOfLife self: this GameOfLife
        @param int x_index: the x index of the cell to check
        @param int y_index: the y index of the cell to check
        @rtype: bool
        """
        if 0 <= x_index < self._width and 0 <= y_index < self._height:
            return self._grid[x_index][y_index].get_state()
        else:
            return DEAD
