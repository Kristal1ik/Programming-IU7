"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 4
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений

"""


def list_output(lst, name):
    print("-" * 20 + f"Список {name}" + "-" * 20)
    for i in range(len(lst)):
        print(f"Элемент {i + 1} = {lst[i]}")


n = int(input("Введите длину матрицы D: "))
while n <= 0:
    print("Длина матрицы должна быть больше 0!")
    n = int(input("Введите длину матрицы D: "))
m = int(input("Введите ширину матрицы D: "))
while m <= 0:
    print("Значение должно быть больше 0!")
    m = int(input("Введите ширину матрицы D: "))

d = [[0] * m for _ in range(n)]
print("Найчинайте заполнять матрицу D: ")
for i in range(n):
    for j in range(m):
        d[i][j] = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
lst = []
lst_length = int(input("Введите длину списка I: "))
while lst_length <= 0:
    print("Длина списка должна быть больше 0!")
    lst_length = int(input("Введите длину списка I: "))
print(
    "Найчинайте заполнять список L (учтите, что элемент списка не может быть больше длины матрицы D, нумерация с 1): ")
for i in range(lst_length):
    item = int(input(f"Введите {i + 1} элемент списка: "))
    while item <= 0 or item > n:
        print("Элемент должен быть больше нуля и меньше или равен длины матрицы")
        item = int(input(f"Введите {i + 1} элемент списка: "))
    lst.append(item)

#  Среднее значение
r = []
for i in range(n):
    if i + 1 in lst:
        r.append(max(d[i]))
if r:
    average_value = sum(r) / len(r)
else:
    average_value = 0

#  Вывод
d_name = "D"
print("-" * 20 + f"Матрица {d_name}" + "-" * 20)
for i in d:
    formatted_row = ''.join(f"{str(item):>{5}}" for item in i)
    print(formatted_row)
list_output(lst, "I")
list_output(r, "R")
print(f"Среднее значение = {average_value:5f}")
