"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 2
Добавление удвоенного значения после положительного элемента

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
while index < len(lst):
    if lst[index] > 0:
        lst += [0]
        for j in range(len(lst) - 1, index, -1):
            lst[j] = lst[j-1]
        lst[index+1] = lst[index] * 2
        index += 1
    index += 1
print(f"Список с удаленными нечетными элементами: ")
for i in range(index):
    print(f"{i+1} элемент = {lst[i]}")
