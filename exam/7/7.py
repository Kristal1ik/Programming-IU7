"""

2. В файле in.txt записаны строки, длина каждой не превышает 100 символов.
Диагональю из символов в рамках этой задачи считать последовательность символов,
расположенных во всех строках файла так, что символ в следующей строке находится
на одну позицию правее символа в предыдущей строке. Требуется переписать в файл
out. txt содержимое исходного файла так, чтобы туда не попали диагонали из символов
%, если они есть. Также к каждой строке через пробел нужно добавить число
слов-палиндромов длиной больше одного, которые в ней присутствуют. Считывать
файл в память целиком нельзя.

"""

with open("in.txt", "r", encoding="utf-8") as file1, open("out.txt", "w", encoding="utf-8"):
    diagonals = []
    while True:
        ...