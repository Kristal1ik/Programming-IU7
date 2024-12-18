"""

В бинарном файле numbers.bin записана последовательность целых 8-байтных чисел (тип long long, формат д в модуле
struct). Требуется отсортировать его по возрастанию методом простых вставок и затем вывести файл на экран. Считывать
единовременно более двух чисел из файла в память запрещено (в процессе сортировки требуется переставлять записи в
самом файле).

"""

import struct


def insertion_sort_binary_file(filename):
    with open(filename, 'r+b') as f:
        f.seek(0, 2)  # Переход в конец файла
        file_size = f.tell()
        f.seek(0)  # Возвращаемся в начало файла

        n = file_size // struct.calcsize('q')  # 'q' для long long (8 байт)

        for i in range(1, n):
            f.seek(i * struct.calcsize('q'))
            key_bytes = f.read(struct.calcsize('q'))
            if len(key_bytes) < struct.calcsize('q'):
                break  # Если не удалось прочитать 8 байт, выходим из цикла
            key = struct.unpack('q', key_bytes)[0]

            j = i - 1

            while j >= 0:
                f.seek(j * struct.calcsize('q'))
                prev_bytes = f.read(struct.calcsize('q'))
                if len(prev_bytes) < struct.calcsize('q'):
                    break  # Если не удалось прочитать 8 байт, выходим из цикла
                prev = struct.unpack('q', prev_bytes)[0]

                if prev <= key:
                    break

                f.seek((j + 1) * struct.calcsize('q'))
                f.write(prev_bytes)
                j -= 1

            f.seek((j + 1) * struct.calcsize('q'))
            f.write(struct.pack('q', key))


# Вызов функции для сортировки файла
insertion_sort_binary_file('numbers.bin')

# Вывод содержимого файла на экран
with open('numbers.bin', 'rb') as f:
    while True:
        bytes_read = f.read(struct.calcsize('q'))
        if not bytes_read:
            break
        number = struct.unpack('q', bytes_read)[0]
        print(number)

# import struct
# import random
#
# def create_binary_file(filename, count):
#     with open(filename, 'wb') as f:
#         for _ in range(count):
#             number = random.randint(-2**63, 2**63 - 1)  # Генерация случайного числа типа long long
#             f.write(struct.pack('q', number))  # Запись числа в бинарном формате
#
# # Создаем файл с 100 случайными числами
# create_binary_file('numbers.bin', 100)

print("Файл 'numbers.bin' успешно создан с 100 случайными числами.")

# print("Файл 'numbers.bin' успешно создан с 100 случайными числами от 0 до 20.")