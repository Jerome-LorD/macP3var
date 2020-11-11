"""App module gets the choice of the version to run."""

from typing import Union

from settings import MAZE_FILE
from model.labyrinth import Labyrinth
from model.player import Player
from views.cliview import CLIView
from controllers.clicontroller import CLIController
from views.pygameview import PYView
from controllers.pygamecontroller import PYController


class Application:
    """MacGyver Application class."""

    def __init__(self, choice: str):
        """Init.

        Args:
            choice (str): the value of the choices's dict -> "pygame" or "cli".
        """
        self.player: Player = Player(0, 0)
        self.model: Labyrinth = Labyrinth(MAZE_FILE, self.player)

        self.choice: str = choice

        if choice == "cli":
            self.view: Union[PYView, CLIView] = CLIView(self.model)
            self.controller: Union[PYController, CLIController] = CLIController()

        elif choice == "pygame":
            self.view: Union[PYView, CLIView] = PYView(self.model)
            self.controller: Union[PYController, CLIController] = PYController()

    def run(self):
        """Run main method."""
        while self.model.run:
            if self.view.display() is False:
                return
            control = self.controller.handle_control()
            self.model.update(control)
