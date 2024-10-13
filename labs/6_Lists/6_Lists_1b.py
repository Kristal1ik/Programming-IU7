#  Пункт 1а
lst = []
n = int(input("Введите размер списка: "))
while n < 1:
    print("Некорректное значение! Чило должно быть > 0.")
    n = int(input("Введите размер списка: "))
for i in range(1, n + 1):
    number = int(input(f"Введите {i} элемент списка: "))
    lst.append(number)
print("-" * 45)
ind = int(input("В какое место хотите добавить элемент? (индекс, индексация с нуля): "))
while ind >= n:
    print(f"Введенный индекс выходит за пределы диапазона! Размер списка = {n}, индексация с нуля.")
    ind = int(input("В какое место хотите добавить элемент? (индекс, индексация с нуля): "))

number = int(input(f"Введите число, которое хотите добавить в заданное место ({ind}): "))
lst_new = []
for i in range(n):
    if i == ind:
        lst_new.append(number)
    else:
        lst_new.append(lst[i])
print("-" * 45)
print("Новый список: ")
for i in range(1, n + 1):
    print(f"{i} элемент = {lst_new[i - 1]}")
