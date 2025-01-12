diagonals = []
diagonals_quantity = 0
counter_m = 0
bad_diagonals = []
palindromes_count_lst = []


def append_items(line):
    global counter_m
    line = line.strip()
    number = 0
    find_palindromes(line)
    for i in range(counter_m, diagonals_quantity):
        diagonals[number] += line[i]
        number += 1
    counter_m += 1


def check_diagonal():
    for i in range(len(diagonals)):
        if diagonals[i] == counter_m * "%":
            bad_diagonals.append(i)


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
        if diagonals_quantity == 0:
            diagonals_quantity = len(line.split()[0])
            diagonals = [""] * diagonals_quantity
            append_items(line)
        else:
            append_items(line)
    size = diagonals_quantity - counter_m + 1
    check_diagonal()


