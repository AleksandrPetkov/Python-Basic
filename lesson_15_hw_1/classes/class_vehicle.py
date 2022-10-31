"""Parent class Vehicle, subclasses: Train, Plain, Bus."""

from decimal import Decimal


class Vehicle:
    """A general class that combines the attributes of vehicles.

    Methods: __init__(),
             calc_travel_minutes(),
             calc_travel_time().
    """

    def __init__(self, avr_speed, avr_fuel_consumption, fuel_price,  distance):
        """Specify the main attributes of the class.

        Attributes: average speed,
        average fuel consumption per 100 km,
        price per 1 liter of fuel,
        distance traveled.
        """
        self.avr_speed = avr_speed
        self.avr_fuel_consumption = avr_fuel_consumption
        self.fuel_price = fuel_price
        self.distance = distance

    def calc_travel_minutes(self):
        """Calculate the vehicle's expected travel time in minutes."""
        minutes_in_hour = 60
        full_time_minutes = int(self.distance / (self.avr_speed / minutes_in_hour))
        return full_time_minutes

    def print_travel_time(self):
        """Calculate the expected travel time of the vehicle.

        Form of calculted time is hours:minutes.
        """
        travel_minutes = self.calc_travel_minutes()
        minutes_in_hour = 60
        hours = int(travel_minutes // minutes_in_hour)
        minutes = int(travel_minutes % minutes_in_hour)
        travel_time = f'{hours}:{minutes}'
        return travel_time


class Train(Vehicle):
    """Child class Vehicle.

    Methods: __init__(),
            fuel_passenger().
    """

    def __init__(self, coef_costs, max_capacity, *args):
        """Specify the main attributes of the subclass.

        Attributes: all attributes of the parent Vehicle class,
        maximum capacity and cost factor.
        """
        super().__init__(*args)
        self.coef_costs = coef_costs  # коэфициент затрат (амортизация, зарплата, пр.)
        self.max_capacity = max_capacity  # общая вместимость

    def make_price(self):
        """Calculate the price for 1 unit of transported."""
        fuel_costs_liters = self.distance * self.avr_fuel_consumption / 100
        fuel_costs_money = fuel_costs_liters * self.fuel_price
        unrounded_price = (Decimal((fuel_costs_money / self.max_capacity) * self.coef_costs))
        price = unrounded_price.quantize(Decimal('1.00'))
        return price


class Plane(Vehicle):
    """Vehicle subclass.

    Methods: __init__(),
            fuel_passenger().
    """

    def __init__(self, coef_costs, max_capacity, *args):
        """Specify the main attributes of the subclass.

        Attributes: all attributes of the parent Vehicle class,
        maximum capacity.
        """
        super().__init__(*args)
        self.coef_costs = coef_costs  # коэфициент затрат (амортизация, зарплата, пр.)
        self.max_capacity = max_capacity  # общая вместимость

    def make_price(self):
        """Calculate the price for 1 unit of transported."""
        fuel_costs_liters = self.calc_travel_minutes() * self.avr_fuel_consumption / 60
        fuel_costs_money = fuel_costs_liters * self.fuel_price
        unrounded_price = (Decimal((fuel_costs_money / self.max_capacity) * self.coef_costs))
        price = unrounded_price.quantize(Decimal('1.00'))
        return price


class Bus(Vehicle):
    """Subclass Vehicle.

    Methods: __init__(),
             fuel_passenger().
    """

    def __init__(self, coef_costs, max_passengers, *args):
        """Define the main attributes of the subclass.

        Attributes: all attributes of the parent Vehicle class,
        maximum passenger capacity.
        """
        super().__init__(*args)
        self.coef_costs = coef_costs  # коэфициент затрат (амортизация, зарплата, пр.)
        self.max_capacity = max_passengers  # общая вместимость

    def make_price(self):
        """Calculate the price for 1 passenger."""
        fuel_costs_liters = self.distance * self.avr_fuel_consumption / 100
        fuel_costs_money = fuel_costs_liters * self.fuel_price
        unrounded_price = (Decimal((fuel_costs_money / self.max_capacity) * self.coef_costs))
        price = unrounded_price.quantize(Decimal('1.00'))
        return price
