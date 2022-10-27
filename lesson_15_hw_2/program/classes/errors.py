"""
This module is responsible for displaying errors for the user in case of incorrect actions.

class: ProgrammError.
"""


class ProgramError:
    """This class have 1 method which input the text of mistake and print it."""

    def __init__(self, message):
        """Initialize class ProgramError and arguments of the class."""
        self.message = message

    def print_error(self):
        """Print the mistake for user."""
        print(f'Ошибка: {self.message}')
