import math

# Объявление необходимых булевых значений, необходимых по условию задачи
is_in_triangle = False
print("Введите координаты точки А")
x_a = int(input("x: "))
y_a = int(input("y: "))
print("Введите координаты точки B")
x_b = int(input("x: "))
y_b = int(input("y "))
print("Введите координаты точки C")
x_c = int(input("x: "))
y_c = int(input("y: "))

# Вычисление длин сторон
ab_ = math.sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
ac_ = math.sqrt((x_c - x_a) ** 2 + (y_c - y_a) ** 2)
bc_ = math.sqrt((x_c - x_b) ** 2 + (y_c - y_b) ** 2)
if not ((ab_ + ac_ <= bc_) or (ac_ >= ab_ + bc_) or (ab_ >= ac_ + bc_)):
    print("-" * 50)
    # Наибольший угол лежит напротив наибольшей стороны
    ab = max(ab_, ac_, bc_)
    ac = min(ab_, ac_, bc_)
    bc = ab_ + ac_ + bc_ - ab - ac
    m_ab = 0.5 * (math.sqrt(2 * ac ** 2 + 2 * bc ** 2 - ab ** 2))
    print(f"AB= {ab:.7g}\n"
          f"BC= {bc:.7g}\n"
          f"AC= {ac:.7g}")
    print(f"Медиана из тупого угла равна: {m_ab:.7g}")

    # Проверка на тупоугольность
    if abs((ac ** 2 + bc ** 2) - (ab ** 2)) < math.e:
        print("Треугольник прямоугольнй")
    elif ab ** 2 > (ac ** 2 + bc ** 2):
        print("Треугольник тупоугольный")

    else:
        print("Треугольник остроугольный")
    print("-" * 50)

    # Ввод координат точки
    x_new = int(input("Введите координату х новой точки: "))
    y_new = int(input("Введите координату у новой точки: "))

    # Проверка на принадлежность точки треугольнику
    abc = abs((x_a * (y_b - y_c) + x_b * (y_c - y_a) + x_c * (y_a - y_b)) / 2.0)
    newbc = abs((x_new * (y_b - y_c) + x_b * (y_c - y_new) + x_c * (y_new - y_b)) / 2.0)
    newac = abs((x_a * (y_new - y_c) + x_new * (y_c - y_a) + x_c * (y_a - y_new)) / 2.0)
    newab = abs((x_a * (y_b - y_new) + x_b * (y_new - y_a) + x_new * (y_a - y_b)) / 2.0)
    if abc == newbc + newac + newab:
        print("Точка находится внутри треугольника")
        is_in_triangle = True
    else:
        print("Точка лежит вне треугольника")
    if is_in_triangle:
        # Нахождение наименьшего расстояния от точки до прямой
        x_center_ab = (x_b + x_a) / 2
        y_center_ab = (y_b + y_a) / 2
        distance_ab = abs(math.sqrt((x_center_ab - x_new) ** 2 + (y_center_ab - y_new) ** 2))

        x_center_ac = (x_c + x_a) / 2
        y_center_ac = (y_c + y_a) / 2
        distance_ac = abs(math.sqrt((x_center_ac - x_new) ** 2 + (y_center_ac - y_new) ** 2))

        x_center_bc = (x_c + x_b) / 2
        y_center_bc = (y_c + y_b) / 2
        distance_bc = abs(math.sqrt((x_center_bc - x_new) ** 2 + (y_center_bc - y_new) ** 2))
        min_distance = min(distance_ab, distance_ac, distance_bc)
        print(f"Минимальное расстояние от точки до одной из сторон = {min_distance}")
        print("-" * 50)
else:
    print("Это не треугольник")

'''
0 0
0 5
5 0
0 -1
'''
