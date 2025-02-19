"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 1
Определить количество полных квадратов в каждой строке матрицы. Записать значения в массив S

"""

import math

n = int(input("Введите длину списков: A, B: "))
a = []
b = []
mx = [[0] * n for _ in range(n)]
s = [0] * n
width = 5
while n <= 0:
    print("Длина должна быть больше 0!")
    n = int(input("Введите длину списков: A, B"))
print("Начнинайте вводить элементы списка A: ")
for i in range(n):
    a.append(int(input()))
print("Начнинайте вводить элементы списка B: ")
for i in range(n):
    b.append(int(input()))
for i in range(n):
    for j in range(n):
        item = a[i] * b[j]
        mx[i][j] = item
        if item == math.isqrt(item) ** 2:  # isqrt() -- корень без десятичной части
            print(item)
            s[i] += 1
for i in range(n):
    row_str = "".join(str(mx[i][j]).ljust(width) for j in range(n))
    if i < n:
        row_str += "| " + str(s[i]).rjust(width)
    print(row_str)
