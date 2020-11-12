"""player module recive order to move from controllers modules."""
from typing import List

from model.labyrinth import Item
from settings import UP, DOWN, RIGHT, LEFT


class Player:
    """Manage player's position from keyboard inputs."""

    def __init__(self, x: int, y: int) -> None:
        """Init x, y.

        Args:
            x (int): Abscissa
            y (int): Ordinate

        """
        self.pos = x, y

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

        if direction == UP:
            self.pos = (pos_x, pos_y - 1)
        elif direction == DOWN:
            self.pos = (pos_x, pos_y + 1)
        elif direction == RIGHT:
            self.pos = (pos_x + 1, pos_y)
        elif direction == LEFT:
            self.pos = (pos_x - 1, pos_y)

        if self.pos not in roads:
            self.pos = self.old_pos
        return self.pos
