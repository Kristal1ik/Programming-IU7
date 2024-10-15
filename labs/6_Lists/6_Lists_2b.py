#  Пункт 2b
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
while ind >= n or ind < 0:
    print(f"Введенный индекс выходит за пределы диапазона! Размер списка = {n}, индексация с нуля. Индекс должен быть больше 0")
    ind = int(input("Из какого места хотите удалить элемент? (индекс, индексация с нуля): "))

for i in range(ind + 1, len(lst)):
    lst[i - 1] = lst[i]

lst[len(lst) - 1] = None
del lst[len(lst) - 1]
print("-" * 45)
print(f"Удален {ind} элемент")
print("Новый список: ")
for i in range(1, n):
    print(f"{i} элемент = {lst[i - 1]}")
