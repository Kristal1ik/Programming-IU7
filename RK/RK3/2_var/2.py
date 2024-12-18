"""

В бинарном файле numbers.bin записана последовательность целых
8-байтных чисел (тип long long, формат д в модуле struct).
Требуется удалить из файла все чётные элементы. Считывать единовременно более одного числа из файла в память запрещено.

"""


import struct
import os


def remove_even_numbers(input_filename):
    with open(input_filename, 'r+b') as infile:
        position = 0  # Позиция для записи нечетного числа
        while True:
            bytes_read = infile.read(8)  # Читаем одно 8-байтное число
            if not bytes_read:
                break  # Достигнут конец файла

            number = struct.unpack('q', bytes_read)[0]  # 'q' для long long (8 байт)

            if number % 2 != 0:  # Если число нечетное
                infile.seek(position)  # Переходим к позиции для записи
                infile.write(bytes_read)  # Записываем нечетное число
                position += 8  # Увеличиваем позицию на размер числа (8 байт)

        # Обрезаем файл до нового размера
        infile.truncate(position)


# Вызов функции с указанием имени файла
remove_even_numbers('numbers.bin')
# import struct
# import random
#
# def create_numbers_file(filename, count):
#     with open(filename, 'wb') as f:
#         for _ in range(count):
#             number = random.randint(-9223372036854775808, 9223372036854775807)  # Генерация случайного long long
#             f.write(struct.pack('q', number))  # 'q' для long long (8 байт)
#
# # Создание файла с 100 случайными числами
# create_numbers_file('numbers.bin', 100)
#
# print("Файл 'numbers.bin' успешно создан с 100 случайными числами.")

print("Все четные числа удалены из файла 'numbers.bin'.")
