#! /usr/bin/python
# Python Enhancement Proposals (propositions d'amélioration de Python)
"""labyrinth constructs and updates the game."""

import random

from typing import List, Dict, Tuple


class Item:
    """Keeps the state of attributes."""

    def __init__(self, name: str, coords: tuple):
        """Init."""
        self.name = name
        self.coords = coords


class Labyrinth:
    """

    Create the labyrinth structure.

    - randomize the items,
    - randomize start position,
    - take items if player position on it,
    - update the game.
    """

    def __init__(self, file, player):
        """Init Labyrinth."""
        self.level_txt = file
        self.player = player

        self.run: bool = True

        self.walls: List[Tuple[int, int]] = []
        self.roads: List[Tuple[int, int]] = []
        self._possible_starts: List[Tuple[int, int]] = []
        self._finish: List[Tuple[int, int]] = []
        self.possible_items: List[Tuple[int, int]] = []
        self._rand_start: Dict[str, Tuple[int, int]] = {"coord": ()}
        self.items_names = ["tube", "needle", "ether"]
        self.items: List[Item] = []
        self.run_states: List[str, str, str] = ["running", "process_quit", "quit"]
        self.run_state: int = 0

        self.load_structure()
        self.randomize_items()
        self.randomize_start()
        self.set_player_position_on_start(self.starts)

    @property
    def starts(self) -> Tuple[int, int]:
        """Return randomized start position."""
        return self._rand_start["coord"]

    @property
    def finish(self) -> Tuple[int, int]:
        """Return the guard position."""
        return self._finish[0]

    def load_structure(self):
        """Load file structure and create lists of coordinates."""
        with open(self.level_txt) as level:
            for pos_y, line in enumerate(level):
                for pos_x, char in enumerate(line):
                    if char == "W":
                        self.walls.append((pos_x, pos_y))
                    elif char == " ":
                        self.roads.append((pos_x, pos_y))
                    elif char == "s":
                        self._possible_starts.append((pos_x, pos_y))
                        self.roads.append((pos_x, pos_y))
                    elif char == "f":
                        self._finish.append((pos_x, pos_y))
                        self.roads.append((pos_x, pos_y))
                    elif char == ".":
                        self.possible_items.append((pos_x, pos_y))
                        self.roads.append((pos_x, pos_y))

    def randomize_start(self):
        """Randomize start coordinates."""
        for name in self._rand_start:
            if not self._rand_start[name]:
                self._rand_start[name] = random.choice(self._possible_starts)

    def set_player_position_on_start(self, start_pos: tuple):
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
        if control == "q":
            self.run = False

        if state == "quit":
            self.run = False
