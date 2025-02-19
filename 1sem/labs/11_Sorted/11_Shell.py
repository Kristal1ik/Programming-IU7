import random
import time


def ShellSort(arr):
    inc = len(arr)
    swaps = 0  # Переменная для подсчета перестановок
    while inc:
        for i, item in enumerate(arr):
            while i >= inc and arr[i - inc] > item:
                arr[i] = arr[i - inc]
                i -= inc
                swaps += 1  # Увеличиваем счетчик перестановок
            arr[i] = item
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return arr, swaps  # Возвращаем отсортированный массив и количество перестановок


def lst_output(arr, length):
    for i in range(length):
        print("{}-ый элемент списка = {}".format(i + 1, arr[i]))


def timing(arr):
    start = time.time()
    sorted_arr, swaps = ShellSort(arr)  # Получаем отсортированный массив и количество перестановок
    return time.time() - start, swaps  # Возвращаем время и количество перестановок


def is_positive_number(s):
    if s.isdigit():
        return int(s) > 0
    else:
        return False


def get_positive_number():
    while True:
        user_input = input("Введите число больше нуля: ")
        if is_positive_number(user_input):
            return int(user_input)
        else:
            print("Некорректный ввод!")


n = get_positive_number()

lst = []
for i in range(n):
    lst.append(int(input("Введите {} элемент списка: ".format(i + 1))))

print("-" * 50)
print("Исходный список:")
lst_output(lst, n)
print("-" * 50)
print("Отсортированный список с помощью алгоритма Шелла:")
sorted_lst, swaps = ShellSort(lst)
lst_output(sorted_lst, n)
print(f"Количество перестановок: {swaps}")

# Генерация случайных списков
n1 = int(input("Введите первую размерность списка: "))
while n1 <= 0:
    print("Размерность списка должна быть больше нуля!")
    n1 = int(input("Введите размерность случайного списка: "))
n2 = int(input("Введите вторую размерность списка: "))
while n2 <= 0:
    print("Размерность списка должна быть больше нуля!")
    n2 = int(input("Введите размерность случайного списка: "))
n3 = int(input("Введите третью размерность списка: "))
while n3 <= 0:
    print("Размерность списка должна быть больше нуля!")
    n3 = int(input("Введите размерность случайного списка: "))

lst_random_n1 = [random.randint(-100, 100) for _ in range(n1)]
lst_random_n2 = [random.randint(-100, 100) for _ in range(n2)]
lst_random_n3 = [random.randint(-100, 100) for _ in range(n3)]

lst_sorted_n1 = sorted([random.randint(-100, 100) for _ in range(n1)])
lst_sorted_n2 = sorted([random.randint(-100, 100) for _ in range(n2)])
lst_sorted_n3 = sorted([random.randint(-100, 100) for _ in range(n3)])

lst_inverted_n1 = sorted([random.randint(-100, 100) for _ in range(n1)], reverse=True)
lst_inverted_n2 = sorted([random.randint(-100, 100) for _ in range(n2)], reverse=True)
lst_inverted_n3 = sorted([random.randint(-100, 100) for _ in range(n3)], reverse=True)

# timing
lst_random_n1_timing, lst_random_n1_swaps = timing(lst_random_n1)
lst_random_n2_timing, lst_random_n2_swaps = timing(lst_random_n2)
lst_random_n3_timing, lst_random_n3_swaps = timing(lst_random_n3)

lst_sorted_n1_timing, lst_sorted_n1_swaps = timing(lst_sorted_n1)
lst_sorted_n2_timing, lst_sorted_n2_swaps = timing(lst_sorted_n2)
lst_sorted_n3_timing, lst_sorted_n3_swaps = timing(lst_sorted_n3)

lst_inverted_n1_timing, lst_inverted_n1_swaps = timing(lst_inverted_n1)
lst_inverted_n2_timing, lst_inverted_n2_swaps = timing(lst_inverted_n2)
lst_inverted_n3_timing, lst_inverted_n3_swaps = timing(lst_inverted_n3)

# Вывод результатов по количеству перестановок
print("-" * 50)
print(f"Количество перестановок для случайного списка n1: {lst_random_n1_swaps}")
print(f"Количество перестановок для случайного списка n2: {lst_random_n2_swaps}")
print(f"Количество перестановок для случайного списка n3: {lst_random_n3_swaps}")

print(f"Количество перестановок для отсортированного списка n1: {lst_sorted_n1_swaps}")
print(f"Количество перестановок для отсортированного списка n2: {lst_sorted_n2_swaps}")
print(f"Количество перестановок для отсортированного списка n3: {lst_sorted_n3_swaps}")

print(f"Количество перестановок для инвертированного списка n1: {lst_inverted_n1_swaps}")
print(f"Количество перестановок для инвертированного списка n2: {lst_inverted_n2_swaps}")
print(f"Количество перестановок для инвертированного списка n3: {lst_inverted_n3_swaps}")
print('_' * 146)
print(' ' * 20, '|', f"{'N1':^40}|{'N2':^40}|{'N3':^40}|")
print('_' * 146)
print(' ' * 20, '|',
      f"{'Время':^21}|{'Перестановки':^18}|{'Время':^21}|{'Перестановки':^18}|{'Время':^21}|{'Перестановки':^18}|")
print('_' * 146)
print(
    f"Упорядоченный        |\nсписок               |{lst_sorted_n1_timing:^22.6g}|{lst_sorted_n1_swaps:^18}|{lst_sorted_n2_timing:^21.6g}|{lst_sorted_n2_swaps:^18}|{lst_sorted_n3_timing:^21.6g}|{lst_sorted_n3_swaps:^18}|")
print('_' * 146)
print(
    f"Случайный            |\nсписок               |{lst_random_n1_timing:^22.6g}|{lst_random_n1_swaps:^18}|{lst_random_n2_timing:^21.6g}|{lst_random_n2_swaps:^18}|{lst_random_n3_timing:^21.6g}|{lst_random_n3_swaps:^18}|")
print('_' * 146)
print(
    f"Упорядоченный        |\nв обратном           |\nпорядке              |{lst_inverted_n1_timing:^22.6g}|{lst_inverted_n1_swaps:^18}|{lst_inverted_n2_timing:^21.6g}|{lst_inverted_n2_swaps:^18}|{lst_inverted_n3_timing:^21.6g}|{lst_inverted_n3_swaps:^18}|")
print('_' * 146)
