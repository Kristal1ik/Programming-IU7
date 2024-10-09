import math

# g0 = float(input("Введите начальное значение: "))
# gn = float(input("Введите конечное значение: "))
# step = float(input("Введите шаг: "))
g0 = -20
gn = 5
step = 1
a2_count = 0
a3_lst = []
g0_lst = []
header1 = "g"
header2 = "a1"
header3 = "a2"
header4 = "a3"
table = ""
print("-" * 60)
print(f"|{header1:^14}|{header2:^14}|{header3:^14}|{header4:^14}|")
print("-" * 60)
for i in range(g0, gn + 1, step):
    g0 = i / 10
    g0_lst.append(g0)
    a1 = g0 ** 3 + 6.1 * g0 ** 2 - 35.4 * g0 - 25.7
    a2 = g0 ** 2 - math.cos(math.pi * g0)
    a3 = math.sqrt((a1 ** 2) + (a2 ** 2))
    a3_lst.append(a3)
    if a2 > 0:
        a2_count += 1
    table += f"|{g0:^14.5g}|{a1:^14.5g}|{a2:^14.5g}|{a3:^14.5g}|\n"

print(table[:-1])
print("-" * 60)
print("Количество положительных значений a2(g) =", a2_count)

dial_length = 12
max_a3_value = max(a3_lst)
min_a3_value = min(a3_lst)
max_a3_value_difference = (max_a3_value - min_a3_value)
ratio = max_a3_value_difference / 80
iteration = 0
serifs = int(input("Введите количество засечек (от 4 до 8): "))
serifs_flag = True if 4 <= serifs <= 8 else False
while not(serifs_flag):
    print("Некорректное значение!")
    serifs = int(input("Введите количество засечек (от 4 до 8): "))
    serifs_flag = True if 4 <= serifs <= 8 else False


label = "График функции a2 = g^2 - cos(π*g)"
print(dial_length * ' ' + label)
dist = 82 // serifs
for i in range(dial_length, dial_length + 82 + 1):
    if i % dist == 0:
        print("{0:>{1}}".format('s', i), end='')

print("{0:>{1}}\n {2:>{1}}>".format('y', dial_length + 82, 82 * "-"))
x_pos = abs(int((- min_a3_value) / ratio))



while iteration < len(a3_lst):
    y1_cur_value = a3_lst[iteration]
    cur_y1_value_and_min_difference = (y1_cur_value - min_a3_value) + \
                                      (y1_cur_value == min_a3_value) * \
                                      ((max_a3_value == min_a3_value))
    pos_of_y = int(cur_y1_value_and_min_difference * 80 / \
                   max_a3_value_difference)

    print("{1:^{0}.6g}".format(dial_length, g0_lst[iteration]), end='')
    print('|' + pos_of_y * ' ' + '*')
    x_pos = 0
    iteration += 1

print((dial_length + x_pos) * ' ' + '|\n',
      (dial_length + x_pos - 3) * ' ' + 'x V')
