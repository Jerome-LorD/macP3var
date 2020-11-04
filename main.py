"""Main application."""

import settings
from app import Application


def main():
    """Entry point of the Maze application."""
    choices = {"1": "cli", "2": "pygame"}
    choice = input(settings.CHOICE)

    if choice not in choices:
        choice = "1"

    app = Application(choices[choice])
    app.run()


if __name__ == "__main__":
    main()
