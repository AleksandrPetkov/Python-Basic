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

    def eat(self, person_volume):
        """This method shows how Godzilla eating.
           Argument can be int or float"""
        eating = self.stomach_fullness + person_volume
        if eating > 0.9 * self.stomach_volume:
            self.stomach_fullness = eating - (eating - 0.9*self.stomach_volume)
            print("Godzilla can't eat anymore")
        else:
            self.stomach_fullness += person_volume


if __name__ == '__main__':
    monster = Godzilla(100)
    monster.eat(120)
    monster.eat(6)
    monster.eat(100)



