"""
Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б

Текстовый процессор
"""

from alignments import left, right, width
from words import delete_word, replace_word, finder, reserching_sentence
from polish_notation import extract_and_evaluate


def is_number(value):
    return isinstance(value, (int, float))


counter = 1


def text_out(text):
    global counter
    counter += 1
    print("-" * 100)
    for line in text:
        print(line)
    print("-" * 100)


little_prince = [
    "foo FOO test,",
    "bar",
    "foo bar! FOO BAR MAR 5+",
    "10 foo baarr, Снег СНЕГ 5+5 + 5 * 0 test, снеговик TEST!!!",
    "sentence."
]

menu = '''Меню:
1. Выровнять текст по левому краю.
2. Выровнять текст по правому краю.
3. Выровнять текст по ширине.н
4. Удаление всех вхождений заданного слова.
5. Замена одного слова другим во всём тексте.
6. Вычисление арифметических выражений над целыми числами внутри текста
(сложение и умножение).
7. Найти (вывести на экран) и затем удалить предложение с самым коротким словом.'''

max_length = max(len(i) for i in little_prince)
print(menu)
print("-" * 100)

while True:
    n = input("Выберите операцию над текстом: ")

    # Проверка на ввод числа
    while not n.isdigit() or not (1 <= int(n) <= 7):
        print("Номер должен находиться на отрезке [1;7]")
        n = input("Выберите операцию над текстом: ")

    n = int(n)  # Преобразуем введенное значение в int

    if counter % 3 == 0:
        print(menu)

    if n == 1:
        left(little_prince)
        text_out(little_prince)
    elif n == 2:
        right(little_prince, max_length)
        text_out(little_prince)
    elif n == 3:
        width(little_prince, max_length)
        text_out(little_prince)
    elif n == 4:
        word = input("Введите слово для удаления во всем тексте: ")
        while not finder(little_prince, word):
            print("Такого слова нет в тексте!")
            word = input("Введите слово для удаления во всем тексте: ")
        delete_word(little_prince, word)
        text_out(little_prince)
    elif n == 5:
        word_from = input("Введите слово, которое вы хотите заменить во всем тексте: ")
        while not finder(little_prince, word_from):
            print("Такого слова нет в тексте!")
            word_from = input("Введите слово, которое вы хотите заменить во всем тексте: ")
        word_to = input("Введите слово, на которое хотите заменить предыдущее слово: ")
        replace_word(little_prince, word_from, word_to)
        text_out(little_prince)
    elif n == 6:
        res = extract_and_evaluate(little_prince)
        text_out(res)
    elif n == 7:
        reserching_sentence(little_prince, 1)
        text_out(little_prince)
