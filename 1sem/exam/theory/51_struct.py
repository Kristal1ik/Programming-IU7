import struct

# Упаковка данных с использованием big-endian порядка
data = struct.pack('>i f', 42, 3.14)  # Упаковка целого числа и float
print(data)  # Выводит упакованные байты

# Упаковка данных с использованием little-endian порядка
data_le = struct.pack('<i f', 42, 3.14)
print(data_le)  # Выводит упакованные байты в little-endian формате

# Упаковка данных с нативным выравниванием
data_native = struct.pack('@i f', 42, 3.14)
print(data_native)  # Выводит упакованные байты в нативном формате
