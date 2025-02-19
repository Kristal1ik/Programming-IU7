import struct


def add(filename):
    with open(filename, 'rb') as file:
        numbers = []
        while True:
            bytes_read = file.read(4)
            if not bytes_read:
                break
            number = struct.unpack('i', bytes_read)[0]
            numbers.append(number)

    # Записываем числа и их удвоенные значения обратно в файл
    with open(filename, 'wb') as file:
        for number in numbers:
            if number % 2 == 0:
                file.write(struct.pack('i', number))
                doubled = number * 2
                file.write(struct.pack('i', doubled))
            else:
                file.write(struct.pack('i', number))


add("data.bin")
