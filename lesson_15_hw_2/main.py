"""This module run the program."""

import sys
from program.classes.run_program import RunProgram, ProgramError


def main():
    """Run the program."""
    run_program = RunProgram('товары.csv')
    run_program.choose_operation()
    run_program.show_program_result()
    while True:
        answer = input('Хотите сделать еще что нибудь? (y/n)')
        if answer == 'y':
            main()
        if answer == 'n':
            print("Завершение работы...")
            sys.exit()
        else:
            ProgramError('Вы ввели неправильный ответ,'
                         ' попробуйте еще раз.').print_error()


if __name__ == '__main__':
    main()
