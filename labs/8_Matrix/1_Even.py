"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 1
Нахождение строки матрицы с наибольшим количеством четных элементов

"""
mx = []
n = int(input("Введите длину матрицы: "))
m = int(input("Введите ширину матрицы: "))
for i in range(n):
    mx_n = []
    for j in range(m):
        item = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
        mx_n.append(item)
    mx.append(mx_n)
mx_odd = 0
mx_str = ""
for i in range(n):
    mx_odd_now = 0
    for j in range(m):
        if mx[i][j] % 2 == 0:
            mx_odd_now += 1
    if mx_odd_now > mx_odd:
        mx_odd = mx_odd_now
        mx_str = mx[i]
print(*mx_str)
