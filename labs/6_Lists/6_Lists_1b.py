"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 1b
Добавление элемента в заданное место алгоритмически.

"""

lst = []
while True:
    n = int(input('Введите изначальное количество элементов списка: '))
    if n < 0:
        print("Количество должно быть числом положительным, друг")
    else:
        break
for i in range(1, n + 1):
    lst.append(int(input(f"Введите {i} элемент списка: ")))
while True:
    pos = int(input("Введите индекс вставки нового элемента: "))
    if not 0 <= pos <= n:
        print(f"Значение индекса должно быть от 0 до {n}!")
    else:
        break
element = int(input("Введите элемент для вставки: "))
lst.append(None)
for i in range(n, pos, -1):
    lst[i] = lst[i - 1]
lst[pos] = element
print("-" * 45)
print("Новый список: ")
for i in range(1, n + 2):
    print(f"{i} элемент = {lst[i - 1]}")
