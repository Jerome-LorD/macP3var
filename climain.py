from controller.clicontroller import CLIController
from model.labyrinth import Labyrinth
from model.player import Player
from views.cliview import CLIView


def main():
    lab = Labyrinth("maze.txt")
    player = Player(0,0)
    view = CLIView(lab, player)
    controller = CLIController(player, lab, view)

    controller.run()

if __name__ == "__main__":
    main()