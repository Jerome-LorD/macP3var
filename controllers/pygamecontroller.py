import pygame as pg
from pygame.locals import *


class PYController:
    """Handle controls from key events"""

    def __init__(self, labyrinth):
        self.lab = labyrinth
        pg.init()

    def handle_control(self):

        for event in pg.event.get():
            if event.type == QUIT:
                return "q"
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    return "left"
                elif event.key == K_UP:
                    return "up"
                elif event.key == K_RIGHT:
                    return "right"
                elif event.key == K_DOWN:
                    return "down"
