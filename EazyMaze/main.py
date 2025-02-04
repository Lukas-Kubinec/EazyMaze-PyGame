"""
@Author: Lukas Kubinec
@Description: A simple little maze game
@Date: 04/02/2025
@Contact: Luko.Kubinec@gmail.com
@File: main.py
"""

import pygame
import ClassPlayer
import ClassWall
import ClassPoint

pygame.init()

# Creation of Window with size and name
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
viewport = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('EazyMaze by Lukas Kubinec')

# Initiate game FPS tick clock
clock = pygame.time.Clock()

# Levels tile maps
tile_size = 64

levels = [
[
    # Level 1
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],

[
    # Level 2
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],

[
    # Level 3
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 2, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],

[
    # Level 4
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 2, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
]

]

# Used to store level number
level_number = 0
# Stores the grid of a current level
tile_grid = levels[level_number]

# Objects list
walls_list = []
player_list = []
points_list = []

# Positions list
wall_positions_list = []
points_positions_list = []

# Player object
player_speed = 64
player_x = 0
player_y = 0
player_score = 0

#Clears lists
def clean_lists():
    walls_list.clear()
    player_list.clear()
    points_list.clear()
    # Positions list
    wall_positions_list.clear()
    points_positions_list.clear()

# Draws the tiles based on the tile map
def initialise_objects():
    for yy in range(len(tile_grid)):
        for xx in range(len(tile_grid[yy])):

            # Creation of fruit
            if tile_grid[yy][xx] == 0:
                point_fruit = ClassPoint.Point(xx * tile_size, yy * tile_size,16, (255, 100, 100), viewport)
                fruit_pos = (xx * tile_size, yy * tile_size)
                # Storing fruits and their positions
                points_list.append(point_fruit)
                points_positions_list.append(fruit_pos)

            # Creation of walls
            if tile_grid[yy][xx] == 1:
                solid_wall = ClassWall.Wall(xx * tile_size, yy * tile_size, tile_size, tile_size, (0, 120, 212), viewport)
                wall_pos = (xx * tile_size, yy * tile_size)
                # Storing walls and their positions
                walls_list.append(solid_wall)
                wall_positions_list.append(wall_pos)

            # Creation of player
            if tile_grid[yy][xx] == 2:
                player_xx = xx * tile_size
                player_yy = yy * tile_size
                player_class = ClassPlayer.Player(player_xx, player_yy, tile_size, tile_size, (0, 0, 0), viewport)
                player_class.draw()
                player_list.append(player_class)


# Runs before the game loop
initialise_objects()

# Assigns objects from the objects list
player = player_list[0]

# Game running loop
game_running = True
while game_running:
    for event in pygame.event.get():
        # BEGIN SECTION
        # Clears the screen every tick
        viewport.fill((255, 255, 255))

        # EVENTS SECTION
        # Checks for any keyboard input
        if event.type == pygame.KEYDOWN:
            # Checks for specific keys are pressed down then checks if the direction player wants to move to is empty
            if event.key == pygame.K_w:
                if (player.x, player.y-player_speed) not in wall_positions_list:
                    player.move_direction(0, -player_speed)
            elif event.key == pygame.K_s:
                if (player.x, player.y + player_speed) not in wall_positions_list:
                    player.move_direction(0, player_speed)
            elif event.key == pygame.K_a:
                if (player.x - player_speed, player.y) not in wall_positions_list:
                    player.move_direction(-player_speed, 0)
            elif event.key == pygame.K_d:
                if (player.x + player_speed, player.y) not in wall_positions_list:
                    player.move_direction(player_speed, 0)

        # Check for score
        if len(points_list) == 0:
            level_number += 1
            tile_grid = levels[level_number]
            clean_lists()
            initialise_objects()

        # Check collisions with points
        if (player.x, player.y) in points_positions_list:
            for i in range(len(points_positions_list)):
                if (player.get_position()) == points_positions_list[i-1]:
                    points_positions_list.pop(i-1)
                    points_list.pop(i - 1)
                    player_score += 1

        # Checks if the window is closed
        if event.type == pygame.QUIT:
            game_running = False

    # DRAW SECTION
    # Draws the player object
    player.draw()

    # Draws the tiles taken from list
    for wall in walls_list:
        ClassWall.Wall.draw(wall)

    for fruit in points_list:
        ClassPoint.Point.draw(fruit)

    # Draws score text
    pygame.display.set_caption('EazyMaze by Lukas Kubinec | Level: ' + str(level_number + 1) + ' | Score: ' + str(player_score))

    # Refreshes display
    #pygame.display.flip()
    pygame.display.flip()

    # Sets the FPS limit to 60
    clock.tick_busy_loop(60)


pygame.quit()