"""

Выполнила: Коробовцева Ольга
Группа: ИУ7-11Б


Текстовый процессор

"""

from alignments import left, right, width
from words import delete_word, replace_word, find_the_sentence_with_the_shortest_word, finder
from polish_notation import extract_and_evaluate

counter = 1


def text_out(text):
    global counter
    counter += 1
    print("-" * 100)
    for _ in text:
        print(_)
    print("-" * 100)


little_prince = [
    "     Когда мне было 1 + 5 или 2 *  3 лет, в книге под названием «Правдивые истории»,",
    "где рассказывалось про девственные леса, я увидел однажды удивительную картинку. На",
    "картинке огромная змея — удав — глотала хищного зверя. Вот как это было нарисовано.",
    "В книге говорилось: «Удав заглатывает свою жертву целиком, не жуя. После",
    "этого он уже не может шевельнуться и спит полгода подряд, пока не переварит пищу». Я",
    "много раздумывал о полной приключений жизни джунглей и тоже нарисовал цветным карандашом свою первую",
    "картинку. Это был мой рисунок №0+1*1. Вот что я нарисовал. "]

menu = '''Меню:
1. Выровнять текст по левому краю.
2. Выровнять текст по правому краю.
3. Выровнять текст по ширине.
4. Удаление всех вхождений заданного слова.
5. Замена одного слова другим во всём тексте.
6. Вычисление арифметических выражений над целыми числами внутри текста
(сложение и умножение).
7. Найти (вывести на экран) и затем удалить предложение с самым коротким словом.'''

max_length = max(len(i) for i in little_prince)
print(menu)
print("-" * 100)

while True:
    n = int(input("Выберите операцию над текстом: "))
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
        while not (finder(little_prince, word)):
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
        extract_and_evaluate(little_prince)
        text_out(little_prince)
    elif n == 7:
        answer = find_the_sentence_with_the_shortest_word(little_prince)
        print(f"Предложение с самым коротким словом: {little_prince[answer[0]]}")
        print(f"Самое короткое слово: {answer[1]}")
        print("Текст после удаления предложения с самым коротким словом:")
        little_prince = little_prince[0:answer[0]] + little_prince[answer[0] + 1:]
        text_out(little_prince)
    else:
        print("Номер должен находиться на отрезке [1;7]")
        n = int(input("Выберите операцию над текстом: "))
