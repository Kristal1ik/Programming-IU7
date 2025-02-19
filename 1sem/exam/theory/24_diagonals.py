mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mx_size = len(mx)
main_diagonal = []
pob_diagonal = []

for i in range(mx_size):
    main_diagonal.append(mx[i][i])
# print(main_diagonal)

for i in range(mx_size):
    pob_diagonal.append(mx[i][mx_size - i - 1])
# print(pob_diagonal)


m = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]

for y in range(len(m)):
    for x in range(len(m[y])):
        if x >= y:  # Проверяем, что элемент находится в верхней части или на диагонали
            print(str(m[y][x]).rjust(3), end=" ")
        else:
            print("   ", end=" ")  # Печатаем пробелы для элементов ниже диагонали
    print()

print()

for y in range(len(m)):
    for x in range(y + 1):
        print(str(m[y][x]).ljust(3), end=" ")
    print()

# 0 2
# 1 1
# 2 0
#
# 0 0
# 1 1
# 2 2

'''
0 0, 0 1, 0 2, 1 1, 1 2, 2 2
'''