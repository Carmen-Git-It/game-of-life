import pygame
from game_of_life import GameOfLife
from build_grid import build_grid
from math import floor

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
width, height = 850, 900
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
            pygame.draw.rect(screen, BORDER, (i * tile_width, j * tile_height, tile_width, tile_height), 3)
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
"""boop"""

"""
======== VARIABLE INITILIZATION ========
"""
# Loop variables
done = False
clock = pygame.time.Clock()
paused = True

# Grid and Game Setup, pass True to randomly fill
game_grid = build_grid(50, 50, False)
game = GameOfLife(game_grid)

"""
======== GAME LOOP ========
"""
target_x = 0
target_y = 0
while not done:
    """ Game Loop """
    grid = game.get_grid()
    # -50 for interface at bottom
    grid_width, grid_height = grid.get_width(), grid.get_height()
    tile_width, tile_height = round(width / grid_width), round((height - 50) / grid_height)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            target_x = int(floor(pos[0] / tile_width))
            target_y = int(floor(pos[1] / tile_height))
            if grid.get_state(target_x, target_y) % 2 == 0:
                grid.set_cell(1, target_x, target_y)
            else:
                grid.set_cell(2, target_x, target_y)
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            new_x = int(floor(pos[0] / tile_width))
            new_y = int(floor(pos[1] / tile_height))
            if pygame.mouse.get_pressed()[0] and (new_x != target_x or new_y != target_y):
                if grid.get_state(new_x, new_y) % 2 == 0:
                    grid.set_cell(1, new_x, new_y)
                else:
                    grid.set_cell(2, new_x, new_y)
                target_x = new_x
                target_y = new_y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    # Game Logic
    if not paused:
        game_logic()

    # Clear Screen To White
    clear_screen()

    # Drawing Code Here
    draw_grid()

    # Update Screen
    pygame.display.flip()

    # Loop Delay
    clock.tick(15)

pygame.quit()
