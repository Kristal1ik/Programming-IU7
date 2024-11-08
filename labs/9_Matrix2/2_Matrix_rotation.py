"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 4
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений

"""



def mx_output(mx, name):
    print("-" * 20 + f"Матрица {name}" + "-" * 20)
    for i in mx:
        formatted_row = ''.join(f"{str(item):>{5}}" for item in i)
        print(formatted_row)


n = int(input("Введите размер квадратной матрицы: "))
while n <= 0:
    print("Длина размер матрицы должна быть больше 0!")
    n = int(input("Введите размер квадратной матрицы: "))
mx = [[0] * n for _ in range(n)]
print("Найчинайте заполнять матрицу: ")
for i in range(n):
    for j in range(n):
        mx[i][j] = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
mx_output(mx, "Исходная")
for layer in range(n // 2):
    first = layer
    last = n - layer - 1
    for i in range(first, last):
        offset = i - first
        top = mx[first][i]
        mx[first][i] = mx[last - offset][first]  # Левый -> Верхний
        mx[last - offset][first] = mx[last][last - offset]  # Нижний -> Левый
        mx[last][last - offset] = mx[i][last]  # Правый -> Нижний
        mx[i][last] = top  # Верхний -> Правый
mx_output(mx, "Промежуточная")
for layer in range(n // 2):
    first = layer
    last = n - layer - 1
    for i in range(first, last):
        offset = i - first  # Смещение относительно первого элемента
        left = mx[first][first + offset]
        mx[first][first + offset] = mx[i][last]  # Правый -> Верхний
        mx[i][last] = mx[last][last - offset]  # Нижний -> Правый
        mx[last][last - offset] = mx[last - i][first]  # Левый -> Нижний
        mx[last - i][first] = left  # Сохраненный левый -> Левый
mx_output(mx, "Итоговая")
