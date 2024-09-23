# Ввод координат точки
x = float(input('Введите x: '))
y = float(input('Введите y: '))

corr_counter = 0

# Левое крыло
if -9 <= x < -8:
    if 7 * (x + 8) ** 2 + 1 <= y <= (-1 / 8) * (x + 9) ** 2 + 8:
        corr_counter += 1
elif -8 <= x < -1:
    if 1 / 49 * (x + 1) ** 2 <= y <= (-1 / 8) * (x + 9) ** 2 + 8:
        corr_counter += 1
elif -8 <= x <= -2:
    if (1 / 3) * (x + 5) ** 2 - 7 <= y <= -(1 / 16) * x ** 2:
        corr_counter += 1
elif -2 < x < -1:
    if -2 * (x + 1) ** 2 - 2 <= y <= -(1 / 16) * x ** 2:
        corr_counter += 1
elif x == -1 and -2 <= y <= 0:
    corr_counter += 1


# Правое крыло
if 1 <= x <= 8:
    if (1 / 49) * (x - 1) ** 2 <= y <= -(1 / 8) * (x - 9) ** 2 + 8:
        corr_counter += 1
elif 8 < x <= 9:
    if 7 * (x - 8) ** 2 + 1 <= y <= -(1 / 8) * (x - 9) ** 2 + 8:
        corr_counter += 1
elif x == 1 and -2 <= y <= 0:
    corr_counter += 1
elif 1 <= x <= 2:
    if -2 * (x - 1) ** 2 - 2 <= y <= -(1 / 16) * x ** 2:
        corr_counter += 1
elif 2 < x <= 8:
    if (1 / 3) * (x - 5) ** 2 - 7 <= y <= -(1 / 16) * x ** 2:
        corr_counter += 1

# Тело
if -1 <= x <= 1:
    if 4 * x ** 2 - 6 <= y <= -4 * x ** 2 + 2:
        corr_counter += 1
# Усы
if -2 <= x <= 0:
    if -(3 / 2) * x + 2 == y:
        corr_counter += 1
elif 0 < x <= 2:
    if (3 / 2) * x + 2 == y:
        corr_counter += 1


if corr_counter > 0:
    print("Принадлежит")
else:
    print("Не принадлежит")
