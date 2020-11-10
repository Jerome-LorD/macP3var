"""cliview display the game onto the terminal."""

from typing import List, Dict

from model.labyrinth import Labyrinth

import settings


class CLIView:
    """Manage and display all prints."""

    def __init__(self, lab):
        """Init."""
        self.lab: Labyrinth = lab

        self.char: str = " "
        self.items_taken: List[str] = []
        self.chars: Dict[str, str] = {
            "tube": settings.TUBE_CHAR,
            "needle": settings.NEEDLE_CHAR,
            "ether": settings.ETHER_CHAR,
        }

    def display_items_taken(self):
        """Display items taken and texts."""
        if len(self.lab.player.bag):
            items_taken = [self.chars[item.name] for item in self.lab.player.bag]
            print(f"{settings.POSSESSION} {' '.join(items_taken)}")

        if (
            len(self.lab.player.bag) < len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.lab.run_state = 1
            print(settings.LOSECLI)
            self.lab.run = False

        elif (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and not self.lab.player.pos == self.lab.finish
        ):
            print(f"{settings.GOT_SYRINGE} {settings.SYRINGE_UNICODE}")

        elif (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.lab.run_state = 1
            print(f"{settings.WINCLI} {settings.SYRINGE_UNICODE}")
            self.lab.run = False

        else:
            print(settings.ADVICE)

    def header(self):
        """Display the header."""
        print(f"\n{settings.DASHES}\n{settings.HEADER}\n{settings.DASHES}")

    def display_items(self, position: tuple) -> str:
        """Display items.

        Args:
            position (tuple): A position in the labyrinth.

        Returns:
            str: The char associated with the name to print.

        """
        for item in self.lab.items:
            if position == item.coords:
                self.char = self.chars[item.name]
        return self.char

    def display(self) -> bool:
        """Display the game."""
        self.header()

        for pos_y in range(settings.WIDTH):
            for pos_x in range(settings.HEIGHT):
                position = pos_x, pos_y

                if position == self.lab.player.pos:
                    self.char = settings.PLAYER_CHAR
                elif position in self.lab.walls:
                    self.char = settings.WALL_CHAR
                elif position == self.lab.starts:
                    self.char = settings.START_CHAR
                elif position == self.lab.finish:
                    self.char = settings.FINISH_CHAR
                else:
                    self.char = settings.ROAD_CHAR

                self.display_items(position)

                print(self.char, end=" ")
            print()
        print()

        self.display_items_taken()
        return self.lab.run
