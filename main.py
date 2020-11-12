#!/usr/bin/env python
"""Main application."""

from settings import CHOICES, CHOICE
from app import Application


def main():
    """Entry point of the Labyrinth application."""
    choices = CHOICES
    choice = input(CHOICE)

    if choice not in choices:
        choice = "1"

    app = Application(choices[choice])
    app.run()


if __name__ == "__main__":
    main()
