"""Contains all constants."""

from colorama import init
from termcolor import colored
from pathlib import Path

init(autoreset=True)

BASE_DIR = Path(".")
DATA_DIR = BASE_DIR / "data"
FONT_DIR = DATA_DIR / "fonts"
MAZE_DIR = DATA_DIR / "levels"

FONT_FILE = FONT_DIR / "Ranchers" / "Ranchers-Regular.ttf"

IMG_DIR = DATA_DIR / "ressource"

MAZE_FILE = MAZE_DIR / "maze.txt"

SCREEN_SIZE = (600, 660)

FONT_SIZE = 30
TEXT_POSITION = (30, 610)

WIDTH = 15
HEIGHT = 15

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WALL_RECT = (340, 100, 20, 20)
STARTPOL_RECT = (160, 20, 20, 20)
PLASTIC_TUBE_RECT = (0, 0, 259, 194)
ETHER_RECT = (0, 0, 225, 225)
NEEDLE_RECT = (0, 0, 545, 720)
SYRINGE_RECT = (0, 0, 90, 90)
FRM_BOX = 0, 603, 600, 53
STANDARD_IMG_RECT = (0, 0, 40, 40)

FRAME_WIDTH = 10

ETHER_POS = (455, 610)
NEEDLE_POS = (500, 610)
TUBE_POS = (545, 610)
SYRINGE_POS = (410, 610)
IMG_WIN_POS = (120, 120)

IMG_SIZE = 40

START_CHAR = "S"
WALL_CHAR = "X"
ROAD_CHAR = " "
FINISH_CHAR = "F"
POSSIBLE_ITEMS_CHAR = "."
PLAYER_CHAR = colored("@", "yellow")
TUBE_CHAR = colored("$", "red")
NEEDLE_CHAR = colored("%", "red")
ETHER_CHAR = colored("#", "red")
SYRINGE_UNICODE = "\U0001F489"
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
QUIT = "q"

CHOICES = {"1": "cli", "2": "pygame"}
CHOICE = "Type a choice:\n1. cli\n2. pygame - [1 or 2]-> "
INPUT = "Type the direction [right, left, up, down (q to quit)]-> "
NOT_IN_BOARD = "Command not in the board"
HEADER = f'#{colored("-MacGyver -- Get out vc-1 -", "yellow")}#'
DASHES = "# ------------------------- #"
ADVICE = "Take all items if you wanna get out."
POSSESSION = "In your possession -> "
WINCLI = colored("Congats, You WIN", "green")
LOSECLI = colored("You lose, you die\nGAME OVER", "red")
GOT_SYRINGE = "You got the syringe, you can get out -> "
THX = colored("Thx, until next time", "green")
