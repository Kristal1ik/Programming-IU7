"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 3
Нахождение столбца с наибольшм количество нулевых элементов.

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

mx_zeros = -1
mx_col_index = -1

for j in range(m):
    zero_count = 0
    for i in range(n):
        if mx[i][j] == 0:
            zero_count += 1
    if zero_count > mx_zeros:
        max_zeros = zero_count
        max_col_index = j
print(f"Столбец с наибольшим количеством нулей: {mx_col_index + 1}, количество нулей: {mx_zeros}")
