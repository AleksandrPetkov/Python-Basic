"""This module is the solution for homework 1 for lesson 14
   classes: Point, Circle"""


class Point:
    """This class is the point which can be inside or outside circle
       methods: __init__(self, point_coord_x, point_coord_y)"""
    def __init__(self, point_coord_x, point_coord_y):
        """Point Class Constructor to initialize the object.
           Arguments can be int or float."""
        self.point_coord_x = point_coord_x
        self.point_coord_y = point_coord_y


class Circle:
    """This class is the circle
       methods: __init__(self, circle_coord_x, circle_coord_y, radius)
                point_in_circle(self, x=Point().point_coord_x, y=Point().point_coord_y)"""
    def __init__(self, circle_coord_x, circle_coord_y, radius):
        """Circle Class Constructor to initialize the object.
           Arguments can be int or float."""
        self.circle_coord_x = circle_coord_x
        self.circle_coord_y = circle_coord_y
        self.radius = radius

    def point_in_circle(self, point):
        """This method check, Point is inside or outside the Circle
           Arguments are objects of class Point"""
        return print((point.point_coord_x - self.circle_coord_x)**2
                     + (point.point_coord_y - self.circle_coord_y)**2 <= self.radius**2)


if __name__ == '__main__':
    obj_point = Point(6, 3)
    obj_circle = Circle(4, 3, 2)
    obj_circle.point_in_circle(obj_point)
