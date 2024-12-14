# Задаем интегрируемую функцию и ее первообразную
def f(x):
    return x ** 2  # Пример функции: f(x) = x^2


def F(x):
    return (1 / 3) * x ** 3  # Первообразная: F(x) = (1/3)x^3


# Метод левых треугольников
def left_triangle_method(a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        integral += f(a + i * h)
    integral *= h
    return integral


# Метод трапеций
def trapezoidal_method(a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral


# Основная функция для вычисления интегралов и погрешностей
def compute_integrals(a, b, n1, n2, epsilon):
    results = []

    for n in [n1, n2]:
        left_integral = left_triangle_method(a, b, n)
        trapezoidal_integral = trapezoidal_method(a, b, n)

        # Вычисляем абсолютные и относительные погрешности
        exact_value = F(b) - F(a)
        left_abs_error = abs(left_integral - exact_value)
        trapezoidal_abs_error = abs(trapezoidal_integral - exact_value)

        left_rel_error = left_abs_error / abs(exact_value) if exact_value != 0 else float('inf')
        trapezoidal_rel_error = trapezoidal_abs_error / abs(exact_value) if exact_value != 0 else float('inf')

        results.append((n, left_integral, trapezoidal_integral,
                        left_abs_error, trapezoidal_abs_error,
                        left_rel_error, trapezoidal_rel_error))  # Добавляем все необходимые значения

    # Выводим таблицу результатов
    print(
        f"{'N':<10}{'Left Integral':<20}{'Trapezoidal Integral':<25}{'Left Abs Error':<20}{'Trapezoidal Abs Error':<25}")
    for result in results:
        n, left_int, trap_int, left_err, trap_err = result[:5]  # Убедитесь, что здесь правильное количество переменных
        print(f"{n:<10}{left_int:<20.6f}{trap_int:<25.6f}{left_err:<20.6f}{trap_err:<25.6f}")

    # Определяем наиболее точный метод
    min_left_error_index = min(range(len(results)),
                               key=lambda i: results[i][4])  # Индекс с минимальной ошибкой трапеции
    min_trap_error_index = min(range(len(results)),
                               key=lambda i: results[i][3])  # Индекс с минимальной ошибкой левых треугольников

    if results[min_left_error_index][4] < results[min_trap_error_index][3]:
        best_method = "Trapezoidal"
        best_index = min_left_error_index
    else:
        best_method = "Left Triangle"
        best_index = min_trap_error_index

    print(f"\nBest method is {best_method} with N={results[best_index][0]} and error={results[best_index][4]:.6f}")


# Пример использования функции с заданными параметрами
if __name__ == "__main__":
    a = 0  # Начало отрезка интегрирования
    b = 10  # Конец отрезка интегрирования
    N1 = 10  # Первое количество участков разбиения
    N2 = 20  # Второе количество участков разбиения
    epsilon = 0.01  # Заданная точность

    compute_integrals(a, b, N1, N2, epsilon)
