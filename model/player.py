#! /usr/bin/python

class Player:
    def __init__(self, x, y):
        self.pos = x, y

    def __eq__(self, other):
        return self.pos == other.pos

    def move(self, direction):
        pos_x, pos_y = self.pos
        if direction == "up":
            self.pos = (pos_x, pos_y - 1*40)
        elif direction == "down":
            self.pos = (pos_x, pos_y + 1*40)
        elif direction == "right":
            self.pos = (pos_x + 1*40, pos_y)
        elif direction == "left":
            self.pos = (pos_x - 1*40, pos_y)

        return self.pos