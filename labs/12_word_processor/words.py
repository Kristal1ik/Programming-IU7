from alignments import left, right, width


def delete_word(text, word):
    word_lower = word.lower()
    for i in range(len(text)):
        lst = []
        words = text[i].split()
        for w in words:
            if not(w == word_lower or w == word_lower + "," or w.lower() == word_lower + "!!!"):
                lst.append(w)
        # text[i] = ' '.join([w for w in words if w.lower() != word_lower or w.lower != word_lower + "," or w.lower != word_lower +"!"])
        text[i] = " ".join(lst)
    return text


def replace_word(text, word, word_replace):
    word_lower = word.lower()
    for i in range(len(text)):
        new_line = ""
        current_word = ""
        for j in range(len(text[i])):
            char = text[i][j]
            if char.isalnum():
                current_word += char
            else:
                if current_word.lower() == word_lower:
                    new_line += word_replace
                else:
                    new_line += current_word
                new_line += char
                current_word = ""
        if current_word.lower() == word_lower:
            new_line += word_replace
        else:
            new_line += current_word

        text[i] = new_line


def find_the_sentence_with_the_shortest_word(text):
    min_sentence_index = -1
    shortest_word = None
    flag_whitespace = False
    sentences = []
    signs = ".!?"
    current_sentence = ""
    for i in range(len(text)):
        string = text[i]

        if flag_whitespace:
            string = " " + string
        for j in range(len(string)):
            char = string[j]
            if j == len(string) - 1 and char not in signs:
                flag_whitespace = True
            if char in signs:
                sentences.append(current_sentence)
                current_sentence = ""
            else:
                current_sentence += char
    for index, sentence in enumerate(sentences):
        words = []
        current_word = ""

        # Извлекаем слова из текущего предложения
        for char in sentence:
            if char.isalnum() or char in '+*':
                current_word += char  # Собираем текущее слово
            else:
                if current_word:  # Если текущее слово не пустое
                    words.append(current_word)
                    current_word = ""

        # Добавляем последнее слово, если оно есть
        if current_word:
            words.append(current_word)

        for word in words:
            if (shortest_word is None or len(word) < len(shortest_word)) and word.isalpha():
                shortest_word = word
                min_sentence_index = index
    print(sentences[min_sentence_index])
    return sentences[min_sentence_index], shortest_word, min_sentence_index, remove_substring(text, sentences[
        min_sentence_index])


def finder(text, word):
    for i in text:
        if word in i:
            return True


def align_text(mode, t) -> 'Удаление лишних пробелов между словами':
    if mode != 1:
        for i in range(len(t)):
            while '  ' in t[i]:
                t[i] = t[i].replace('  ', ' ')
        return t


def printing_mode(t, mode) -> 'Вывод полученного текста с исходным выравниванием':
    if mode == 1:
        left(t)
    elif mode == 2:
        right(t, mode)
    else:
        width(t, 10000)


def reserching_sentence(t, mode):
    sentence = ''  # Собранное предложение
    mx_sentence = ''  # Нужное предложение
    word = ''  # Собранное слово
    # Начальные индексы для предложений
    start_i = 0
    start_j = 0
    mx_start_i = 0
    mx_finish_i = 0
    mx_start_j = 0
    mx_finish_j = 0
    words = []
    mn_len_word = 10 ** 8
    mn_all_word = 10 ** 8
    for i in range(len(t)):
        j = 0  # Индекс символов строки
        for x in t[i]:
            sentence += x
            if x == ' ':  # Если дошли до разделителя
                if len(word) < mn_len_word:  # Проверяем нужное условие
                    mn_len_word = len(word)

            elif x in '.!?':  # Если дошли до конца предложения
                if x == ' ':  # Если дошли до разделителя
                    if len(word) < mn_len_word:  # Проверяем нужное условие
                        mn_len_word = len(word)

                finish_i = i
                finish_j = j

                if mn_len_word < mn_all_word:  # Ищем предложение с максимальным количеством нужных слов
                    mn_all_word = mn_len_word

                    mx_sentence = sentence
                    mx_start_i = start_i
                    mx_start_j = start_j
                    mx_finish_i = finish_i
                    mx_finish_j = finish_j

                # Изменяем начальные счетчики для следующего предложения
                if j + 1 >= len(t[i]):
                    start_i = i + 1
                else:
                    start_i = i
                start_j = j + 1
                sentence = ''
            else:
                word += x
                words.append(word)
            j += 1
    if mx_start_j == mx_finish_j == mx_finish_i == mx_start_i == 0:
        print('Таких предложений нет')
    else:
        print("Предложение с самым коротким словом:",
              mx_sentence)
        print()

        if mx_start_i == mx_finish_i:  # Если предложение находится в одной строке
            t[mx_start_i] = t[mx_finish_i][:mx_start_j] + t[mx_finish_i][mx_finish_j + 1:]
            if not t[mx_start_i]:  # Удаляем пустую строку
                t = t[:mx_start_i] + t[mx_start_i + 1:]
        else:  # Если предложение растянулось на несколько строк
            t[mx_start_i] = t[mx_start_i][:mx_start_j]
            t[mx_finish_i] = t[mx_finish_i][mx_finish_j + 2:]
            if not t[mx_start_i]:  # Удаляем пустую строку
                t = t[:mx_start_i] + t[mx_start_i + 1:]
            elif not t[mx_finish_i]:
                t = t[:mx_finish_i] + t[mx_finish_i + 1:]
        print('Полученный текст: ')
        printing_mode(t, mode)
