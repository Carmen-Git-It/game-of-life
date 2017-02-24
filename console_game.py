from game_of_life import GameOfLife
from grid import Grid
import time

if __name__ == "__main__":
    game_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                 [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                 [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    game_grid = Grid(game_grid, 0, 0)
    game = GameOfLife(game_grid)

    while True:
        game.step()
        print(game)
        time.sleep(0.5)
