import settings


class CLIController:
    """Handle controls from keyboard inputs"""

    def __init__(self, labyrinth):
        self.lab = labyrinth

    def handle_control(self):
        """Manage all direction from input"""

        if self.lab.run_state != 0:
            return "q"
        else:
            command = ""
            board = ["up", "right", "down", "left", "q"]

            command = str(
                input(settings.INPUT)
            )

            if command == "q":
                print(f"\n{settings.THX}")
            if command not in board:
                print(settings.NOT_IN_BOARD)
            return command
