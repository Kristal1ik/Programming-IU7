def ShakerSort(arr):
    left = 0
    right = len(arr) - 1
    flag = True

    while left < right and flag:
        flag = False
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        right -= 1
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                flag = True
        left += 1
    return arr


n = int(input("Введите расмер списка: "))
lst = []
for i in range(n):
    lst.append(int(input("Введите {} элемент списка: ".format(i + 1))))
sorted_lst = ShakerSort(lst)
print(sorted_lst)