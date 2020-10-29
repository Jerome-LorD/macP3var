#! /usr/bin/python
import random

class Labyrinth:
    """doc str"""

    def __init__(self, file, player):
        self.file = file
        self.player = player

        self.wall = []
        self.road = []
        self._start = []
        self._finish = []

        self.items_position = {"tube": True, "needle": True, "ether": True}
        self.items_states = {"tube": "", "needle": "", "ether": ""}
        self.collision_counter = 0

        self.running = True

        self.load_structure()
        self.randomize_tools()

    @property
    def start(self):
        return self._start

    @property
    def finish(self):
        return self._finish

    def __contains__(self, position):
        return position in self.road

    def verify_gatekeeper_contact(self, position):
        return position in self._finish

    def verify_items_contact(self, position):
        return position in self.items_position.values()

    def load_structure(self):
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

    def randomize_tools(self):
        for name in self.items_position.keys():
            if True in self.items_position.values():
                self.items_position[name] = random.choices(self.road[15:-15],\
                 weights=None, cum_weights=None, k=1)[0]
        return self.items_position

    def find_items(self):
        for name in self.items_position.keys():
            if self.items_position[name] == self.player.pos:
                self.collision_counter += 1
                self.items_states[name] = "found" 
                self.items_position[name] = False

    def update(self, control):
        
        self.old_pos = self.player.pos
        self.player.move(control)
        
        if self.player.pos not in self.road:
            self.player.pos = self.old_pos

        self.find_items()   

        if self.verify_gatekeeper_contact(self.player.pos) and self.collision_counter == 3:
            return False
        if self.verify_gatekeeper_contact(self.player.pos) and self.collision_counter < 3:
            return False
