print('This program will answer the question: "Is your year high?"')
user_num = int(input('Please, enter four-digit number: '))
mod_4 = user_num % 4
mod_100 = user_num % 100
mod_400 = user_num % 400
if mod_4 == 0 and mod_100 != 0 or mod_400 == 0:
    print('YES')
else:
    print('NO')
