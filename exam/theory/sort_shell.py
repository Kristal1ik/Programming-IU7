def shell_sort(seq):
    inc = len(seq) // 2
    while inc > 0:
        for i, elem in enumerate(seq):
            while i >= inc and elem < seq[i - inc]:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = elem
        inc //= 2
    return seq


arr = [12, 11, 13, 5, 6]
sorted_arr = shell_sort(arr)
print("Отсортированный массив:", sorted_arr)
