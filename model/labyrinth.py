#! /usr/bin/python

class Labyrinth:
    """doc str"""

    def __init__(self, filename):
        self.filename = filename

        self.coord_let = []
        self.wall = []
        self.road = []
        self._start = []
        self._finish = []
        self.tools = []
        self.toolbox = []

        self.load_structure()

    @property
    def wall_lst(self):
        return self.wall

    @property
    def start(self):
        return self._start

    @property
    def finish(self):
        return self._finish

    @property
    def tools_rand(self):
        return self.random_tools()

    def __contains__(self, position):
        return position in self.road

    def __getitem__(self, key):
        return self.tools[key]
        
    def collide_gatekeeper(self, position):
        return position in self._finish

    def collide_tube(self, position):
        return position in tuple(self.tools_rand)[0]

    def collide_needle(self, position):
        return position in tuple(self.tools_rand)[1]

    def collide_ether(self, position):
        return position in tuple(self.tools_rand)[2]

    def load_structure(self):
        with open(self.filename) as levels:
            for line in levels:
                self.coord_let.append(line.strip('\n'))
        for y in range(15):
            for x,v in enumerate(self.coord_let[y]):
                if v == "W":
                    self.wall.append((x*40, y*40))
                elif v == " ":
                    self.road.append((x*40, y*40))
                elif v == "s":
                    self._start.append((x*40, y*40))
                    self.road.append((x*40, y*40))
                elif v == "f":
                    self._finish.append((x*40, y*40))                    
                    self.road.append((x*40, y*40))


    def random_tools(self):
        for i in range(3):
            self.tools.append(random.choices(self.road[15:110],\
                 weights=None, cum_weights=None, k=1))
            if i == 3:
                break
        return self.tools
