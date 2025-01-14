"""

Даны 2 текстовых файла in1. txt и in2.txt, в которых записан убывающие
последовательности целых чисел, по одному числу в строке. Не используя списки
и методы сортировки, сформировать файл out. txt, в который записать неубывающую
последовательность чисел, содержащую все числа из исходных файлов. С файлами in.txt и
in2.txt работать построчно (в памяти единовременно должно находиться не более одной строки из каждого файла).

"""
# Функции высшего порядка — это функции, которые либо принимают, либо возвращают другие функции, либо делают всё сразу. Функции высшего порядка — это функции, которые либо принимают, либо возвращают другие функции, либо делают всё сразу.

def merge_sorted_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        num1 = f1.readline()  # Считываем первое число из первого файла
        num2 = f2.readline()  # Считываем первое число из второго файла

        # Преобразуем считанные строки в целые числа (или None, если строка пустая)
        if num1:
            num1 = int(num1.strip())
        else:
            num1 = None

        if num2:
            num2 = int(num2.strip())
        else:
            num2 = None

        while num1 is not None or num2 is not None:  # Пока есть числа в любом из файлов
            if num1 is not None and (num2 is None or num1 >= num2):
                out.write(f"{num1}\n")  # Записываем число из первого файла
                try:
                    num1 = int(f1.readline().strip())  # Считываем следующее число из первого файла
                except ValueError:
                    num1 = None  # Если больше нет чисел, устанавливаем в None
            elif num2 is not None:
                out.write(f"{num2}\n")  # Записываем число из второго файла
                try:
                    num2 = int(f2.readline().strip())  # Считываем следующее число из второго файла
                except ValueError:
                    num2 = None  # Если больше нет чисел, устанавливаем в None


# Вызов функции с указанием имен файлов
merge_sorted_files('in1.txt', 'in2.txt', 'out.txt')


print("Файл 'out.txt' успешно создан с неубывающей последовательностью чисел.")

