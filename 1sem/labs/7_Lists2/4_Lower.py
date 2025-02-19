"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 4
Замена всех заглавных гласных английских букв на строчные

"""

lst = []
n = int(input("Введите размер списка: "))
elem_answer = ""

while n < 1:
    print("Некорректное значение! Чило должно быть > 0.")
    n = int(input("Введите размер списка: "))
for i in range(1, n + 1):
    number = input(f"Введите {i} элемент списка: ")
    lst.append(number)
print("-" * 45)

for i in range(n):
    lst[i] = lst[i].replace("A", "a")
    lst[i] = lst[i].replace("E", "e")
    lst[i] = lst[i].replace("I", "i")
    lst[i] = lst[i].replace("O", "o")
    lst[i] = lst[i].replace("U", "u")
print(f"Список с измененными гласными буквами: ")
for i in range(len(lst)):
    print(f"{i + 1} элемент = {lst[i]}")
