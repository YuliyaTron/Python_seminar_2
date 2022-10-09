# 3) Задайте список (словарь не нужно выводить!) 
# из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


n = int(input('Введите число: '))
sum_numbers = 0
list_numbers = []

for i in range(1, n + 1):
    res = round(((1+1/i)**i), 2)
    list_numbers.append(res)
    sum_numbers += res

print(list_numbers)

print(sum_numbers)    



