"""

В бинарном файле numbers.bin записана последовательность целых
8-байтных чисел (тип long long, формат и в модуле struct) чётной длины.
Требуется преобразовать его следующим образом: обменять местами первую и вторую половины файла так,
чтобы вторая половина сохранила свой исходный порядок, а первая оказалась в обратном порядке. Пример:
12345678 - 56784321
Затем вывести файл на экран. Обратить внимание на эффективность программы.

"""

import struct


def swap_and_reverse_in_place(filename):
    with open(filename, 'r+b') as file:
        data = file.read()
        num_count = len(data) // 8
        half_count = num_count // 2
        first_half = [struct.unpack('q', data[i * 8:(i + 1) * 8])[0] for i in range(half_count)]
        second_half = [struct.unpack('q', data[(i + half_count) * 8:(i + half_count + 1) * 8])[0] for i in
                       range(half_count)]

        first_half.reverse()
        file.seek(0)
        for number in second_half:
            file.write(struct.pack('q', number))
        for number in first_half:
            file.write(struct.pack('q', number))


swap_and_reverse_in_place('numbers.bin')

print("Файл 'numbers.bin' успешно изменен на месте.")

# def create_binary_file(filename, numbers):
#     with open(filename, 'wb') as file:
#         for number in numbers:
#             file.write(struct.pack('q', number))
# numbers_to_write = [1, 2, 3, 4, 5, 6, 7, 8]
# create_binary_file('numbers.bin', numbers_to_write)
