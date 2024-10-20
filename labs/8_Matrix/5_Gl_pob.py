"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 5
Нахождение максимального значения в квадратной матрице над главной диагональю и минимальное - под побочной диагональю.

"""
mx = []
n = int(input("Введите размерноать квадратной матрицы: "))

for i in range(n):
    mx_n = []
    for j in range(n):
        item = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
        mx_n.append(item)
    mx.append(mx_n)

max_value = float('-inf')
min_value = float('inf')

# Поиск максимума над главной диагональю
for i in range(n):
    for j in range(i + 1, n):
        if mx[i][j] > max_value:
            max_value = mx[i][j]

# Поиск минимума под побочной диагональю
for i in range(n):
    for j in range(n - i - 1):
        if mx[i][j] < min_value:
            min_value = mx[i][j]

print(f"Максимальное значение над главной диагональю: {max_value}")
print(f"Минимальное значение под побочной диагональю: {min_value}")
