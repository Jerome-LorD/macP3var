#! /usr/bin/python
"""player module recive order to move from controllers modules."""

from typing import List, Tuple

from model.labyrinth import Item

import settings


class Player:
    """Manage player's position from keyboard inputs."""

    def __init__(self, x: int, y: int) -> None:
        """Init x, y.

        Args:
            x (int): Abscissa
            y (int): Ordinate

        """
        self.pos: Tuple[int, int] = x, y

        self.bag: List[Item] = []

    def move(self, direction: str, roads: tuple) -> tuple:
        """Verify if player is in the roads and return direction from handle control.

        Args:
            direction (str): A str who represents the direction.

        Returns:
            tuple: The player's position.

        """
        self.old_pos = self.pos
        pos_x, pos_y = self.pos

        if direction == settings.UP:
            self.pos = (pos_x, pos_y - 1)
        elif direction == settings.DOWN:
            self.pos = (pos_x, pos_y + 1)
        elif direction == settings.RIGHT:
            self.pos = (pos_x + 1, pos_y)
        elif direction == settings.LEFT:
            self.pos = (pos_x - 1, pos_y)

        if self.pos not in roads:
            self.pos = self.old_pos
        return self.pos
