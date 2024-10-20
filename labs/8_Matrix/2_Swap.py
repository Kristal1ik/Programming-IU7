"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 2
Перестановка  строки с наибольшим и наименьшим количеством отрицательных элементов.

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
max_neg_count = -1
min_neg_count = float('inf')
max_row_index = -1
min_row_index = -1
for i in range(n):
    neg_count = sum(1 for x in mx[i] if x < 0)
    if neg_count > max_neg_count:
        max_neg_count = neg_count
        max_row_index = i
    if neg_count < min_neg_count:
        min_neg_count = neg_count
        min_row_index = i
if max_row_index != -1 and min_row_index != -1:
    mx[max_row_index], mx[min_row_index] = mx[min_row_index], mx[max_row_index]

for row in mx:
    print(*row)
