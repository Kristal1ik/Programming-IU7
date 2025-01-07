array = [6, 43, 2, 1, 2, 1, 1, 1, 1, 6, 7, 8]
n = len(array)

for i in range(n):
    for j in range(n - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print("Отсортированный массив:", array)