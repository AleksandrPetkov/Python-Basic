"""Test class Vehicle."""
from decimal import Decimal

from lesson_15_hw_1.classes.class_vehicle import Train
from lesson_15_hw_1.classes.class_vehicle import Plane
from lesson_15_hw_1.classes.class_vehicle import Bus


class Test:
    def test_train(self):
        """Test child class Train."""
        train = Train(1.5, 500, 120, 7.6, 53, 700)
        assert train.calc_travel_minutes() == 350, "Mistake in parent class Vehicle"
        assert train.print_travel_time() == '5:50', "Mistake in parent class Vehicle"
        assert train.make_price() == Decimal(8.46).quantize(Decimal('1.00')), "Mistake in child class Train"

    def test_bus(self):
        """Test child class Bus."""
        bus = Bus(1.5, 500, 150, 7.6, 55, 700)
        assert bus.calc_travel_minutes() == 280, "Mistake in parent class Vehicle"
        assert bus.print_travel_time() == '4:40', "Mistake in parent class Vehicle"
        assert bus.make_price() == Decimal(8.78).quantize(Decimal('1.00')), "Mistake in child class Train"

    def test_plane(self):
        """Test child class Plane."""
        plane = Plane(1.5, 500, 170, 10, 55, 700)
        assert plane.calc_travel_minutes() == 247, "Mistake in parent class Vehicle"
        assert plane.print_travel_time() == '4:7', "Mistake in parent class Vehicle"
        assert plane.make_price() == Decimal(6.79).quantize(Decimal('1.00')), "Mistake in child class Train"


