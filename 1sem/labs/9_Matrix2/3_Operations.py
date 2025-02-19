"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 3
Подсчитать для каждого столбца матрицы А количество элементов, больших
среднего арифметического элементов соответствующего столбца матрицы В.
Вывести полученные значения. Затем преобразовать матрицу В путем
умножения всех элементов столбца матрицы на посчитанное для этого столбца
значение, если оно ненулевое.

"""


def matrix_output(matrix, name):
    print("-" * 20 + f" Матрица {name} " + "-" * 20)
    for i in matrix:
        formatted_row = ''.join(f"{str(item):>{5}}" for item in i)
        print(formatted_row)


n = int(input("Введите длину матрицы A: "))
while n <= 0:
    print("Длина матрицы должна быть больше 0!")
    n = int(input("Введите длину матрицы A: "))
k = int(input("Введите длину матрицы B: "))
while k <= 0:
    print("Длина матрицы должна быть больше 0!")

m = int(input("Введите ширину матриц A и B: "))
while m <= 0:
    print("Ширина матриц должна быть больше 0!")
    m = int(input("Введите длину матриц A и B: "))
a = []
b = []
middles = [0] * m

print("-" * 20 + "Заполнение матрицы A" + "-" * 20)
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"Введите {j + 1} элемент {i + 1} строки: ")))
    a.append(row)

print("-" * 20 + "Заполнение матрицы B" + "-" * 20)
for i in range(k):
    row = []
    for j in range(m):
        row.append(int(input(f"Введите {j + 1} элемент {i + 1} строки: ")))
    b.append(row)

for j in range(m):
    sum_row = 0
    for i in range(k):
        middles[j] += b[i][j]
    middles[j] /= k
print("Средние арифметические по столбцам матрицы B:", middles)
counter_more_then_middle_lst = []
for j in range(m):
    counter = 0
    for i in range(n):
        if a[i][j] > middles[j]:
            counter += 1
    counter_more_then_middle_lst.append(counter)
    print(
        f"В {j + 1} столбце {counter} элементов больше соответствующего знаечения среднего арифметического элементов "
        f"соответствующего столбца матрицы В")
for i in range(m):
    if counter_more_then_middle_lst[i] != 0:
        for j in range(k):
            b[i][j] *= counter_more_then_middle_lst[j]

matrix_output(b, "Преобразованная матрица B")
