def is_integer(s):
    """Проверяет, является ли строка целым числом."""
    return s.lstrip('-').isdigit()

def compare_sequences(line_a, line_b, verbose=False):
    index_a = 0
    index_b = 0

    words_a = line_a.split()
    words_b = line_b.split()

    while index_a < len(words_a) and index_b < len(words_b):
        # Получаем текущее слово из первой строки
        current_a = words_a[index_a]
        # Получаем текущее слово из второй строки
        current_b = words_b[index_b]

        if is_integer(current_a) and is_integer(current_b):
            if current_a != current_b:
                print(f"Найдено несоответствие: {current_a} (строка 1) не равно {current_b} (строка 2).")
                return 1  # Возвращаем код ошибки при несоответствии

            if verbose:
                print(f"Число {current_a} найдено в обеих строках.")

            index_a += 1
            index_b += 1
        elif is_integer(current_a):
            print(f"Найдено несоответствие: {current_a} (строка 1) не имеет соответствия во второй строке.")
            return 1
        elif is_integer(current_b):
            print(f"Найдено несоответствие: {current_b} (строка 2) не имеет соответствия в первой строке.")
            return 1
        else:
            # Если оба слова не являются числами, просто переходим к следующему слову
            index_a += 1
            index_b += 1

    # Проверка на оставшиеся числа в одной из строк
    while index_a < len(words_a):
        if is_integer(words_a[index_a]):
            print(f"Найдено лишнее число в первой строке: {words_a[index_a]}")
            return 1
        index_a += 1

    while index_b < len(words_b):
        if is_integer(words_b[index_b]):
            print(f"Найдено лишнее число во второй строке: {words_b[index_b]}")
            return 1
        index_b += 1

    print("Все целые числа совпадают.")
    return 0  # Возвращаем код успешного завершения при совпадении всех чисел.

if __name__ == "__main__":
    # Пример входных данных
    line1 = "3 2 1 2 т 3"
    line2 = "3 в 2 1"

    verbose = True  # Установите True для подробного вывода

    exit_code = compare_sequences(line1, line2, verbose)
    exit(exit_code)