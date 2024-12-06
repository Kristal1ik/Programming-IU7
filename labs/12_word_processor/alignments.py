def left(text):
    for i in range(len(text)):
        while text[i][0] == " ":
            text[i] = text[i][1:]
    return text


def right(text, length):
    for i in range(len(text)):
        while len(text[i]) != length:
            text[i] = " " + text[i]
    return text


def width(text, mx_len):
    for i in range(len(text)):
        text[i] = text[i].strip()

    for i in range(len(text)):
        if len(text[i]) > mx_len:
            mx_len = len(text[i])

    for i in range(len(text)):
        spaces_counter = text[i].count(' ')
        spaces_words = len(text[i]) - spaces_counter
        needed_spaces = mx_len - spaces_words
        counter_needed_spaces = needed_spaces // spaces_counter
        counter_needed_spaces_extra = needed_spaces % spaces_counter
        text[i] = text[i].replace(' ', ' ' * counter_needed_spaces)
        text[i] = text[i].replace(' ' * counter_needed_spaces, ' ' * (counter_needed_spaces + 1),
                                  counter_needed_spaces_extra)
