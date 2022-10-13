"""
This module is the solution for task 1 in lesson 14
Classes: Godzilla
"""
import copy


class Godzilla:
    """class Godzilla using to show how eat Godzilla
    methods: __init__(self, stomach_volume)
             eat(self, person_volume)"""

    def __init__(self, stomach_volume):
        """Godzilla Class Constructor to initialize the object.
           Argument can be int or float."""
        self.stomach_volume = stomach_volume
        self.copy_stomach_volume = copy.deepcopy(self.stomach_volume)

    def eat(self, person_volume):
        """This method shows how Godzilla eating.
           Argument can be int or float"""
        empty_stomach_part = 0.1 * self.copy_stomach_volume
        self.stomach_volume -= person_volume
        if self.stomach_volume < empty_stomach_part:
            print('Godzilla can\'t eat anymore, it has eaten people')


if __name__ == '__main__':
    monster = Godzilla(100)
    monster.eat(85)
    monster.eat(6)

