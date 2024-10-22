mx = []
n = int(input("Введите длину матрицы: "))
m = int(input("Введите ширину матрицы: "))
for i in range(n):
    mx_n = []
    for j in range(m):
        item = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
        mx_n.append(item)
    mx.append(mx_n)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if (sum(mx[j]) / len(mx[j])) < (sum(mx[min_index]) / len(mx[min_index])):
            min_index = j
    if min_index != i:
        mx[i], mx[min_index] = mx[min_index], mx[i]

print("Отсортированная матрица по среднему значению строк:")
for row in mx:
    formatted_row = ''.join(f"{str(item):>{5}}" for item in row)
    print(formatted_row)
