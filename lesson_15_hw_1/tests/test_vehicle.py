"""testing class Vehicle"""
from lesson_15_hw_1.classes.class_vehicle import Train
from lesson_15_hw_1.classes.class_vehicle import Plain
from lesson_15_hw_1.classes.class_vehicle import Bus


def test_train():
    """testing child class Train"""
    train = Train(1.5, 500, 120, 7.6, 53, 700)
    assert train.calc_travel_minutes() == 350, "Mistake in parent class Vehicle"
    assert train.calc_travel_time() == '5:50', "Mistake in parent class Vehicle"
    assert train.make_price() == '8.46', "Mistake in child class Train"


def test_bus():
    """testing child class Bus"""
    bus = Bus(1.5, 500, 150, 7.6, 55, 700)
    assert bus.calc_travel_minutes() == 280, "Mistake in parent class Vehicle"
    assert bus.calc_travel_time() == '4:40', "Mistake in parent class Vehicle"
    assert bus.make_price() == '8.78', "Mistake in child class Train"


def test_plain():
    """testing child class Plain"""
    plain = Plain(1.5, 500, 170, 10, 55, 700)
    assert plain.calc_travel_minutes() == 247, "Mistake in parent class Vehicle"
    assert plain.calc_travel_time() == '4:7', "Mistake in parent class Vehicle"
    assert plain.make_price() == '6.79', "Mistake in child class Train"
