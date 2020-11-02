import os

import pygame as pg
from pygame.locals import *

import settings


class PYView:
    """Manage and display images and texts with pygame"""

    def __init__(self, lab):
        pg.init()
        self.lab = lab

        self.items_taken = []
        self.items_pos = {
            "tube": settings.TUBE_POS,
            "needle": settings.NEEDLE_POS,
            "ether": settings.ETHER_POS,
        }

        self.screen_size = settings.SCREEN_SIZE
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("MacGyver - V1.0")

        self.text = [
            "Make a syringe.",
            "Nice job! Now, you can get out.",
            "You lose! you die... GAME OVER !!!",
            "Congrats, you win! Free to get out",
        ]

        self.font = self.load_font(settings.FONT_FILE)

        self.images = {
            "macgyver": self.load_image(settings.IMG_DIR / "macgyver.png"),
            "macgyver2": self.load_image(settings.IMG_DIR / "macgyver2.png"),
            "tube": self.load_image(settings.IMG_DIR / "tube2.png"),
            "needle": self.load_image(settings.IMG_DIR / "needle.png"),
            "ether": self.load_image(settings.IMG_DIR / "ether.png"),
            "syringe": self.load_image(settings.IMG_DIR / "syringe2.png"),
            "brick": self.load_image(settings.IMG_DIR / "brick.png"),
            "start": self.load_image(settings.IMG_DIR / "start.png"),
            "gatekeeper": self.load_image(settings.IMG_DIR / "gatekeeper.png"),
            "ground": self.load_image(settings.IMG_DIR / "ground.png"),
        }

    def load_font(self, path):
        try:
            return pg.font.Font(str(path), settings.FONT_SIZE)
        except FileNotFoundError:
            raise SystemExit(f"Cannot load font: {path}")

    def load_image(self, path):
        try:
            return pg.image.load(str(path)).convert_alpha()
        except FileNotFoundError:
            raise SystemExit(f"Cannot load image: {path}")

    def change_state(self):
        """Manage the filling of items_taken list"""
        for item in self.lab.items_states:
            if self.lab.items_states[item] == "found":
                self.items_taken.append(self.images[item])
                # To stop filling the list:
                self.lab.items_states[item] = "taken"

    def display_items(self):
        """Display items in the bottom frame"""
        if len(self.items_taken) >= 1:
            for name in self.items_pos:
                if self.lab.player.pos == self.lab.new_items[name]:
                    self.screen.blit(self.images[name], self.items_pos[name])
        if len(self.items_taken) == 3:
            # img_base = self.images["syringe"]
            # self.images["syringe"] = pg.transform.rotate(img_base, rot_const)
            self.screen.blit(self.images["syringe"], settings.SYRINGE_POS)
        if (
            self.lab.collision_counter == 3
            and self.lab.player.pos == self.lab.finish[0]
        ):
            self.screen.blit(self.images["macgyver2"], (120, 120))

    def display_txt(self):
        """Display texts in the bottom frame"""
        if self.lab.collision_counter < 3 and self.lab.player.pos == self.lab.finish[0]:
            return self.font.render(self.text[2], True, settings.RED, settings.BLACK)
        elif (
            self.lab.collision_counter == 3
            and not self.lab.player.pos == self.lab.finish[0]
        ):
            return self.font.render(self.text[1], True, settings.WHITE, settings.BLACK)
        elif (
            self.lab.collision_counter == 3
            and self.lab.player.pos == self.lab.finish[0]
        ):
            return self.font.render(self.text[3], True, settings.GREEN, settings.BLACK)
        else:
            return self.font.render(self.text[0], True, settings.WHITE, settings.BLACK)

    def display(self):
        """Display the game"""

        self.change_state()
        # self.display_items()

        reversed_items_position = {
            pos: name for name, pos in self.lab.items_position.items()
        }

        pg.draw.rect(self.screen, settings.WHITE, settings.CADRE_BOX_RECT, 10)
        self.screen.blit(self.display_txt(), settings.TEXT_POSITION)

        for pos_y in range(settings.WIDTH):
            for pos_x in range(settings.HEIGHT):
                position = pos_x, pos_y
                pygame_pos = pos_x * settings.IMG_SIZE, pos_y * settings.IMG_SIZE

                if position == self.lab.player.pos:
                    surface = self.images["macgyver"]
                elif position in self.lab.items_position.values():
                    surface = self.images[reversed_items_position[position]]
                elif position in self.lab.wall:
                    surface = self.images["brick"]
                elif position == self.lab.start:
                    surface = self.images["start"]
                elif position in self.lab.finish:
                    surface = self.images["gatekeeper"]
                elif position in self.lab.road:
                    surface = self.images["ground"]

                self.screen.blit(surface, pygame_pos)
                self.display_items()
                pg.display.flip()
