import struct


def shell(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def sort_file(filename):
    with open(filename, 'rb') as file:
        numbers = []
        while True:
            bytes_read = file.read(4)
            if not bytes_read:
                break
            number = struct.unpack('i', bytes_read)[0]
            numbers.append(number)
    shell(numbers)

    with open(filename, 'wb') as file:
        for number in numbers:
            file.write(struct.pack('i', number))


sort_file("data.bin")
