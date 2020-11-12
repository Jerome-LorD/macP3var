"""Pygamecontroller module transmits commands to the player module."""
import pygame
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP

from settings import QUIT_APP, LEFT, UP, RIGHT, DOWN


class PYController:
    """Handle controls from keyboard events."""

    def handle_control(self):
        """Handle control from directional arrow on keyboard."""
        for event in pygame.event.get():
            if event.type == QUIT:
                return QUIT_APP
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    return LEFT
                elif event.key == K_UP:
                    return UP
                elif event.key == K_RIGHT:
                    return RIGHT
                elif event.key == K_DOWN:
                    return DOWN
