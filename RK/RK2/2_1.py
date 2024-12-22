def matrix_output(matrix, name):
    print("-" * 20 + f"Матрица {name}" + "-" * 20)
    for i in matrix:
        formatted_row = ''.join(f"{str(item):>{5}}" for item in i)
        print(formatted_row)


mx = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
      [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
      [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
      [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
      [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
      [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
      [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
      [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
      [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]
n = m = len(mx)
matrix_output(mx, "Исходная")
print()
for layer in range(0, n // 2, 2):
    print(layer)
    first = layer
    last = n - layer - 1
    for i in range(first, last):
        offset = i - first
        top = mx[first][i]
        mx[first][i] = mx[last - offset][first]
        mx[last - offset][first] = mx[last][last - offset]
        mx[last][last - offset] = mx[i][last]
        mx[i][last] = top
# for layer in range(n // 2):
#     first = layer
#     last = n - layer - 1
#     for i in range(first, last):
#         offset = i - first  # Смещение относительно первого элемента
#         left = mx[first][first + offset]
#         mx[first][first + offset] = mx[i][last]  # Правый -> Верхний
#         mx[i][last] = mx[last][last - offset]  # Нижний -> Правый
#         mx[last][last - offset] = mx[last - i][first]  # Левый -> Нижний
#         mx[last - i][first] = left  # Сохраненный левый -> Левый
matrix_output(mx, "Перевернутая")

i = j = len(sp) - 2
step = len(sp) - 1
