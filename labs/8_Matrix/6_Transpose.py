"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 6
Транспонирование матрицы

"""
mx = []
n = int(input("Введите размерноать квадратной матрицы: "))

for i in range(n):
    mx_n = []
    for j in range(n):
        item = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
        mx_n.append(item)
    mx.append(mx_n)
for i in range(n):
    for j in range(i + 1, n):
        mx[i][j], mx[j][i] = mx[j][i], mx[i][j]
for row in mx:
    print(*row)
