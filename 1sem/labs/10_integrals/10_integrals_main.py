def f(x):
    return x ** 2


def F(x):
    return (1 / 3) * x ** 3


# Метод левых треугольников
def left_triangle_method(a, b, n):
    h = (b - a) / n  # длина отрезков
    integral = 0
    for x in range(n):
        integral += f(a + x * h)
    integral *= h
    return integral


# Метод трапеций
def trapezoidal_method(a, b, n):
    h = (b - a) / n  # высота трапеций
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral


a = float(input("Введите начало отрезка интегрирования (a): "))
b = float(input("Введите конец отрезка интегрирования (b > a, a = {}): ".format(a)))
while b <= a:
    print("Конец отрезка должен быть больше начала!")
    b = float(input("Введите конец отрезка интегрирования (b > a, a = {}): ".format(a)))
n1 = int(input("Введите количество участков разбиения для метода левых прямоугольников (N1): "))
while n1 <= 0:
    print("Количество участков разбиения должно быть больше 0!")
    n1 = int(input("Введите количество участков разбиения для метода левых прямоугольников (N1): "))
n2 = int(input("Введите количество участков разбиения для метода трапеций (N2): "))
while n2 <= 0:
    print("Количество участков разбиения должно быть больше 0!")
    n2 = int(input("Введите количество участков разбиения для метода левых прямоугольников (N1): "))

left_triangle_method_n1 = left_triangle_method(a, b, n1)
left_triangle_method_n2 = left_triangle_method(a, b, n2)

trapezoidal_method_n1 = trapezoidal_method(a, b, n1)
trapezoidal_method_n2 = trapezoidal_method(a, b, n2)

#  Таблица вычисленных интегралов
print("-" * 70)
left_triangle_header = "Левые прямоугольники"
trapezoidal_method_header = "Метод трапеций"
print(f"{'':<30}{'N1':<20}{'N2'}")
print(f"{left_triangle_header:<30}{left_triangle_method_n1:<20.5f}{left_triangle_method_n2:<20.5f}")
print(f"{trapezoidal_method_header:<30}{trapezoidal_method_n1:<20.5f}{trapezoidal_method_n2:<20.5f}")

correct_integral = F(b) - F(a)

#  Абсолютные погрешности

abs_error_left_n1 = abs(left_triangle_method_n1 - correct_integral)
abs_error_left_n2 = abs(left_triangle_method_n2 - correct_integral)

abs_error_trap_n1 = abs(trapezoidal_method_n1 - correct_integral)
abs_error_trap_n2 = abs(trapezoidal_method_n2 - correct_integral)

#  Относительные погрешности

rel_error_left_n1 = abs_error_left_n1 / abs(correct_integral)
rel_error_left_n2 = abs_error_left_n2 / abs(correct_integral)

rel_error_trap_n1 = abs_error_trap_n1 / abs(correct_integral)
rel_error_trap_n2 = abs_error_trap_n2 / abs(correct_integral)

#  Таблица погрешностей
print("-" * 70)
abs_error = "Абсолютная погрешность"
rel_error = "Относительная погрешность"

header1 = left_triangle_header + " N1"
header2 = left_triangle_header + " N2"
header3 = trapezoidal_method_header + " N1"
header4 = trapezoidal_method_header + " N2"

print(f"{'':<30}{'abs_error':<20}{'rel_error'}")
print(f"{header1:<30}{abs_error_left_n1:<20.5f}{rel_error_left_n1:<20.5f}")
print(f"{header2:<30}{abs_error_left_n2:<20.5f}{rel_error_left_n2:<20.5f}")
print(f"{header3:<30}{abs_error_trap_n1:<20.5f}{rel_error_trap_n1:<20.5f}")
print(f"{header4:<30}{abs_error_trap_n2:<20.5f}{rel_error_trap_n2:<20.5f}")

#  Определение наиболее точного метода
# Инициализация словаря для подсчета "побед"
d = {left_triangle_header: 0, trapezoidal_method_header: 0}

# Сравнение абсолютных погрешностей
if abs_error_trap_n1 < abs_error_left_n1:
    d[trapezoidal_method_header] += 1
else:
    d[left_triangle_header] += 1

if abs_error_left_n2 < abs_error_trap_n2:
    d[left_triangle_header] += 1
else:
    d[trapezoidal_method_header] += 1

# Сравнение относительных погрешностей
if rel_error_left_n1 < rel_error_trap_n1:
    d[left_triangle_header] += 1
else:
    d[trapezoidal_method_header] += 1

if rel_error_left_n2 < rel_error_trap_n2:
    d[left_triangle_header] += 1
else:
    d[trapezoidal_method_header] += 1

print(70 * "-")
best_value = max(d, key=d.get)
bad_value = min(d, key=d.get)
print(f"Наиболее точный метод: {best_value}")
print(best_value, bad_value)

# Задаем точность ε
eps = float(input("Введите желаемую точность ε: "))
while eps < 0:
    print("Погрешность должна быть больше 0!")
n = n2
while True:
    if bad_value == "Левые прямоугольники":
        I_N = left_triangle_method(a, b, n)
        I_2N = left_triangle_method(a, b, 2 * n)
    else:
        I_N = trapezoidal_method(a, b, n)
        I_2N = trapezoidal_method(a, b, 2 * n)
    if abs(I_N - I_2N) < eps:
        break
    n *= 2
print(70 * "-")
print(f"Приближенное значение интеграла по методу {bad_value}: {I_2N:.5f}")
print(f"Количество участков разбиения: {n}")

