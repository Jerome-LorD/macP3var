#! /usr/bin/python
import random


class Item:
    """Keep the state of items"""
    def __init__(self, name, pos):
        self.name = name
        self.position = pos
        # self.item_state = "found"


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
        self.rand_start = {"start": "position"}

        self.new_items = {"tube": (), "needle": (), "ether": ()}
        self.items_position = {"tube": (), "needle": (), "ether": ()}
        self.items_states = {"tube": "", "needle": "", "ether": ""}
        self.collision_counter = 0

        self.load_structure()
        # self.randomize_items()
        self.randomize_via_Item()
        self.randomize_start()
        self.set_player_position_on_start(self.start)

    # @property
    # def start(self):
    #     return self._start

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
        return position in self._finish

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

    def randomize_via_Item(self):
        """It was the goal but..."""
        for name, position in self.items_position.items():
            self.item = Item(name, position)
            if not self.item.position:
                rnd_choice = random.choice(self.items)
                if rnd_choice not in self.items_position.values():
                    self.items_position[name] = rnd_choice

    # def randomize_items(self):
    #     """docstr"""
    #     for name in self.items_position.keys():
    #         if "open" in self.items_position.values():
    #             self.items_position[name] = random.choice(self.items)
    #     return self.items_position

    def randomize_start(self):
        """docstr"""
        for name in self.rand_start.keys():
            if "position" in self.rand_start.values():
                self.rand_start[name] = random.choice(self._start)
        return self.rand_start[name]

    # def find_items(self):
    #     for name in self.items_position.keys():
    #         if self.items_position[name] == self.player.pos:
    #             self.collision_counter += 1
    #             self.items_states[name] = "found"
    #             self.items_position[name] = "close"

    def find_items(self):
        """docstr"""
        for name, position in self.items_position.items():
            self.item = Item(name, position)
            if self.player.pos == self.items_position[name]:
                self.collision_counter += 1
                self.items_states[name] = "found"
                self.new_items[name] = self.items_position[name]
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
        #  and self.collision_counter == 3:
        #     self.run = False
        # if self.verify_gatekeeper_contact(self.player.pos)\
        #  and self.collision_counter < 3:
        #     self.run = False
