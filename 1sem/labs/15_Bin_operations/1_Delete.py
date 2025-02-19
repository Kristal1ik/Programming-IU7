import struct


def remove_odd_indexed(filename):
    with open(filename, 'rb') as file:
        numbers = []
        index = 0

        while True:
            bytes_read = file.read(4)  # Читаем 4 байта (32-битное целое)
            if not bytes_read:
                break
            number = struct.unpack('i', bytes_read)[0]
            # Сохраняем только числа с чётными индексами
            if index % 2 == 0:
                numbers.append(number)
            index += 1

    # Записываем только чётные индексы обратно в файл
    with open(filename, 'wb') as file:
        for number in numbers:
            file.write(struct.pack('i', number))


remove_odd_indexed("data.bin")
