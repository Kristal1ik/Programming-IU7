def delete_word(text, word):
    for i in range(len(text)):
        text[i] = text[i].replace(word, "")


def replace_word(text, word, word_replace):
    for i in range(len(text)):
        text[i] = text[i].replace(word, word_replace)


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

        # Проверяем каждое слово в текущем предложении
        for word in words:
            if shortest_word is None or len(word) < len(shortest_word):
                shortest_word = word
                min_sentence_index = index  # Сохраняем индекс текущего предложения

    return min_sentence_index, shortest_word


def finder(text, word):
    for i in text:
        if word in i:
            return True
