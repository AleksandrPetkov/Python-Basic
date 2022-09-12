import random

user_number = int(input('Please enter your number from 1 to 10: '))
while True:
    hidden_number = random.randint(1, 3)
    if user_number == hidden_number:
        print('Congratulations, you guessed the number!!!')
        break
    else:
        choice = input('Do you want to try again, enter y/n:')
        if choice == 'n':
            print('Goodbye!')
            break
        elif choice != 'n' and choice != 'y':
            print('You enter the wrong answer!')
            continue
        else:
            choice_2 = input('Do you want continue to guess or computer can try to guess your number,'
                             'enter "i" - you want to continue, "c" - computer try to guess:')
            if choice_2 == 'i':
                user_number = int(input('Please enter your number from 1 to 10: '))
                continue
            elif choice_2 != 'i' and choice_2 != 'c':
                print('You enter the wrong answer!')
                continue
            else:
                comp_number = random.randint(1, 10)
                comp_range = [*range(1, 11)]
                mid = len(comp_range) // 2
                low = 1
                high = len(comp_range)
                print('Am I guess your number, enter y/n?', mid)
                user_answer = input()
                if user_answer == 'y':
                    print('I am guess your number!!!')
                    break
                else:
                    while mid != comp_number and low <= high:
                        user_answer_2 = input('Is your number less or bigger than mine, enter less/bigger:')
                        if user_answer_2 == 'bigger':
                            low = mid + 1
                        elif user_answer_2 != 'bigger' and user_answer_2 != 'less':
                            print('You enter the wrong answer!')
                            continue
                        else:
                            high = mid - 1
                        mid = (low + high) // 2
                        if low > high:
                            print('No value')
                        else:
                            print('Am I guess your number, enter y/n?', mid)
                            user_answer2 = input()
                            if user_answer2 == 'n':
                                continue
                            if user_answer2 == 'y':
                                print('I am guess your number!!!')
                                break
        break
