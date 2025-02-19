"""

Дан файл in.txt в нем записаны предложения, в предложениях появляются вещественные 16-ричные числа,
гарантируется, что каждое число отделено пробелами от других символов. Необходимо прочитать файл
in и в файл out строки, в которых 16-чные заменить на 8-чные. Далее необходимо создать бинарный файл,
 в который записать кол во предложений, затем кол во слов в каждом предложении друг за другом.

Подводные камни: предложения на разных строчках, числа нужно обрабатывать и целочисленные тоже надо обрабатывать,
стоит учитывать унарные плюсы и минусы

"""


def from_letter_to_number(number):
    if number == "A":
        item = 10
    elif number == "B":
        item = 11
    elif number == "C":
        item = 12
    elif number == "D":
        item = 13
    elif number == "E":
        item = 14
    elif number == "F":
        item = 15
    else:
        item = int(number)
    return item


def whole_part_from_16_to_10(part):
    number = 0
    pow = len(part) - 1
    for i in range(len(part)):
        item = from_letter_to_number(part[i])
        number += item * 16 ** pow
        pow -= 1
    return str(number)
    # return int(part, 16)


def fractional_part_from_16_to_10(part):
    number = 0
    pow = -1
    for i in range(len(part)):
        item = from_letter_to_number(part[i])
        number += item * 16 ** pow
        pow -= 1
    return str(number)[2:]


def from_16_to_10(number):
    if "." in number:
        number = number.split(".")
    else:
        number = number.split(",")
    whole_part = whole_part_from_16_to_10(number[0])
    fractional_part = fractional_part_from_16_to_10(number[1])
    res_number = whole_part + "." + fractional_part
    return res_number



def whole_part_from_10_to_8(number):
    res_number = ""
    number = int(number)
    while number > 0:
        res_number += str(number % 8)
        number //= 8
    return res_number[::-1]


def fractional_part_from_10_to_8(number):
    res_number = ""
    number = int(number)
    while len(res_number) < 4 and number > 0:
        number *= 8
        res_number += str(int(number))
        number -= int(number)
    return res_number

def from_10_to_8(number):
    if "." in number:
        number = number.split(".")
    else:
        number = number.split(",")
    whole_part = whole_part_from_10_to_8(number[0])
    fractional_part = fractional_part_from_10_to_8(number[1])
    res_number = whole_part + "." + fractional_part
    return res_number

def from_16_to_8(number):
    return from_10_to_8(from_16_to_10(number))

