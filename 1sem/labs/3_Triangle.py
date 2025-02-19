"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Программа по введенным целочисленным координатам трех точек на плоскости вычисляет длины сторон
образованного треугольника и длину медианы, проведенной из наибольшего угла, определяет вид треугольника.
Далее по введенным координатам точки вычисляет, находится ли они внутри треугольника.
Если да, то находит расстояние от точки до ближайшей стороны треугольника.

"""

import math

# Объявление необходимых булевых значений, необходимых по условию задачи
is_in_triangle = False
eps = 1e-6
print("Введите координаты первой точки")
x_a = int(input("x: "))
y_a = int(input("y: "))
print("Введите координаты второй точки")
x_b = int(input("x: "))
y_b = int(input("y "))
print("Введите координаты третьей точки")
x_c = int(input("x: "))
y_c = int(input("y: "))

# Вычисление длин сторон
ab = math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
ac = math.sqrt((x_c - x_a) ** 2 + (y_c - y_a) ** 2)
bc = math.sqrt((x_c - x_b) ** 2 + (y_c - y_b) ** 2)
if not ((ab + ac <= bc) or (ac >= ab + bc) or (ab >= ac + bc)):
    print("-" * 50)
    a = max(ab, bc, ac)
    b = min(ab, bc, ac)
    c = ab + bc + ac - a - b
    # Наибольший угол лежит напротив наибольшей стороны
    m_ab = 0.5 * (math.sqrt(2 * c ** 2 + 2 * b ** 2 - a ** 2))
    print(f"AB = {ab:.7g}\n"
          f"BC = {bc:.7g}\n"
          f"AC = {ac:.7g}")

    # Определение вида треугольника
    if a ** 2 > (c ** 2 + b ** 2):
        print("Треугольник тупоугольный")
        print(f"Медиана из тупого угла равна: {m_ab:.7g}")
    else:
        print("Треугольник не тупоугольный")
    print("-" * 50)

    # Ввод координат точки
    x_new = int(input("Введите координату х новой точки: "))
    y_new = int(input("Введите координату у новой точки: "))

    # Проверка на принадлежность точки треугольнику
    abc = abs((x_a * (y_b - y_c) + x_b * (y_c - y_a) + x_c * (y_a - y_b)) / 2)
    newbc = abs((x_new * (y_b - y_c) + x_b * (y_c - y_new) + x_c * (y_new - y_b)) / 2)
    newac = abs((x_a * (y_new - y_c) + x_new * (y_c - y_a) + x_c * (y_a - y_new)) / 2)
    newab = abs((x_a * (y_b - y_new) + x_b * (y_new - y_a) + x_new * (y_a - y_b)) / 2)
    if abc - (newbc + newac + newab) < eps:
        print("Точка находится внутри треугольника")
        is_in_triangle = True
    else:
        print("Точка лежит вне треугольника")
    if is_in_triangle:
        # Нахождение наименьшего расстояния от точки до прямой
        new_to_a = math.sqrt((x_new - x_a) ** 2 + (y_new - y_a) ** 2)
        new_to_b = math.sqrt((x_new - x_b) ** 2 + (y_new - y_b) ** 2)
        new_to_c = math.sqrt((x_new - x_c) ** 2 + (y_new - y_c) ** 2)

        p_abnew = (new_to_a + new_to_b + ab) / 2
        p_bcnew = (new_to_b + new_to_c + bc) / 2
        p_acnew = (new_to_a + new_to_c + ac) / 2

        s_abnew = math.sqrt(p_abnew * (p_abnew - new_to_a) * (p_abnew - new_to_b) * (p_abnew - ab))
        h_abnew = (2 * s_abnew) / ab

        s_bcnew = math.sqrt(p_bcnew * (p_bcnew - new_to_b) * (p_bcnew - new_to_c) * (p_bcnew - bc))
        h_bcnew = (2 * s_bcnew) / bc

        s_acnew = math.sqrt(p_acnew * (p_acnew - new_to_a) * (p_acnew - new_to_c) * (p_acnew - ac))
        h_acnew = (2 * s_acnew) / ac

        min_distance = min(h_abnew, h_acnew, h_bcnew)
        print(f"Минимальное расстояние от точки до одной из сторон = {min_distance:.7g}")
        print("-" * 50)
else:
    print("Это не треугольник")

'''
0 0
0 5
5 0
0 -1

0 0
3 1
4 -2
3 0
'''
