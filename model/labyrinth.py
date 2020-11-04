#! /usr/bin/python
import random


class Labyrinth:
    """Create the labyrinth and randomize the position of certain elements"""

    def __init__(self, file, player):

        self.file = file
        self.player = player

        self.run = True

        self.walls = []
        self.roads = []
        self._possible_starts = []
        self._finish = []
        self.possible_items = []
        self.randomizable_items = []
        self._rand_start = {"start": ()}
        self.items_position = {"tube": (), "needle": (), "ether": ()}
        self.collision_counter = 0
        self.items_taken = []
        self.run_states = ["running", "quit"]
        self.run_state = 0

        self.load_structure()
        self.randomize_items()
        self.randomize_start()
        self.set_player_position_on_start(self.starts)

    @property
    def starts(self):
        return self._rand_start["start"]

    @property
    def finish(self):
        return self._finish

    def __contains__(self, position):
        return position in self.roads

    def verify_gatekeeper_contact(self, position):
        """Verify if the player position is in the list _finnish."""
        return position in self.finish

    def verify_items_contact(self, position):
        """Verify if the player position is in the dict items_position."""
        return position in self.items_position.values()

    def load_structure(self):
        """Load file structure and create lists of coordinates."""
        with open(self.file) as levels:
            for pos_y, line in enumerate(levels):
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
                        self.randomizable_items.append((pos_x, pos_y))
                        self.roads.append((pos_x, pos_y))

    def randomize_items(self):
        """Randomize items coordinates"""
        for name in self.items_position:
            if not self.items_position[name]:
                self.items_position[name] =\
                     random.choice(self.randomizable_items)
                self.randomizable_items.remove(self.items_position[name])

    def randomize_start(self):
        """Randomize start coordinates"""
        for name in self._rand_start:
            if not self._rand_start[name]:
                self._rand_start[name] = random.choice(self._possible_starts)

    def find_items(self):
        """Verify if player is on item."""
        for name in self.items_position:
            if self.player.pos == self.items_position[name]:
                self.collision_counter += 1
                self.items_position[name] = ()

    def set_player_position_on_start(self, start_pos):
        """Set player position on start randomized position"""
        self.player.pos = start_pos

    def update(self, control):
        """Update positions of player"""

        self.player.move(control, self.roads)

        self.find_items()

        state = self.run_states[self.run_state]
        if control == "q" or state != "running":
            self.run_state += 1

        if (
            self.verify_gatekeeper_contact(self.player.pos)
            and self.collision_counter == 3
        ) or state != "running":
            self.run_state += 1

        if (
            self.verify_gatekeeper_contact(self.player.pos)
            and self.collision_counter < 3
        ) or state != "running":
            self.run_state += 1

        if state == "quit":
            self.run = False
