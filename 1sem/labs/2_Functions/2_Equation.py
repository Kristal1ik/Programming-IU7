"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

"""



import math

a = float(input("Введите коэффициент а: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
print("-" * 50)
answer = ""
if a != 0:
    d = b * b - 4 * a * c
    if d < 0:
        answer = "Нет вещественных корней"
    else:
        if d == 0:
            x = -b / (2 * a)
            answer = round(x, 6)
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            answer = str(round(x1, 6)) + " " + str(round(x2, 6))
elif a == 0:
    if b == 0:
        if c == 0:
            answer = "Любое x"
        else:
            answer = "Нет решений"
    else:
        x = -c / b
        answer = x
print(answer)
