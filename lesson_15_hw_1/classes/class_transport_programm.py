"""This module creates a transport company help desk class using the Vehicle class"""
import sys
from lesson_15_hw_1.classes.class_vehicle import Train
from lesson_15_hw_1.classes.class_vehicle import Plain
from lesson_15_hw_1.classes.class_vehicle import Bus


class TransportCompany:
    """Creates a transport company help desk job.
    Uses imported subclasses of the Vehicle class to work.
    Methods: __init__(), begin(), choose_service (), vechicle_for_programm(),
    choose_destination(), route_length(), plain_price_time(),
    train_price_time(), plain_cargo_price_time(), train_cargo_price_time(),
    bus_price_time(), run_client_answer().
    """
    _cach_storage = {'chosen_service': '',
                     'chosen_vehicle': '',
                     'route_dict': {},
                     'destination': '',
                     'chosen_route_length': '',
                     'continue_answer': ''}

    def __init__(self, services_info, route_info, **vehicles_info):
        """Initiates the Transport Company class.
        Attributes: services_info, route_info, vehicles info
        """
        self.services_info = services_info
        self.route_info = route_info
        self.vehicles_info = vehicles_info

    def begin(self):
        """Starts communication with the client"""
        answer = input('Добрый день, хотели бы вы узнать подробнее о наших услугах (y/n):')
        if answer == 'y':
            routes = ','.join(list(self.route_info))
            print(f'Мы предоставляем пассажирские и грузо-перевозки '
                  f'по следующим направлениям:\n'
                  f'{routes}')
            return answer
        if answer == 'n':
            print('До встречи')
            sys.exit()
        else:
            print('Вы ввели неправильное значение, попробуйте еще раз!')
            self.begin()
        return None

    def choose_service(self):
        """Shows the list of services and
        receives the number of the service selected by the client.
        """
        print('О какой услуге вы бы хотели узнать подробнее(введите номер услуги):')
        for key, item in self.services_info.items():
            print(f'{key}:{item}')
        service = input()
        check_list_service = list(self.services_info.keys())
        if service in check_list_service:
            self._cach_storage['chosen_service'] = service
            return self._cach_storage
        else:
            print('Вы ввели неправильное значение, попробуйте еще раз!')
            self.choose_service()
        return None

    def vechicle_for_programm(self):
        """Intermediate function to return the key to a dictionary with distances"""
        train = ['2', '5']
        plain = ['1', '4']
        bus = ['3']
        if self._cach_storage['chosen_service'] in train:
            self._cach_storage['chosen_vehicle'] = 'train'
        elif self._cach_storage['chosen_service'] in plain:
            self._cach_storage['chosen_vehicle'] = 'plain'
        elif self._cach_storage['chosen_service'] in bus:
            self._cach_storage['chosen_vehicle'] = 'bus'
        return self._cach_storage

    def choose_destination(self):
        """Shows directions, accepts customer's choice,
        returns a list of destinations and customer selection
        """
        print('Выберите маршрут (введите номер направления):')
        route_dict = {}
        number = 1
        for key in self.route_info:
            route_dict[str(number)] = key
            print(f'{number}.{key}')
            number += 1
        destination = input()
        num_routes = list(range(1, len(self.route_info) + 1))
        check_list_service = list(map(str, num_routes))
        if destination in check_list_service:
            self._cach_storage['route_dict'], self._cach_storage['destination'] = route_dict, destination
            return self._cach_storage
        else:
            print('Вы ввели неправильное значение, попробуйте еще раз!')
            self.choose_destination()
        return None

    def route_length(self):
        """Calculates distance"""
        route_name = self._cach_storage['route_dict'].get(self._cach_storage['destination'])
        vehicle_key = self._cach_storage['chosen_vehicle']
        route_length = self.route_info.get(route_name).get(vehicle_key)
        self._cach_storage['chosen_route_length'] = route_length
        return self._cach_storage

    def plain_price_time(self):
        """Calculates the cost of a passenger plane ticket and travel time"""
        dict_info = self.vehicles_info['plain_pass']
        plain_info = list(dict_info.values())
        plain = Plain(*plain_info, self._cach_storage['chosen_route_length'])
        price = plain.make_price()
        travel_time = plain.calc_travel_time()
        return price, travel_time

    def train_price_time(self):
        """Calculates the cost of a passenger plane ticket and travel time"""
        dict_info = self.vehicles_info['train_pass']
        train_info = list(dict_info.values())
        train = Train(*train_info, self._cach_storage['chosen_route_length'])
        price = train.make_price()
        travel_time = train.calc_travel_time()
        return price, travel_time

    def plain_cargo_price_time(self):
        """Calculates the cost of 1 kg of cargo carried by plane and the travel time"""
        dict_info = self.vehicles_info['plain_cargo']
        plain_info = list(dict_info.values())
        plain = Plain(*plain_info, self._cach_storage['chosen_route_length'])
        price = plain.make_price()
        travel_time = plain.calc_travel_time()
        return price, travel_time

    def train_cargo_price_time(self):
        """Calculates the cost of 1 kg of cargo carried by train and the travel time"""
        dict_info = self.vehicles_info['train_cargo']
        train_info = list(dict_info.values())
        train = Train(*train_info, self._cach_storage['chosen_route_length'])
        price = train.make_price()
        travel_time = train.calc_travel_time()
        return price, travel_time

    def bus_price_time(self):
        """Calculates the cost of a passenger bus ticket and travel time"""
        dict_info = self.vehicles_info['bus']
        bus_info = list(dict_info.values())
        bus = Bus(*bus_info, self._cach_storage['chosen_route_length'])
        price = bus.make_price()
        travel_time = bus.calc_travel_time()
        return price, travel_time

    def run_calc_price(self):
        """Calculates the price of the selected service"""
        dict_def_calc = {'1': self.plain_price_time(),
                         '2': self.train_price_time(),
                         '3': self.bus_price_time(),
                         '4': self.plain_cargo_price_time(),
                         '5': self.train_cargo_price_time(),
                         }
        pass_vehicle = ['1', '2', '3']
        if self._cach_storage['chosen_service'] in pass_vehicle:
            price, travel_time = dict_def_calc[self._cach_storage['chosen_service']]
            print(f'Цена билета для одного пассажира {price}грн., '
                  f'ожидаемое время в пути(часы:минуты): {travel_time}')
        else:
            price, travel_time = dict_def_calc[self._cach_storage['chosen_service']]
            print(f'Цена перевозки 1 кг груза {price}грн., '
                  f'ожидаемое время в пути(часы:минуты): {travel_time}')

    def continue_work(self):
        answer = input("Хотели бы узнать еще что то (y/n)? ")
        if answer == 'y':
            self._cach_storage['continue_answer'] = '1'
            return self._cach_storage
        elif answer == 'n':
            self._cach_storage['continue_answer'] = '0'
            return self._cach_storage
        else:
            print('Вы ввели неправильное значение, попробуйте еще раз!')
            self.continue_work()
