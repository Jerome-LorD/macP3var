class CLIController:
    def __init__(self, player, labyrinth, view):
        self.player = player
        self.lab = labyrinth
        self.view = view

    def run(self):
        self.view.display(self.player.pos)

        while self.view.run:
            self.old_pos = self.player.pos

            if self.view.get_player_controls() == 0:
                return

            if self.player.pos not in self.lab.road:
                self.player.pos = self.old_pos
            else:
                self.view.display(self.player.move(self.view.direction))