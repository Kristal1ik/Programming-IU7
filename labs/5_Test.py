import math

# g0 = float(input("Введите начальное значение: "))
# gn = float(input("Введите конечное значение: "))
# step = float(input("Введите шаг: "))
g0 = float(input())
gn = float(input())
step = float(input())
a2_count = 0
iteration = 0
dial_length = 12
max_value = 4
min_value = 4 - gn ** 2
max_a3_value_difference = (max_value - min_value)
width = 80
ratio = max_a3_value_difference / width
serifs = 2
label = "График функции y = 4 - x^2"
print(dial_length * ' ' + label)
dist = width // serifs
print("{1:>{0}.6g}".format(dial_length, min_value), end='')
print("{1:>{0}.6g}".format(width, max_value), end='')
print("{0:>{1}}\n {2:>{1}}>".format('y', dial_length + 82, 82 * "-"))
x_pos = abs(int((- min_value) / ratio))
for i in range(int((gn - g0) / step) + 1):
    x_current = g0 + i * step
    y1_cur_value = 4 - x_current ** 2
    cur_y1_value_and_min_difference = (y1_cur_value - min_value) + \
                                      (y1_cur_value == min_value) * \
                                      ((max_value == min_value))
    pos_of_y = int(cur_y1_value_and_min_difference * width / \
                   max_a3_value_difference)
    print("{1:^{0}.6g}".format(dial_length, x_current), end='')
    print('|' + pos_of_y * ' ' + '*')
    x_pos = 0
    iteration += 1

print((dial_length + x_pos) * ' ' + '|\n',
      (dial_length + x_pos - 3) * ' ' + 'x V')
