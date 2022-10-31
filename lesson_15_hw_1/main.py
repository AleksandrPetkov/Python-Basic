"""Settings to launch 'transport company' program."""
import sys
from lesson_15_hw_1.classes.class_transport_programm import TransportCompany
from lesson_15_hw_1.tests.test_vehicle import Test


def tests():
    """Test all classes used in the program."""
    test = Test()
    test.test_bus()
    test.test_train()
    test.test_plane()


def main():
    """Launch the 'transport company' program."""
    services = {'1': 'Пассажирские перевозки самолетом',
                '2': 'Пассажирские перевозки поездом',
                '3': 'Пассажирские перевозки автобусом',
                '4': 'Грузовые перевозки самолетом',
                '5': 'Грузовые перевозки поездом'
                }
    route_name_length = {'Одесса-Киев': {'train': 655, 'plane': 440, 'bus': 474},
                         'Одесса-Львов': {'train': 746, 'plane': 620, 'bus': 795},
                         'Одесса-Бухарест': {'train': 779, 'plane': 425, 'bus': 575},
                         'Одесса-Варшава': {'train': 1228, 'plane': 951, 'bus': 1180},
                         'Одесса-Кишинев': {'train': 189, 'plane': 150, 'bus': 180}
                         }
    dict_info_vehicles = {'train_pass': {'coef': 8.5, 'passengers': 630, 'speed': 60,
                                         'fuel': 160, 'fuel_price': 53.52},
                          'plane_pass': {'coef': 1.7, 'passengers': 140, 'speed': 500,
                                         'fuel': 2180, 'fuel_price': 90},
                          'train_cargo': {'coef': 15, 'cargo_space': 3000000, 'speed': 40,
                                          'fuel': 160, 'fuel_price': 53.52},
                          'plane_cargo': {'coef': 60, 'cargo_space': 120000, 'speed': 700,
                                          'fuel': 10300, 'fuel_price': 90},
                          'bus': {'coef': 4.3, 'passengers': 50, 'speed': 80,
                                  'fuel': 28, 'fuel_price': 53.52}
                          }
    company = TransportCompany(services, route_name_length, **dict_info_vehicles)
    company.begin()
    company.choose_service()
    company.vechicle_for_programm()
    company.choose_destination()
    company.route_length()
    company.run_calc_price()
    while True:
        answer = input("Хотели бы узнать еще что то (y/n)? ")
        if answer == 'y':
            company.choose_service()
            company.vechicle_for_programm()
            company.choose_destination()
            company.route_length()
            company.run_calc_price()
            continue
        if answer == 'n':
            print('До встречи!')
            sys.exit()
        else:
            print('Вы ввели неправильное значение, попробуйте еще раз!')
            continue


if __name__ == '__main__':
    tests()
    main()
