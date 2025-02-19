"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 5
Получить матрицу С, равную произведению матриц А и В

"""


def matrix_output(matrix, name):
    print("-" * 20 + f"Матрица {name}" + "-" * 20)
    for i in matrix:
        formatted_row = ''.join(f"{str(item):>{5}}" for item in i)
        print(formatted_row)


n = int(input("Введите длину матрицы A: "))
while n <= 0:
    print("Длина матрицы должна быть больше 0!")
    n = int(input("Введите длину матрицы A: "))
m = int(input("Введите ширину матрицы A (она равна длине матрицы B): "))
while m <= 0:
    print("Значение должно быть больше 0!")
    m = int(input("Введите ширину матрицы A (она равна длине матрицы B): "))
k = int(input("Введите ширину матрицы B: "))
while k <= 0:
    print("Щирина матрицы должна быть больше 0!")
    k = int(input("Введите ширину матрицы B: "))

a = []
b = []
c = [[0] * k for _ in range(n)]

print("-" * 20 + "Заполнение матрицы A" + "-" * 20)
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input(f"Введите {j + 1} элемент {i + 1} строки: ")))
    a.append(row)

print("-" * 20 + "Заполнение матрицы B" + "-" * 20)
for i in range(m):
    row = []
    for j in range(k):
        row.append(int(input(f"Введите {j + 1} элемент {i + 1} строки: ")))
    b.append(row)

for i in range(n):  # по столбцам a
    for j in range(k):  # по строкам b
        for p in range(m):
            c[i][j] += a[i][p] * b[p][j]

matrix_output(a, "A")
matrix_output(b, "B")
matrix_output(c, "C, полученная путем перемножения A и B")
