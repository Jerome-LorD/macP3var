import pygame
from pygame.locals import *
from model.player import Player
from model.labyrinth import Labyrinth
from views.cliview import CLIView
from controllers.clicontroller import CLIController
from views.pygameview import PYView
from controllers.pygamecontroller import PYController


class Application:
    """Maze application class."""

    def __init__(self, choice: str):
        """Init."""
        self.player = Player(0, 0)
        self.model = Labyrinth("data/levels/maze.txt", self.player)

        self.running = True
        self.choice = choice

        if choice == "cli":
            self.view = CLIView(self.model)
            self.controller = CLIController(self.model)
            pass
        elif choice == "pygame":
            self.view = PYView(self.model)
            self.controller = PYController(self.model)

    def run(self):
        """Run main method."""
        # self.running = True
        running = True
        while running:
            self.view.display()
            control = self.controller.handle_control()
            self.model.update(control)
        