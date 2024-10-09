import math
# Входные данные
start = float(input("Введите начальное значение аргумента: "))
finish = float(input("Введите конечное значение аргумента: "))
step = float(input("Введите шаг разбиения отрезка: "))
width = int(input("Введите ширину графика: "))
# Инициализация переменных
table = ""  # Таблица для вывода значений функции


# Заголовки таблицы
header1 = "g"
header2 = "a1"
header3 = "a2"
header4 = "a3"
a3_min = math.inf
a3_max = -math.inf
if start < finish:
    # Вычисления
    for i in range(int((finish - start) / step) + 1):
        x = start + i * step  # Добавляем к значению x шаг
        if x > finish:
            break
        else:
            a1 = x ** 3 + 6.1 * x ** 2 - 35.4 * x - 25.7
            a2 = x ** 2 - math.cos(math.pi * x)
            a3 = math.sqrt((a1 ** 2) + (a2 ** 2))
            if a3_min > a3:
                a3_min = a3
            if a3_max < a3:
                a3_max = a3
            table += f"|{x:^14.5g}|{a1:^14.5g}|{a2:^14.5g}|{a3:^14.5g}|\n"

    # Вывод таблицы значений
    print("-" * 60)
    print(f"|{header1:^14}|{header2:^14}|{header3:^14}|{header4:^14}|")
    print("-" * 60)
    print(table[:-1])
    print("-" * 60)

    # Вычисления для графика
    while True:  # Проверка на входное число
        k = int(input("Введите количество засечек на оси ординат от 4 до 8): "))
        if 4 <= k <= 8:
            break
        else:
            print('Количество засечек должно быть от 4 до 8!')

    free_space = width - len(f"{start:.5g}")  # Место для засечек

    # Вывод засечек
    print(" " * 14 + f"{a3_min:.5g}", end="")

    for i in range(1, k):
        current_y = a3_min + abs(a3_max - a3_min) / (k - 1) * i
        current_space = free_space // (k - i)
        free_space -= current_space

        print(" " * (current_space - len(f"{current_y:.5g}") - 1), f"{current_y:.5g}", end="")

    print('\n')

    one = abs(a3_min - a3_max) / width  # Место для 1 символа
    zero = int(abs(a3_min) // one)  # Столбец для x = 0

    # Построение графика
    for i in range(int((finish - start) / step) + 1):
        x = start + i * step  # Добавляем к значению x шаг
        a1 = x ** 3 + 6.1 * x ** 2 - 35.4 * x - 25.7
        a2 = x ** 2 - math.cos(math.pi * x)
        a3 = math.sqrt((a1 ** 2) + (a2 ** 2))

        current_x = int(abs(a3_min - a3) // one)  # Текущая позиция

        if current_x == width:
            current_x -= 1

        # вывод строки графика
        print(f"{x:<12.5g} |", end="")
        if zero < current_x and a3_min <= 0 <= a3_max:
            print(" " * zero + "|" + " " * (current_x - zero - 1) + "*" + " " * (width - current_x - 1))
        elif zero > current_x and a3_min <= 0 <= a3_max:
            print(" " * current_x + "*" + " " * (zero - current_x - 1) + "|" + " " * (width - zero - 1))
        else:
            print(" " * current_x + "*" + " " * (width - current_x - 1))
else:
    print("Некорректные значения!")