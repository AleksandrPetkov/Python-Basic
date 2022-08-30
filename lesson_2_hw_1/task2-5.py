import math
from art import *
from decimal import Decimal


name0 = text2art("sasha", "tarty1")
print(name0)

a = 1
b = 5
c = 4
x1 = (-b+(math.sqrt(b**2-4*a*c)))/(2*a)
x2 = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
print("Решение задачи x1=", x1)
print("Решение задачи x2=", x2)

print("Введите ваше имя:")
name = input()
print("Привет,", name, "!")
print("Вы хотите обменять гривны на доллары? (да/нет)")
b = input()
print("Сколько вы хотите обменять?") if b == "да" else print("До свидания!")
c = Decimal(input())
exchange = Decimal(39.5)
print("По курсу валют на 25.08.22 1 доллар США стоит", exchange, ", вы получите", format(c/exchange, '.3f'))
