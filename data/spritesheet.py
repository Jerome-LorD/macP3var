import os
import pygame
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0]
sprites_dir = os.path.join(main_dir, "ressource")
pygame.init()

class Spritesheet:
    def __init__(self, filename):
        img = os.path.join(sprites_dir, filename)
        try:
            self.sheet = pygame.image.load(img)#.convert_alpha()
        except:
            raise SystemExit(f"Unable to load spritesheet image: {filename}")
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)