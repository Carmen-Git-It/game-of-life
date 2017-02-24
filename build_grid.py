from grid import Grid
from math import floor
import random
def build_grid(width, height):
    """ Builds a grid of 0s and 1s for game of life

    @param int width: width of the grid
    @param int height: height of the grid
    @rtype: Grid
    """
    new_grid = Grid(None, width, height)
    alive_max = width * height / 5
    alive_count = 0
    count = 0
    while True:
        if alive_count > alive_max:
            break
        if count > width * height * 10:
            break
        if random.random() >= 0.8:
            x = floor(random.random() * width)
            y = floor(random.random() * height)
            if not new_grid.get_state(x, y):
                new_grid.set_cell(True, x, y)
                alive_count += 1
        count += 1
    return new_grid


