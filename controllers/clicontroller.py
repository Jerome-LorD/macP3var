"""Clicontroller module transmits commands to the player module."""


import settings


class CLIController:
    """Handle controls from keyboard inputs."""

    def handle_control(self) -> str:
        """Manage and return command from input."""
        command = ""
        board = ["up", "right", "down", "left", "q"]

        command = input(settings.INPUT)

        if command == "q":
            print(f"\n{settings.THX}")
        if command not in board:
            print(settings.NOT_IN_BOARD)
        return command
