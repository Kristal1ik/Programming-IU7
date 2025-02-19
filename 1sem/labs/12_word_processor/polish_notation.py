def precedence(op):
    if op == '*':
        return 2
    if op == '+':
        return 1
    return 0


def apply_operator(operators, values):
    if len(values) < 2:
        raise ValueError("Ошибка: недостаточно значений для выполнения операции.")

    right = values.pop()
    left = values.pop()
    operator = operators.pop()

    if operator == '+':
        values.append(left + right)
    elif operator == '*':
        values.append(left * right)


def evaluate_expression(expression):
    values = []
    operators = []

    i = 0
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            continue

        while operators and precedence(operators[-1]) >= precedence(char):
            apply_operator(operators, values)

        operators.append(char)
        i += 1

    while operators:
        apply_operator(operators, values)

    if not values:
        raise ValueError("Ошибка: выражение не содержит чисел.")
    return values[0]


def remove_empty_lines(lines):
    return [line for line in lines if line.strip() != '']


def remove_lines_with_text(lines, text_to_remove):
    return [line for line in lines if text_to_remove not in line]


def extract_and_evaluate(lines):
    current_expression = ''
    lines = remove_empty_lines(lines)
    for index in range(len(lines)):
        result_line = ''  # Строка для хранения результата текущей строки
        line_contains_operation = False  # Флаг для отслеживания наличия арифметической операции

        for char in lines[index]:
            if char.isdigit() or char in '+* ':
                current_expression += char
                line_contains_operation = True  # Установить флаг, если есть операция
            else:
                if current_expression:
                    try:
                        evaluated_result = evaluate_expression(current_expression)
                        result_line += str(evaluated_result)  # Добавляем результат в строку
                    except ValueError:
                        result_line += current_expression  # Если ошибка, добавляем исходное выражение
                    current_expression = ''
                result_line += char  # Добавляем текущий символ (буква или знак препинания)

        if current_expression:
            try:
                evaluated_result = evaluate_expression(current_expression)
                result_line += str(evaluated_result)
            except ValueError:
                result_line += current_expression

        lines[index] = result_line

        if line_contains_operation:
            lines[index] = lines[index].replace(current_expression, '',
                                                1).strip()  # Удаляем первую встреченную операцию
    return lines


# Пример использования
little_prince = [
    "foo test,",
    "bar",
    "foo bar! FOO BAR MAR",
    "foo baarr, Снег СНЕГ 5 +", "",
    "5 test, снеговик TEST!!!",
    "sentence."
]

# Вызов функции для извлечения и оценки выражений
result_lines = extract_and_evaluate(little_prince)
for line in result_lines:
    print(line)
