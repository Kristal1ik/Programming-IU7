"""

Коробовцева Ольга, ИУ7-11Б, Вариант 2

№1. Фактические параметры (аргументы функции) -- переменные, которые должны передаваться в функцию при ее вызове.
С ними можно взаимодействовать в теле функции, также они определяют нчальные значения переменных-параметров


№2. Области видимости — это зоны доступности переменных в программе,
которые определяют, где именно переменные могут быть использованы. они могут быть глобальынми и локальными.

"""

matrix_size = 0


def check_if_finished(col_num):
    return col_num >= matrix_size and col_num != 0


try:
    with open("in.txt", "r", encoding="utf-8") as f_input, open("out.txt", "w", encoding="utf-8") as f_output:
        column = ""
        column_num = 0
        flag_check_if_not_matrix_size = False
        while True:

            if check_if_finished(column_num):
                break

            row = f_input.readline()
            if not row:
                if column:
                    f_output.write(column.strip() + '\n')
                f_input.seek(0)
                column = ""
                column_num += 1
                flag_check_if_not_matrix_size = False

            row = row.strip().split(' ')
            if row and row[0] != "":
                if column_num < len(row):
                    column = row[column_num] + " " + column

            #  Определние размерности матрицы
            if column_num == 0:
                flag_check_if_not_matrix_size = True

            if flag_check_if_not_matrix_size:
                matrix_size += 1

except Exception as e:
    print(f"Произошла ошибка: {e}")
