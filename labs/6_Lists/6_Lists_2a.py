"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 2a
Удаление элеманта с заданным индексом с использованием любых средств Python.

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
ind = int(input("Из какого места хотите удалить элемент? (индекс, индексация с нуля): "))
while not (0 <= ind <= n):
    print(f"Введенный индекс выходит за пределы диапазона! Размер списка = {n}, индексация с нуля.")
    ind = int(input("Из какого места хотите удалить элемент? (индекс, индексация с нуля): "))

lst.pop(ind)
print("-" * 45)
print(f"Удален {ind} элемент")
print("Новый список: ")
for i in range(1, n):
    print(f"{i} элемент = {lst[i - 1]}")