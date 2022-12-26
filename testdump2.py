import pygame

# Set the width and height of the grid cell
cell_size = 32

# Create a 2D array representing the grid
grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

# Create a sprite object
sprite = pygame.sprite.Sprite()
sprite.rect = get_rect()

# Set the position of the sprite
sprite.rect.x = 10
sprite.rect.y = 10

# Snap the sprite to the grid
grid_x = sprite.rect.x // cell_size
grid_y = sprite.rect.y // cell_size

sprite.rect.x = grid_x * cell_size
sprite.rect.y = grid_y * cell_size

# The sprite is now aligned to the grid