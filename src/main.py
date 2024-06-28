import pygame

# In-Project Imports
from misc.constants import *
from misc.utils import *

from grid import Grid


pygame.init()
screen: pygame.Surface = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Code a Week #1: Grid & Nearest Neighbours")

# The clock used by the Application
clock = pygame.time.Clock()
running = True

# Adjust Grid Parameters Here
grid = Grid(screen, 8)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        grid.handle_event(event)

    pos = pygame.mouse.get_pos()
    grid.update(pos)
    
    screen.fill(GRAY10)
    grid.render()
    pygame.display.flip()
    
    clock.tick(60)
    
    
pygame.quit()