import math

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
print("-" * 50)

# Наибольший угол лежит напротив наибольшей стороны
ab = max(ab_, ac_, bc_)
ac = min(ab_, ac_, bc_)
bc = ab_ + ac_ + bc_ - ab - ac
m_ab = 0.5 * (math.sqrt(2 * ac ** 2 + 2 * bc ** 2 - ab ** 2))
print(ab, ac, bc)
print("-" * 50)

print(f"Медиана из тупого угла равна: {m_ab:.7g}")

print("-" * 50)

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
# p = (ab + ac + bc) / 2
# s = math.sqrt(p * (p - ab) * (p - bc) * (p - bc))
# h_ab = (2 * s) / ab
# h_ac = (2 * s) / ac
# h_bc = (2 * s) / bc
#
# a_new = math.sqrt((x_new - x_a) ** 2 + (y_new - y_a) ** 2)
# b_new = math.sqrt((x_new - x_b) ** 2 + (y_new - y_b) ** 2)
# c_new = math.sqrt((x_new - x_c) ** 2 + (y_new - y_c) ** 2)
#
# print("-" * 50)
# print(a_new * h_ab, b_new * h_bc, c_new * h_ac)
# if a_new * h_ab > 0 and b_new * h_bc > 0 and c_new * h_ac > 0:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


abc = abs((x_a * (y_b - y_c) + x_b * (y_c - y_a) + x_c * (y_a - y_b)) / 2.0)
# newbc = area(x_new, y_new, x_b, y_b, x_c, y_c)
newbc = abs((x_new * (y_b - y_c) + x_b * (y_c - y_new) + x_c * (y_new - y_b)) / 2.0)
# newac = area(x_a, y_a, x_new, y_new, x_c, y_c)
newac = abs((x_a * (y_new - y_c) + x_new * (y_c - y_a) + x_c * (y_a - y_new)) / 2.0)
# newab = area(x_a, y_a, x_b, y_b, x_new, y_new)
newab = abs((x_a * (y_b - y_new) + x_b * (y_new - y_a) + x_new * (y_a - y_b)) / 2.0)

if abc == newbc + newac + newab:
    print("Точка находитс внутри треугольника")
else:
    print("Точка лежит вне треугольника")

'''
0 0
0 5
5 0
0 -1
# '''
