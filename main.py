import numpy as np

# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 720

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

GRID_WIDTH, GRID_HEIGHT = 30, 30
CELL_WIDTH, CELL_HEIGHT = SCREEN_WIDTH // GRID_WIDTH, SCREEN_HEIGHT // GRID_HEIGHT
BG_COLOR = (190, 230, 130)
LINE_COLOR = (90, 210, 160)

ROBOT_ICON =  pygame.transform.scale( pygame.image.load("./assets/robot.png"), (CELL_WIDTH, CELL_HEIGHT))
APPLE_ICON = pygame.image.load("./assets/apple.png")

player_coords = pygame.Vector2(random.randint(0, GRID_WIDTH), random.randint(0, GRID_HEIGHT))
PRESSED_KEY = ''
LAST_EXECUTED_TICK = 0

def draw_grid():
    """Draw a grid on the screen"""
    # Draw vertical lines
    for x in range(0, SCREEN_WIDTH, CELL_HEIGHT):
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))

    # Draw horizontal lines
    for y in range(0, SCREEN_HEIGHT, CELL_WIDTH):
        pygame.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))

def execute_step(pressed_key=None):
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BG_COLOR)

    draw_grid()

    player_pos = pygame.Vector2(player_coords.x * CELL_WIDTH, player_coords.y * CELL_HEIGHT)
    pygame.Surface.blit(screen, ROBOT_ICON, player_pos)
    if pressed_key == 'w':
        player_coords.y -= 1
    if pressed_key == 's':
        player_coords.y += 1
    if pressed_key == 'a':
        player_coords.x -= 1
    if pressed_key == 'd':
        player_coords.x += 1


    pygame.display.update()

execute_step()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_tick = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        PRESSED_KEY = 'w'
    if keys[pygame.K_s]:
        PRESSED_KEY = 's'
    if keys[pygame.K_a]:
        PRESSED_KEY = 'a'
    if keys[pygame.K_d]:
        PRESSED_KEY = 'd'

    if current_tick % 1000 == 0 and current_tick != LAST_EXECUTED_TICK:
        execute_step(PRESSED_KEY)
        PRESSED_KEY = ''
        LAST_EXECUTED_TICK = current_tick

pygame.quit()


