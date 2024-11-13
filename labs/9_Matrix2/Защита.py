n = int(input("Введите длину матрицы: "))
while n <= 0:
    print("Длина матрицы должна быть больше 0!")
    n = int(input("Введите длину матрицы: "))
m = int(input("Введите ширину матрицы: "))
while m <= 0:
    print("Ширина матрицы должна быть больше 0!")
    m = int(input("Введите ширину матрицы: "))
mx = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        item = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
        mx[i][j] = item

min_indexes = [0, 0]
max_indexes = [0, 0]
min_item = mx[0][0]
max_item = mx[0][0]

for i in range(n):
    for j in range(m):
        if mx[i][j] < min_item:
            min_item = mx[i][j]
            min_indexes[0], min_indexes[1] = i, j
        if mx[i][j] > max_item:
            max_item = mx[i][j]
            max_indexes[0], max_indexes[1] = i, j

row_start = min(min_indexes[0], max_indexes[0])
row_end = max(min_indexes[0], max_indexes[0])
col_start = min(min_indexes[1], max_indexes[1])
col_end = max(min_indexes[1], max_indexes[1])

mini_mx = []
for i in range(row_start, row_end + 1):
    row = []
    for j in range(col_start, col_end + 1):
        row.append(mx[i][j])
    mini_mx.append(row)

positives = []
for row in mini_mx:
    for value in row:
        if value > 0:
            positives.append(value)
average_positive = sum(positives) / len(positives)

print("Исходная матрица:")
for row in mx:
    print(row)

print("Подматрица:")
for row in mini_mx:
    print(row)

print(f"Среднее арифметическое положительных элементов подматрицы: {average_positive:.2f}")