"""
This module is the solution for task 1 in lesson 14
Classes: Godzilla
"""


class Godzilla:
    """class Godzilla using to show how eat Godzilla
    methods: __init__(self, stomach_volume)
             eat(self, person_volume)"""

    def __init__(self, stomach_volume):
        """Godzilla Class Constructor to initialize the object.
           Argument can be int or float."""
        self.stomach_volume = stomach_volume
        self.stomach_fullness = 0
        self.eaten_up_msg = "Godzilla can't eat anymore"

    def eat(self, person_volume):
        """This method shows how Godzilla eating.
           Argument can be int or float"""
        if self.stomach_fullness <= 0.9 * self.stomach_volume:
            self.stomach_fullness += person_volume
        if self.stomach_fullness >= 0.9 * self.stomach_volume:
            print(self.eaten_up_msg)


if __name__ == '__main__':
    monster = Godzilla(100)
    monster.eat(85)
    monster.eat(6)
