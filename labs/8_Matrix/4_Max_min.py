"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 4
Перестановка столбцов с максимальной и минимальной суммой элементов.

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

max_sum = float('-inf')
min_sum = float('inf')
max_col_index = -1
min_col_index = -1

for j in range(m):
    col_sum = sum(mx[i][j] for i in range(n))
    if col_sum > max_sum:
        max_sum = col_sum
        max_col_index = j

    if col_sum < min_sum:
        min_sum = col_sum
        min_col_index = j
for i in range(n):
    mx[i][max_col_index], mx[i][min_col_index] = mx[i][min_col_index], mx[i][max_col_index]

for row in mx:
    print(*row)
