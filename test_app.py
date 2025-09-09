#!/usr/bin/env python3
"""
Unit tests for the simple test application.
"""

import unittest
from unittest.mock import patch
import app


class TestApp(unittest.TestCase):
    """Test cases for the app module."""

    def test_get_random_color_returns_valid_color(self):
        """Test that get_random_color returns a color from the expected list."""
        expected_colors = [
            "red", "blue", "green", "yellow", "purple", 
            "orange", "pink", "cyan", "magenta", "lime"
        ]
        color = app.get_random_color()
        self.assertIn(color, expected_colors)

    def test_get_random_color_returns_string(self):
        """Test that get_random_color returns a string."""
        color = app.get_random_color()
        self.assertIsInstance(color, str)

    @patch('app.get_random_color')
    def test_print_welcome_message_format(self, mock_get_color):
        """Test that print_welcome returns the correct message format."""
        mock_get_color.return_value = "blue"
        expected_message = "Welcome! Your random color is: blue"
        
        result = app.print_welcome()
        self.assertEqual(result, expected_message)

    @patch('builtins.print')
    @patch('app.get_random_color')
    def test_print_welcome_calls_print(self, mock_get_color, mock_print):
        """Test that print_welcome calls print with the correct message."""
        mock_get_color.return_value = "red"
        expected_message = "Welcome! Your random color is: red"
        
        app.print_welcome()
        mock_print.assert_called_once_with(expected_message)

    @patch('app.print_welcome')
    def test_main_calls_print_welcome(self, mock_print_welcome):
        """Test that main function calls print_welcome."""
        app.main()
        mock_print_welcome.assert_called_once()


if __name__ == "__main__":
    unittest.main()