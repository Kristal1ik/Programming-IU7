import math

# g0 = float(input("Введите начальное значение: "))
# gn = float(input("Введите конечное значение: "))
# step = float(input("Введите шаг: "))
g0 = -2
gn = 0.5
step = 0.1
a2_count = 0
header1 = "g"
header2 = "a1"
header3 = "a2"
header4 = "a3"
table = ""
print("-" * 60)
print(f"|{header1:^14}|{header2:^14}|{header3:^14}|{header4:^14}|")
print("-" * 60)
for i in range(0, int(abs((g0 - gn) / step))):
    a1 = g0 ** 3 + 6.1 * g0 ** 2 - 35.4 * g0 - 25.7
    a2 = g0 ** 2 - math.cos(math.pi * g0)
    a3 = math.sqrt((a1 ** 2) + (a2 ** 2))
    if a2 > 0:
        a2_count += 1
    table += f"|{g0:^14.5g}|{a1:^14.5g}|{a2:^14.5g}|{a3:^14.5g}|\n"
    g0 += step
print(table[:-1])
print("-" * 60)
print("Количество положительных значений a2(g) =", a2_count)
dial_length = 12
label = "График функции y1 = x**3 - 2*x**2 + 4*x - 8"

print("{0:>{1}}".format(label, len(label) + dial_length), '\n')
print("{aux[1]:>{aux[0]}}\n {aux[2]:>{aux[0]}}>\n".format(aux=
                                                          [dial_length + 81, 'y', 82 * '-']), end='')
#
# MAX_Y1_VALUE_DIFFERENCE = (max_y1_value - min_y1_value) + \
#                           (max_y1_value == min_y1_value)
# RATIO = MAX_Y1_VALUE_DIFFERENCE / 80
# AXIS_X_POS = abs(int((- min_y1_value) / RATIO))
# if (AXIS_X_POS > 80):
#     AXIS_X_POS = 81
#
# while (is_sequence_decreasing and from_x >= to_x) or \
#         (not is_sequence_decreasing and from_x <= to_x):
#
#     y1_cur_value = y1(from_x)
#     cur_y1_value_and_min_difference = (y1_cur_value - min_y1_value) + \
#                                       (y1_cur_value == min_y1_value) * \
#                                       ((max_y1_value == min_y1_value))
#     pos_of_y = int(cur_y1_value_and_min_difference * 80 / \
#                    MAX_Y1_VALUE_DIFFERENCE)
#
#     print("{1:^{0}.6g}".format(dial_length, from_x), end='')
#
#     if (negative_value_exists):
#         if y1_cur_value <= 0 - RATIO / 2:
#             req_aux = AXIS_X_POS - pos_of_y
#             if (req_aux != 0):
#                 print(pos_of_y * ' ' + '*' + (req_aux - 1) * ' ' + '|')
#             else:
#                 print((AXIS_X_POS - 1) * ' ' + '*' + '|')
#         elif y1_cur_value >= 0 + RATIO / 2:
#             req_aux = pos_of_y - AXIS_X_POS
#             if (req_aux != 0):
#                 print(AXIS_X_POS * ' ' + '|' + (req_aux - 1) * ' ' + '*')
#             else:
#                 print((AXIS_X_POS) * ' ' + '|*')
#         else:
#             print(AXIS_X_POS * ' ' + '*')
#     else:
#         print('|' + pos_of_y* ' ' + '*')
#         AXIS_X_POS = 0
#     from_x += pace_x
# print((dial_length + AXIS_X_POS) * ' ' + '|\n',
#       (dial_length + AXIS_X_POS - 3) * ' ' + 'x V')
