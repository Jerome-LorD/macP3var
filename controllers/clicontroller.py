class CLIController:
    """Handle controls from keyboard inputs"""

    def __init__(self, labyrinth):
        self.lab = labyrinth

    def handle_control(self):
        """Manage all direction from input"""
        self.direction = ""
        board = ["up", "right", "down", "left", "q"]

        self.direction = str(
            input("Type the direction [right, left, up, down (q to quit)]-> ")
        )

        if self.direction == "q":
            print("thx, until next time")
            self.lab.run = False
        if self.direction not in board:
            print("Command not in the board")
            self.lab.run = True
        return self.direction
