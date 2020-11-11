#! /usr/bin/python
"""labyrinth constructs and updates the game."""

import random

from pathlib import Path

from typing import List, Tuple

import settings


class Item:
    """Keeps the state of attributes."""

    def __init__(self, name: str, coords: tuple):
        """Init."""
        self.name: str = name
        self.coords: tuple = coords


class Labyrinth:
    """

    Create the labyrinth structure.

    - randomize the items,
    - randomize start position,
    - take items if player position on it,
    - update the game.
    """

    def __init__(self, filename: Path, player):
        """Init Labyrinth."""
        self.level_txt: Path = filename
        self.player = player

        self.run: bool = True

        self.walls: List[Tuple[int, int]] = []
        self.roads: List[Tuple[int, int]] = []
        self.possible_starts: List[Tuple[int, int]] = []
        self.finish: Tuple[()] = ()
        self.possible_items: List[Tuple[int, int]] = []
        self.start: Tuple[()] = ()
        self.items_names: List[str] = ["tube", "needle", "ether"]
        self.items: List[Item] = []
        self.run_states: List[str] = ["running", "process_quit", "quit"]
        self.run_state: int = 0

        self.load_structure()
        self.randomize_items()
        self.randomize_start()
        self.set_player_position_on_start(self.start)

    def load_structure(self):
        """Load file structure and create lists of coordinates."""
        with open(self.level_txt) as level:
            for pos_y, line in enumerate(level):
                for pos_x, char in enumerate(line):
                    if char == settings.WALL_CHAR:
                        self.walls.append((pos_x, pos_y))
                    elif char == settings.ROAD_CHAR:
                        self.roads.append((pos_x, pos_y))
                    elif char == settings.START_CHAR:
                        self.possible_starts.append((pos_x, pos_y))
                        self.roads.append((pos_x, pos_y))
                    elif char == settings.FINISH_CHAR:
                        self.finish = (pos_x, pos_y)
                        self.roads.append((pos_x, pos_y))
                    elif char == settings.POSSIBLE_ITEMS_CHAR:
                        self.possible_items.append((pos_x, pos_y))
                        self.roads.append((pos_x, pos_y))

    def randomize_start(self):
        """Randomize start coordinates."""
        if not self.start:
            self.start = random.choice(self.possible_starts)

    def set_player_position_on_start(self, start_pos):
        """Set player position on start randomized coordinate."""
        self.player.pos = start_pos

    def randomize_items(self):
        """Randomize items coordinates."""
        for name in self.items_names:
            position = random.choice(self.possible_items)
            self.possible_items.remove(position)
            item = Item(name, position)
            self.items.append(item)

    def find_item(self, player_position: tuple):
        """Remove the item if the player position is equal to an item position."""
        for item in self.items:
            if item.coords == player_position:
                self.items.remove(item)
                self.player.bag.append(item)

    def update(self, control: str):
        """Update player position, items and quit the game."""
        self.player.move(control, self.roads)

        self.find_item(self.player.pos)

        if self.player.pos == self.finish:
            self.run_state += 1

        state = self.run_states[self.run_state]
        if control == settings.QUIT:
            self.run = False

        if state == "quit":
            self.run = False
