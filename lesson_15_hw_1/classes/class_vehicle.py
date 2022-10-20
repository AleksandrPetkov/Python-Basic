"""Parent class Vehicle, subclasses: Train, Plain, Bus"""
from decimal import Decimal


class Vehicle:
    """A general class that combines the attributes of vehicles
     methods: __init__()
             calc_travel_minutes()
             calc_travel_time()
    """
    def __init__(self, avr_speed, avr_fuel_consumption, fuel_price,  distance):
        """Specifies the main attributes of the class.
         Attributes: average speed, average fuel consumption per 100 km,
         price per 1 liter of fuel, distance traveled
        """
        self.avr_speed = avr_speed
        self.avr_fuel_consumption = avr_fuel_consumption
        self.fuel_price = fuel_price
        self.distance = distance

    def calc_travel_minutes(self):
        """Calculates the vehicle's expected travel time in minutes"""
        minutes_in_hour = 60
        full_time_minutes = int(self.distance / (self.avr_speed / minutes_in_hour))
        return full_time_minutes

    def calc_travel_time(self):
        """Calculates the expected travel time of the vehicle,
        in the form hours:minutes
        """
        minutes_in_hour = 60
        hours = int(self.calc_travel_minutes() // minutes_in_hour)
        minutes = int(self.calc_travel_minutes() % minutes_in_hour)
        travel_time = f'{hours}:{minutes}'
        return travel_time


class Train(Vehicle):
    """Подкласс Vehicle, поезд
    методы: __init__()
            fuel_passenger()
    """
    def __init__(self, coef_costs, max_capacity, *args):
        """Specifies the main attributes of the subclass.
         Attributes: all attributes of the parent Vehicle class,
         maximum capacity and cost factor.
        """
        super().__init__(*args)
        self.coef_costs = coef_costs  # коэфициент затрат (амортизация, зарплата, пр.)
        self.max_capacity = max_capacity  # общая вместимость

    def make_price(self):
        """Calculates the price for 1 unit of transported."""
        fuel_costs_liters = self.distance * self.avr_fuel_consumption / 100
        fuel_costs_money = fuel_costs_liters * self.fuel_price
        unrounded_price = (Decimal((fuel_costs_money / self.max_capacity) * self.coef_costs))
        price = str(unrounded_price.quantize(Decimal('1.00')))
        return price


class Plain(Vehicle):
    """Vehicle subclass, aircraft
    methods: __init__()
            fuel_passenger()
    """
    def __init__(self, coef_costs, max_capacity, *args):
        """Specifies the main attributes of the subclass.
         Attributes: all attributes of the parent Vehicle class,
         maximum capacity.
        """
        super().__init__(*args)
        self.coef_costs = coef_costs  # коэфициент затрат (амортизация, зарплата, пр.)
        self.max_capacity = max_capacity  # общая вместимость

    def make_price(self):
        """Calculates the price for 1 unit of transported."""
        fuel_costs_liters = self.calc_travel_minutes() * self.avr_fuel_consumption / 60
        fuel_costs_money = fuel_costs_liters * self.fuel_price
        unrounded_price = (Decimal((fuel_costs_money / self.max_capacity) * self.coef_costs))
        price = str(unrounded_price.quantize(Decimal('1.00')))
        return price


class Bus(Vehicle):
    """Subclass Vehicle, bus
     methods: __init__()
             fuel_passenger()
    """
    def __init__(self, coef_costs, max_passengers, *args):
        """Defines the main attributes of the subclass
         attributes: all attributes of the parent Vehicle class,
         maximum passenger capacity
        """
        super().__init__(*args)
        self.coef_costs = coef_costs  # коэфициент затрат (амортизация, зарплата, пр.)
        self.max_capacity = max_passengers  # общая вместимость

    def make_price(self):
        """Calculates the price for 1 passenger"""
        fuel_costs_liters = self.distance * self.avr_fuel_consumption / 100
        fuel_costs_money = fuel_costs_liters * self.fuel_price
        unrounded_price = (Decimal((fuel_costs_money / self.max_capacity) * self.coef_costs))
        price = str(unrounded_price.quantize(Decimal('1.00')))
        return price
