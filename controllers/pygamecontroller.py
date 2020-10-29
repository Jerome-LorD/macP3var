import pygame as pg
from pygame.locals import *
import settings as const

pg.init()
# pg.display.init()
# screen_size = const.SCREEN_SIZE
# screen = pg.display.set_mode(screen_size)


class PYController:
    def __init__(self, labyrinth):
        self.lab = labyrinth

    def handle_control(self):

        for event in pg.event.get():
            if event.type == QUIT:
               return False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    return "left"
                elif event.key == K_UP:
                    return "up"
                elif event.key == K_RIGHT:
                    return "right"
                elif event.key == K_DOWN:
                    return "down"
