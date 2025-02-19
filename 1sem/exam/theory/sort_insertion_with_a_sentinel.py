def insertion_sort_with_barrier(seq):
    seq = [0] + seq
    for i in range(1, len(seq)):
        # Сохраняем текущее значение для вставки
        seq[0] = seq[i]
        j = i - 1
        # Сдвигаем элементы вправо, пока не найдем место для вставки
        while j > 0 and seq[0] < seq[j]:
            seq[j + 1] = seq[j]
            j -= 1
        # Вставляем текущее значение на правильную позицию
        seq[j + 1] = seq[0]
    return seq[1:]


# Пример использования
arr = [8, 9,9,  1]
sorted_arr = insertion_sort_with_barrier(arr)
print(sorted_arr)  # Вывод: [1, 8, 9]
