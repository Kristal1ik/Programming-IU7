"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б
Вариант 10

Пункт 5
Смена мест последнего четного и минимального положительного элементов.

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
last_even = 0
last_even_index = 0
min_pos = max(lst)
min_pos_index = 0
for i in range(len(lst)):
    if 0 < lst[i] < min_pos:
        min_pos = lst[i]
        print(min_pos)
        min_pos_index = i
    if lst[i] % 2 == 0:
        last_even = lst[i]
        last_even_index = i
lst[min_pos_index], lst[last_even_index] = lst[last_even_index], lst[min_pos_index]
print(lst)
