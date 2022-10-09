# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число: ')

newnumber = 10 ** (len(number)-2)
number = int(float(number)*newnumber)

res = 0
while number != 0:
    res += number % 10
    number //= 10      
print(res)

