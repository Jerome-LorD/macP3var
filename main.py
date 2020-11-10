#!/usr/bin/env python
"""Main application."""

import settings
from app import Application


def main():
    """Entry point of the Labyrinth application."""
    choices = settings.CHOICES
    choice = input(settings.CHOICE)

    if choice not in choices:
        choice = "1"

    app = Application(choices[choice])
    app.run()


if __name__ == "__main__":
    main()
