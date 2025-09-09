#!/usr/bin/env python3
"""
Simple test application that prints a welcome message and random color.
"""

import random


def get_random_color():
    """Return a random color name."""
    colors = [
        "red", "blue", "green", "yellow", "purple", 
        "orange", "pink", "cyan", "magenta", "lime"
    ]
    return random.choice(colors)


def print_welcome():
    """Print welcome message with a random color."""
    color = get_random_color()
    message = f"Welcome! Your random color is: {color}"
    print(message)
    return message


def main():
    """Main function to run the application."""
    print_welcome()


if __name__ == "__main__":
    main()