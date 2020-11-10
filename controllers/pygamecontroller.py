"""Pygamecontroller module transmits commands to the player module."""

import pygame
from pygame import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_UP

import settings

pygame.init()


class PYController:
    """Handle controls from keyboard events."""

    def handle_control(self):
        """Handle control from directional arrow on keyboard."""
        for event in pygame.event.get():
            if event.type == QUIT:
                return settings.QUIT
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    return settings.LEFT
                elif event.key == K_UP:
                    return settings.UP
                elif event.key == K_RIGHT:
                    return settings.RIGHT
                elif event.key == K_DOWN:
                    return settings.DOWN
