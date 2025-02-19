import struct

size = 8


def output_bin_file(filename):
    with open(filename, 'rb') as file:
        while True:
            bytes_read = file.read(struct.calcsize('q'))
            if not bytes_read:
                break
            number = struct.unpack('q', bytes_read)[0]
            print(number)


def create_binary_file(filename, numbers):
    with open(filename, 'wb') as file:
        for number in numbers:
            file.write(struct.pack('q', number))


def swap(filename):
    with open(filename, 'r+b') as file:
        data = file.read()
        num_count = len(data) // size
        half_count = num_count // 2
        first_half = [struct.unpack('q', data[i * size:(i + 1) * size])[0] for i in range(half_count)]
        second_half = [struct.unpack('q', data[(i + half_count) * size:(i + half_count + 1) * size])[0] for i in
                       range(half_count)]

        first_half.reverse()
        file.seek(0)
        for number in second_half:
            file.write(struct.pack('q', number))
        for number in first_half:
            file.write(struct.pack('q', number))


file_name = "numbers.bin"
numbers_to_write = [1, 2, 3, 4, 5, 6, 7, size]
create_binary_file(file_name, numbers_to_write)
print("Файл до изменений:")
output_bin_file(file_name)
swap(file_name)
print("Файл после изменений:")
output_bin_file(file_name)
print("Данные в файле хранятся в одной строке (как в условии), но для экономии памяти выводятся в столбик.")