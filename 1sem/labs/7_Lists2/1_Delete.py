"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 1
Удаление нечетных элементов из списка

"""

lst = []
n = int(input("Введите размер списка: "))
while n < 1:
    print("Некорректное значение! Чило должно быть > 0.")
    n = int(input("Введите размер списка: "))
for i in range(1, n + 1):
    number = int(input(f"Введите {i} элемент списка: "))
    lst.append(number)
print("-" * 45)

index = 0
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        lst[index] = lst[i]
        index += 1
lst = lst[:index]
print(f"Список с удаленными нечетными элементами: ")
for i in range(index):
    print(f"{i + 1} элемент = {lst[i]}")
