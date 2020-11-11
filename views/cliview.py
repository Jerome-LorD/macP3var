"""cliview display the game onto the terminal."""
from typing import List, Dict

from model.labyrinth import Labyrinth
from settings import (
    TUBE_CHAR,
    NEEDLE_CHAR,
    ETHER_CHAR,
    POSSESSION,
    LOSECLI,
    WINCLI,
    GOT_SYRINGE,
    SYRINGE_UNICODE,
    ADVICECLI,
    DASHES,
    HEADER,
    WIDTH,
    HEIGHT,
    PLAYER_CHAR,
    WALL_CHAR,
    START_CHAR,
    FINISH_CHAR,
    ROAD_CHAR,
)


class CLIView:
    """Manage and display all prints."""

    def __init__(self, lab):
        """Init."""
        self.lab: Labyrinth = lab

        self.char: str = " "
        self.items_taken: List[str] = []
        self.chars: Dict[str, str] = {
            "tube": TUBE_CHAR,
            "needle": NEEDLE_CHAR,
            "ether": ETHER_CHAR,
        }

    def display_items_taken(self):
        """Display items taken and texts."""
        if len(self.lab.player.bag):
            items_taken = [self.chars[item.name] for item in self.lab.player.bag]
            print(f"{POSSESSION} {' '.join(items_taken)}")

        if (
            len(self.lab.player.bag) < len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.lab.run_state = 1
            print(LOSECLI)
            self.lab.run = False

        elif (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and not self.lab.player.pos == self.lab.finish
        ):
            print(f"{GOT_SYRINGE} {SYRINGE_UNICODE}")

        elif (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.lab.run_state = 1
            print(f"{WINCLI} {SYRINGE_UNICODE}")
            self.lab.run = False

        else:
            print(ADVICECLI)

    def header(self):
        """Display the header."""
        print(f"\n{DASHES}\n{HEADER}\n{DASHES}")

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

        for pos_y in range(WIDTH):
            for pos_x in range(HEIGHT):
                position = pos_x, pos_y

                if position == self.lab.player.pos:
                    self.char = PLAYER_CHAR
                elif position in self.lab.walls:
                    self.char = WALL_CHAR
                elif position == self.lab.start:
                    self.char = START_CHAR
                elif position == self.lab.finish:
                    self.char = FINISH_CHAR
                else:
                    self.char = ROAD_CHAR

                self.display_items(position)

                print(self.char, end=" ")
            print()
        print()

        self.display_items_taken()
        return self.lab.run
