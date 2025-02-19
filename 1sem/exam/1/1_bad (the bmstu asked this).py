diagonals = []
palindromes_count_lst =  []
len_i = None
len_j = None
line_ind = 0


def find_palindromes(line):
    line = line.split()
    palindrome_counter = 0
    for i in line:
        middle = len(i) // 2
        first = i[:middle]
        second = i[middle + 1:]
        if first == second:
            palindrome_counter += 1
    palindromes_count_lst.append(palindrome_counter)

with open("1.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        find_palindromes(line)
        if len_i is None:
            len_i = len(line)
            diagonals = [True] * len_i
        for i in range(line_ind, len_i):
            if line[i] != "%":
                diagonals[i - line_ind] = False
        line_ind += 1
print(diagonals)
print(palindromes_count_lst)

line_ind = 0
with open("out.txt", "w+", encoding="utf-8") as f_out, open("1.txt", encoding="utf-8") as f_in:
    for line in f_in:
        line = line.strip()
        for i in range(len_i):
            if diagonals[i - line_ind] and i - line_ind >= 0:
                continue
            else:
                f_out.write(line[i])
        f_out.write(" " + str(palindromes_count_lst[line_ind]))
        f_out.write("\n")
        line_ind += 1


