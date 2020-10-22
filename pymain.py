from controller.pycontroller import PYController
from model.labyrinth import Labyrinth
from model.player import Player
from views.pyview import PYView

def main():
    
    lab = Labyrinth("maze.txt")
    player = Player(0,0)
    view = PYView(lab, player)
    controller = PYController(player, lab, view)

    controller.run()


if __name__ == "__main__":
    main()