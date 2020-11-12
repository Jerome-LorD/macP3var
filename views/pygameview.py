"""pygameview load all graphical parts and display the game onto a pygame screen."""
import pygame as pg

from pathlib import Path
from typing import Dict, Tuple

from model.labyrinth import Labyrinth
from settings import (
    TUBE_POS,
    NEEDLE_POS,
    ETHER_POS,
    SCREEN_SIZE,
    ADVICEPY,
    NICE,
    LOSEPY,
    WINPY,
    FONT_FILE,
    IMG_DIR,
    FONT_SIZE,
    SYRINGE_POS,
    IMG_WIN_POS,
    RED,
    WHITE,
    BLACK,
    GREEN,
    IMG_SIZE,
    FRM_BOX,
    FRAME_WIDTH,
    TEXT_POSITION,
    WIDTH,
    HEIGHT,
)


class PYView:
    """Manage and display images and texts with pygame."""

    def __init__(self, lab):
        """Init."""
        pg.font.init()
        pg.display.init()

        self.lab: Labyrinth = lab

        self.items_pos: Dict[str, tuple] = {
            "tube": TUBE_POS,
            "needle": NEEDLE_POS,
            "ether": ETHER_POS,
        }

        self.screen_size: Tuple[int, int] = SCREEN_SIZE
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("MacGyver - V1.0")

        self.text: Dict[str, str] = {
            "advice": ADVICEPY,
            "nice": NICE,
            "lose": LOSEPY,
            "win": WINPY,
        }

        self.font: pg.font.Font = self.load_font(FONT_FILE)

        self.images: Dict[str, pg.Surface] = {
            "macgyver": self.load_image(IMG_DIR / "macgyver.png"),
            "macgyver2": self.load_image(IMG_DIR / "macgyver2.png"),
            "tube": self.load_image(IMG_DIR / "tube2.png"),
            "needle": self.load_image(IMG_DIR / "needle.png"),
            "ether": self.load_image(IMG_DIR / "ether.png"),
            "syringe": self.load_image(IMG_DIR / "syringe2.png"),
            "brick": self.load_image(IMG_DIR / "brick.png"),
            "start": self.load_image(IMG_DIR / "start.png"),
            "gatekeeper": self.load_image(IMG_DIR / "gatekeeper.png"),
            "ground": self.load_image(IMG_DIR / "ground.png"),
        }

        pg.display.set_icon(self.images["macgyver"])

    def load_font(self, path: Path) -> pg.font.Font:
        """Load font."""
        try:
            return pg.font.Font(str(path), FONT_SIZE)
        except FileNotFoundError:
            raise SystemExit(f"Cannot load font: {path}")

    def load_image(self, path: Path) -> pg.Surface:
        """Load image."""
        try:
            return pg.image.load(str(path)).convert_alpha()
        except FileNotFoundError:
            raise SystemExit(f"Cannot load image: {path}")

    def display_items_in_frame(self):
        """Display items in the bottom frame."""
        for item in self.lab.player.bag:
            self.screen.blit(self.images[item.name], self.items_pos[item.name])

    def display_syringe(self):
        """Display syringe if player get all items."""
        if len(self.lab.player.bag) == len(self.lab.items_names):
            self.screen.blit(self.images["syringe"], SYRINGE_POS)

    def display_win(self):
        """Display win image."""
        if (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.screen.blit(self.images["macgyver2"], IMG_WIN_POS)

    def display_text(self):
        """Display texts in the bottom frame."""
        if (
            len(self.lab.player.bag) < len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.lab.run_state = 1
            return self.font.render(self.text["lose"], True, RED, BLACK)
        elif (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and not self.lab.player.pos == self.lab.finish
        ):
            return self.font.render(self.text["nice"], True, WHITE, BLACK)
        elif (
            len(self.lab.player.bag) == len(self.lab.items_names)
            and self.lab.player.pos == self.lab.finish
        ):
            self.lab.run_state = 1
            return self.font.render(self.text["win"], True, GREEN, BLACK)
        else:
            return self.font.render(self.text["advice"], True, WHITE, BLACK)

    def display_items(self):
        """Display items in the game."""
        for item in self.lab.items:
            pos_x, pos_y = item.coords
            position = pos_x * IMG_SIZE, pos_y * IMG_SIZE

            self.screen.blit(self.images[item.name], position)

    def display(self):
        """Display the game."""
        pg.draw.rect(self.screen, WHITE, FRM_BOX, FRAME_WIDTH)
        self.screen.blit(self.display_text(), TEXT_POSITION)

        for pos_y in range(WIDTH):
            for pos_x in range(HEIGHT):
                position = pos_x, pos_y
                pygame_pos = pos_x * IMG_SIZE, pos_y * IMG_SIZE

                if position == self.lab.player.pos:
                    surface = self.images["macgyver"]
                elif position in self.lab.walls:
                    surface = self.images["brick"]
                elif position == self.lab.start:
                    surface = self.images["start"]
                elif position == self.lab.finish:
                    surface = self.images["gatekeeper"]
                elif position in self.lab.roads:
                    surface = self.images["ground"]

                self.screen.blit(surface, pygame_pos)
                self.display_items()
                self.display_items_in_frame()
                self.display_syringe()
                self.display_win()
                pg.display.flip()
