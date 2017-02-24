import pygame
from game_of_life import GameOfLife
from build_grid import build_grid

"""
======== CONSTANTS ========
"""
BORDER = (0, 0, 0)  # black
BACKGROUND = (255, 255, 255)  # white
ALIVE = (17, 17, 109)  # ALIVE1
ALIVE2 = (38, 38, 162)  # ALIVE2
ALIVE3 = (93, 93, 216)  # ALIVE3
ALIVE4 = (130, 130, 235)  # ALIVE4
DEAD = (22, 136, 22)  # DEAD1
DEAD2 = (47, 203, 47)  # DEAD2
DEAD3 = (110, 255, 110)  # DEAD3
DEAD4 = (142, 255, 142)  # DEAD4


"""
======== PYGAME SETUP ========
"""
pygame.init()
width, height = 700, 750
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")
myfont = pygame.font.SysFont("monospace", 20)


"""
======== FUNCTIONS ========
"""


def draw_grid():
    """ Draws the grid."""
    for i in range(0, grid_width):
        for j in range(0, grid_height):
            if grid.get_state(i, j) == 1:  # First Dead Colour
                pygame.draw.rect(screen, DEAD, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            elif grid.get_state(i, j) == 2:  # First Alive Colour
                pygame.draw.rect(screen, ALIVE, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            elif grid.get_state(i, j) == 3:  # Second Dead Colour
                pygame.draw.rect(screen, DEAD2, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            elif grid.get_state(i, j) == 4:  # First Alive Colour
                pygame.draw.rect(screen, ALIVE2, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            elif grid.get_state(i, j) == 5:  # First Alive Colour
                pygame.draw.rect(screen, DEAD3, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            elif grid.get_state(i, j) == 6:  # First Alive Colour
                pygame.draw.rect(screen, ALIVE3, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            elif grid.get_state(i, j) % 2 == 0:  # Last Alive Colour
                pygame.draw.rect(screen, ALIVE4, (i * tile_width, j * tile_height, tile_width, tile_height), 0)
            else:  # Last Dead Colour
                pygame.draw.rect(screen, DEAD4, (i * tile_width, j * tile_height, tile_width, tile_height), 0)

    # Draw Labels
    label = myfont.render("{} generations have passed".format(game.get_steps()), 1, BORDER)
    screen.blit(label, (14 * width / 21, height - 25))

    label2 = myfont.render("{} cells have been generated".format(game.cells_generated()), 1, BORDER)
    screen.blit(label2, (1 * width / 21, height - 25))


def clear_screen():
    """ Clears the screen to the background colour."""
    screen.fill(BACKGROUND)


def game_logic():
    """ The game logic step."""
    game.step()


"""
======== VARIABLE INITILIZATION ========
"""
# Loop variables
done = False
clock = pygame.time.Clock()

# Grid and Game Setup
game_grid = build_grid(70, 70)
game = GameOfLife(game_grid)

"""
======== GAME LOOP ========
"""

while not done:
    """ Game Loop """
    grid = game.get_grid()
    # -50 for interface at bottom
    grid_width, grid_height = grid.get_width(), grid.get_height()
    tile_width, tile_height = round(width / grid_width), round((height - 50)/ grid_height)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game Logic
    game_logic()

    # Clear Screen To White
    clear_screen()

    # Drawing Code Here
    draw_grid()

    # Update Screen
    pygame.display.flip()

    # Loop Delay
    clock.tick(30)

pygame.quit()
