#  Пункт 3
lst = []
lst_extremes = []
n = int(input("Введите размер списка: "))
while n < 1:
    print("Некорректное значение! Чило должно быть > 0.")
    n = int(input("Введите размер списка: "))
for i in range(1, n + 1):
    number = int(input(f"Введите {i} элемент списка: "))
    lst.append(number)
print("-" * 45)
for i in range(1, n - 1):
    if (lst[i] > lst[i - 1] and lst[i] > lst[i + 1]) or (lst[i] < lst[i - 1] and lst[i] < lst[i + 1]):
        lst_extremes.append(lst[i])
k = int(input("Введите номер экстремума в списке (нумерация с 1): "))
while k > len(lst_extremes):
    print(f"Введено число, большее искомого количества точек экстремума, оно равно {len(lst_extremes)}!")
    k = int(input("Введите номер экстремума в списке (нумерация с 1): "))
print("-" * 45)
print(f"k-тый экстремум = {lst_extremes[k - 1]}")
