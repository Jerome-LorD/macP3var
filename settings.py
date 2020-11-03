from termcolor import colored
from pathlib import Path


BASE_DIR = Path(".")
DATA_DIR = BASE_DIR / "data"
FONT_DIR = DATA_DIR / "fonts"
MAZE_DIR = DATA_DIR / "levels"

FONT_FILE = FONT_DIR / "Ranchers" / "Ranchers-Regular.ttf"

IMG_DIR = DATA_DIR / "ressource"

MAZE_FILE = MAZE_DIR / "maze.txt"

SCREEN_SIZE = (600, 660)
FPS = 30

FONT_SIZE = 30
TEXT_POSITION = (30, 610)

WIDTH = 15
HEIGHT = 15

WHITE = (255,255,255)
BLACK = (0, 0, 0)
GREEN = (0,255,0)
RED = (255,0,0)

WALL_RECT = (340,100,20,20)
STARTPOL_RECT = (160,20,20,20)
PLASTIC_TUBE_RECT = (0,0,259,194)
ETHER_RECT = (0,0,225,225)
NEEDLE_RECT = (0,0,545,720)
SYRINGE_RECT = (0,0,90,90)
CADRE_BOX_RECT = 0,603,600,53
STANDARD_IMG_RECT = (0,0,40,40)

CADRE_POS = (30,610)
ETHER_POS = (455,610)
NEEDLE_POS = (500,610)
TUBE_POS = (545,610)
SYRINGE_POS = (410,610)

IMG_SIZE = 40
IMG_HIDE_SIZE = (0, 0)

START_CHAR = "s"
WALL_CHAR = "W"
ROAD_CHAR = " "
FINNISH_CHAR = "f"
PLAYER_CHAR = colored("@", "yellow")
TUBE_CHAR = colored("$", "red")
NEEDLE_CHAR = colored("%", "red")
ETHER_CHAR = colored("#", "red")
SYRINGE_UNICODE = "\U0001F489"

WINCLI = colored("Congats, You WIN", "green")
LOSECLI = colored("You lose, you die\nGAME OVER", "red")
GOT_SYRINGE = "You got the syringe, you can get out -> "
