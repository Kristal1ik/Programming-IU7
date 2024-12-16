"""

В файле in.txt записана квадратная целочисленная матрица А (числа в строках разделены одним пробелом).
Требуется в файл out.txt записать матрицу В, которая получится в результате поворота матрицы А на 90
градусов по часовой стрелке.

"""

# Фактические параметры, также называемые аргументами функции — переменные или выражения, которые должны быть
# упомянуты при вызове функции, и которые определяют начальные значения переменных-параметров при этом выполнении
# функции.

# Область видимости — зона доступности элементов в коде. Она может быть глобальной или локальной.
#
# Глобальная область подразумевает то, что элементы программы открыты для использования в любой ее части. Они
# объявляются за рамками функций и блоков.

file = open("in.txt", "r")
file2 = open("out.txt", "w")
counter = 0
n = 0
stolb = ""

while True:
    line = file.readline()
    if not line:
        file2.write(stolb + '\n')
        stolb = ""
        file.seek(0)
        counter += 1
        flag_start = False
    if counter >= n and counter != 0:
        break
    line = line.strip('\n').split(' ')
    if line[0] != "":
        stolb = line[counter] + " " + stolb
    if counter == 0:
        flag_start = True
    if flag_start:
        n += 1
file.close()
file2.close()
