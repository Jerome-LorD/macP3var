
class CLIController:
    """Do only one thing for the moment: handle controls from input"""
    def __init__(self, labyrinth):
        self.lab = labyrinth

    def handle_control(self):
        """Manage all direction from input"""
        self.direction = ""
        board = ["up", "right", "down", "left", "q"]
        try:        
            self.direction = str(input("Chose the direction: "))
        except ValueError:
            print('Invalid input! Type character please.')
            return True
        if self.direction == "q":
            print("thx, until next time")
            return False
        if self.direction not in board:
            print("Command not in the board")
            return True
        return self.direction