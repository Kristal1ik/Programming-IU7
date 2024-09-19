import math

a = float(input("Введите коэффициент а: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
print("-" * 50)
if a != 0:
    d = b * b - 4 * a * c
    if d < 0:
        print("Нет вещественных корней")
    else:
        if d == 0:
            x = -b / (2 * a)
            print(f"x1 = {x:.7g}")
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"x1 = {x1:.7g}\nx2 = {x2:.7g}")
elif a == 0:
    if b == 0:
        if c == 0:
            print("Любое x")
        else:
            print("Нет решений")
    else:
        x = -c / b
        print(x)
