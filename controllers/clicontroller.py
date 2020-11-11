"""Clicontroller module transmits commands to the player module."""


from settings import UP, RIGHT, DOWN, LEFT, QUIT_APP, INPUT, THX, NOT_IN_BOARD


class CLIController:
    """Handle controls from keyboard inputs."""

    def handle_control(self) -> str:
        """Manage and return command from input."""
        command = ""
        board = [UP, RIGHT, DOWN, LEFT, QUIT_APP]

        command = input(INPUT)

        if command == QUIT_APP:
            print(f"\n{THX}")
        if command not in board:
            print(NOT_IN_BOARD)
        return command
