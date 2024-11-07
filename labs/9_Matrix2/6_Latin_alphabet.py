"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 6
Заменить все согласные латинские букв на заглавные, а все гласные латинские буквы на строчные.

"""


def matrix_output(matrix, name):
    print("-" * 20 + f"Матрица {name}" + "-" * 20)
    for i in matrix:
        formatted_row = ''.join(f"{str(item):>{5}}" for item in i)
        print(formatted_row)


mx = []
n = int(input("Введите длину матрицы: "))
while n <= 0:
    print("Длина матрицы должна быть больше 0!")
    n = int(input("Введите длину матрицы: "))

m = int(input("Введите ширину матрицы: "))
while m <= 0:
    print("Ширина матрицы должна быть больше 0!")
    m = int(input("Введите ширину матрицы: "))

for i in range(n):
    mx_n = []
    for j in range(m):
        item = int(input(f"Введите {j + 1} элемент {i + 1} строки: "))
        mx_n.append(item)
    mx.append(mx_n)
new_mx = []
vowels = "aeiouAEIOU"
consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for i in mx:
    new_mx.append([lambda char: char.lower() if char in vowels else char.upper() if char in consonant else char])

matrix_output(mx, "Введенная матрица")
matrix_output(new_mx, "Преобразованная матрица")
