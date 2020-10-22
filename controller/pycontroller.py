

class PYController:
    def __init__(self, player, labyrinth, view):
        self.player = player
        self.lab = labyrinth
        self.view = view

    def take_tool_and_put_in_toolbox(self, tool):
        if tool == self.view.ether:
            self.view.ether = pygame.transform.scale(tool, (0, 0))
            screen.blit(self.view.ether2, (455,610))
        if tool == self.view.needle:
            self.view.needle = pygame.transform.scale(self.view.needle, (0, 0))
            screen.blit(self.view.needle2, (500,610))
        if tool == self.view.plastic_tube:
            self.view.plastic_tube = pygame.transform.scale(self.view.plastic_tube, (0, 0))
            screen.blit(self.view.plastic_tube2, (545,610))

    def take_things(self):
        if self.lab.collide_tube(self.player.pos):
            self.view.holster.append(self.view.plastic_tube2)

        if self.lab.collide_needle(self.player.pos):
            self.view.holster.append(self.view.needle2)
      
        if self.lab.collide_ether(self.view.player.pos):
            self.view.holster.append(self.view.ether2)
        self.view.get_holster()

    def end_game(self):
        if self.lab.collide_gatekeeper(self.player.pos) and len(self.view.holster) > 2:
            self.view.blit_you_win()
            return 0
        if self.lab.collide_gatekeeper(self.player.pos) and len(self.view.holster) < 3:
            self.view.blit_you_lose()
            return 0 

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
                self.take_things()
                self.end_game()
        self.view.closing()
