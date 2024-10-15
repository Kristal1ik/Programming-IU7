lst = []
n = int(input("Введите размер списка: "))
while n < 1:
    print("Некорректное значение! Чило должно быть > 0.")
    n = int(input("Введите размер списка: "))
for i in range(1, n + 1):
    number = int(input(f"Введите {i} элемент списка: "))
    lst.append(number)
print("-" * 45)
while True:
    k = int(input("Введите номер экстремума: "))
    if not 1 <= k < n:
        print(f"Номер экстремума должен быть от больше нуля")
    else:
        break
occurrences = 0
for i in range(1, n - 1):
    if lst[i - 1] < lst[i] > lst[i + 1] or lst[i - 1] > lst[i] < lst[i + 1]:
        occurrences += 1
        if occurrences == k:
            print(f"K-й экстремум: {lst[i]} на индексе {i}")
            break
else:
    print("В списке меньше K экстремумов:(")