"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 7
Ввести трёхмерный массив (массив матриц размера X*Y*Z). Вывести срез
массива по большему измерению, индекс среза – середина размерности с
округлением в меньшую сторону .

"""

n = int(input("Введите длину матрицы (количество строк): "))
while n <= 0:
    print("Длина матрицы должна быть больше 0!")
    n = int(input("Введите длину матрицы: "))

m = int(input("Введите ширину матрицы (количество столбцов): "))
while m <= 0:
    print("Ширина должна быть больше 0!")
    m = int(input("Введите ширину матрицы: "))

k = int(input("Введите глубину матрицы (количество слоев): "))
while k <= 0:
    print("Глубина должна быть больше 0!")
    k = int(input("Введите глубину матрицы: "))

# Создание трехмерного массива
mx = []
for i in range(k):
    layer = []
    for j in range(n):
        row = list(map(int, input(f"Введите элементы строки {j + 1} для слоя {i + 1} (через пробел): ").split()))
        while len(row) != m:
            print(f"Ошибка: ожидается {m} элементов. Пожалуйста, введите снова.")
            row = list(map(int, input(f"Введите элементы строки {j + 1} для слоя {i + 1} (через пробел): ").split()))
        layer.append(row)
    mx.append(layer)

# Вывод трехмерного массива
print("\nТрехмерный массив:")
for layer in mx:
    print(layer)
    print()

max_side = max(n, m, k)
slice_index = (max_side - 1) // 2

# Срез по большему измерению
if max_side == n:
    slice_result = [layer[slice_index] for layer in mx]  # Срез по строкам
elif max_side == m:
    slice_result = [[layer[i][slice_index] for i in range(n)] for layer in mx]  # Срез по столбцам
else:
    slice_result = mx[slice_index]  # Срез по слоям

print(f"Срез по большему измерению (индекс {slice_index}):")
for row in slice_result:
    print(row)
