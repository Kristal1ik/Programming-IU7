def precedence(op):
    if op == '*':
        return 2
    if op == '+':
        return 1
    return 0


def apply_operator(operators, values):
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

        while (operators and precedence(operators[-1]) >= precedence(char)):
            apply_operator(operators, values)

        operators.append(char)
        i += 1

    while operators:
        apply_operator(operators, values)

    if not values:
        raise ValueError("Ошибка: выражение не содержит чисел.")

    return values[0]


def extract_and_evaluate(lines):
    for index in range(len(lines)):
        current_expression = ''
        result_line = ''  # Строка для хранения результата текущей строки

        for char in lines[index]:
            if char.isdigit() or char in '+* ':
                current_expression += char
            else:
                if current_expression:
                    try:
                        evaluated_result = evaluate_expression(current_expression)
                        result_line += str(evaluated_result)  # Добавляем результат в строку
                    except ValueError:
                        result_line += current_expression  # Если ошибка, добавляем исходное выражение
                    current_expression = ''
                result_line += char  # Добавляем текущий символ (буква или знак препинания)

        if current_expression:  # Обработка оставшегося выражения в конце строки
            try:
                evaluated_result = evaluate_expression(current_expression)
                result_line += str(evaluated_result)
            except ValueError:
                result_line += current_expression

        lines[index] = result_line  # Обновляем строку в списке
