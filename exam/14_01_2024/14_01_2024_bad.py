"""

Дан файл in.txt в нем записаны предложения, в предложениях появляются вещественные 16-ричные числа,
гарантируется, что каждое число отделено пробелами от других символов. Необходимо прочитать файл
in и в файл out строки, в которых 16-чные заменить на 8-чные. Далее необходимо создать бинарный файл,
 в который записать кол во предложений, затем кол во слов в каждом предложении друг за другом.

Подводные камни: предложения на разных строчках, числа нужно обрабатывать и целочисленные тоже надо обрабатывать,
стоит учитывать унарные плюсы и минусы

"""


def from_16_to_2_triad(number):
    if "," in number:
        number = number.split(",")
        whole_part = bin(int(number[0], 16))[2:]
        fractional_part = bin(int(number[1], 16))[2:]
    else:
        whole_part = bin(int(number, 16))[2:]
        fractional_part = ""
    if len(whole_part) % 3 != 0:
        whole_part = whole_part.rjust(len(whole_part) + (3 - (len(whole_part)) % 3), "0")
    if len(fractional_part) % 3 != 0:
        fractional_part = fractional_part.ljust(len(fractional_part) + (3 - (len(fractional_part)) % 3), "0")
    return whole_part, fractional_part


def from_2_to_8_tetrad(number):
    if number[1] != "":
        whole_part = number[0]
        fractional_part = number[1]
    else:
        whole_part = number[0]
        fractional_part = ""

    whole_part_oct = ""
    fractional_part_oct = ""
    for i in range(0, len(whole_part), 3):
        whole_part_oct += oct(int(whole_part[i:i + 3], 2))[2:]
    for i in range(0, len(fractional_part), 3):
        fractional_part_oct += oct(int(fractional_part[i:i + 3], 2))[2:]
    if fractional_part_oct != "":
        return whole_part_oct + "," + fractional_part_oct
    return whole_part_oct


def from_16_to_8(number):
    return from_2_to_8_tetrad(from_16_to_2_triad(number))


def check_if_not_16(number):
    alph = "QWRTYUIOPSGHJKLZXVNM"
    for i in number:
        if i in alph:
            return False
    return True

with open("in.txt", "r", encoding="utf-8") as f_in:
    with open("out.txt", "w+", encoding="utf-8") as f_out:
        sentence = ""
        word = ""
        word_is_written = False
        for line in f_in:
            for item in line:
                if item not in " \n\t":
                    word += item
                else:
                    if len(word) > 0 and word[0] in "1234567890ABCDEF":
                        if check_if_not_16(word):
                            word = from_16_to_8(word)
                    sentence += word
                    sentence += item
                    word = ''
                if item in ".!?":
                    sentence += word
                    f_out.write(sentence)
                    sentence = ""
                    word = ""

