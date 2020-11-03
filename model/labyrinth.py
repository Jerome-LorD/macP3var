#! /usr/bin/python
import random



class Labyrinth:
    """Create the labyrinth and randomize the position of certains elements"""

    def __init__(self, file, player):

        self.file = file
        self.player = player

        self.run = True

        self.wall = []
        self.road = []
        self._start = []
        self._finish = []
        self.items = []
        self.rand_start = {"start": ()}
        self.items_position = {"tube": (), "needle": (), "ether": ()}
        self.collision_counter = 0
        self.items_taken = []

        self.load_structure()
        self.randomize_items()
        self.randomize_start()
        self.set_player_position_on_start(self.start)

    @property
    def start(self):
        return self.rand_start["start"]

    @property
    def finish(self):
        return self._finish

    def __contains__(self, position):
        return position in self.road

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
                        self.wall.append((pos_x, pos_y))
                    elif char == " ":
                        self.road.append((pos_x, pos_y))
                    elif char == "s":
                        self._start.append((pos_x, pos_y))
                        self.road.append((pos_x, pos_y))
                    elif char == "f":
                        self._finish.append((pos_x, pos_y))
                        self.road.append((pos_x, pos_y))
                    elif char == ".":
                        self.items.append((pos_x, pos_y))
                        self.road.append((pos_x, pos_y))

    def randomize_items(self):
        """Randomize items coordinates"""
        for name in self.items_position:
            if not self.items_position[name]:
                self.items_position[name] = random.choice(self.items)

    def randomize_start(self):
        """Randomize start coordinates"""
        for name in self.rand_start:
            if not self.rand_start[name]:
                self.rand_start[name] = random.choice(self._start)

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
        self.old_pos = self.player.pos
        self.player.move(control)

        if self.player.pos not in self.road:
            self.player.pos = self.old_pos

        self.find_items()

        # if self.verify_gatekeeper_contact(self.player.pos)\
        # and self.collision_counter == 3:
        #     self.run = False
        # if self.verify_gatekeeper_contact(self.player.pos)\
        # and self.collision_counter < 3:
        #     self.run = False
