"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Пункт 3
Поиск элемента с наибольшим числом английских гласных букв

"""

vowels = "aeiou"
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

for i in lst:
    counter = 0
    for j in i.lower():
        if j in vowels:
            counter += 1
    if counter > len(elem_answer):
        elem_answer = i
print(f"Элемент с наибольшим числом английских гласных букв = {elem_answer}")
