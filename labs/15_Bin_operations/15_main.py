import struct


def create_test_file(filename):
    numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]

    with open(filename, 'wb') as file:
        for number in numbers:
            file.write(struct.pack('i', number))


if __name__ == "__main__":
    create_test_file("data.bin")
