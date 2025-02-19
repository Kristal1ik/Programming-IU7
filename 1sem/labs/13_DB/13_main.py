import os


def has_permission_read(file_path):
    return os.access(file_path, os.R_OK)


def has_permission_write(file_path):
    return os.access(file_path, os.W_OK)


def main_menu():
    while True:
        print("1. Выбрать файл для работы")
        print("2. Инициализировать базу данных")
        print("3. Вывести содержимое базы данных")
        print("4. Добавить запись")
        print("5. Поиск по одному полю")
        print("6. Поиск по двум полям")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            select_file()
        elif choice == '2':
            initialize_database()
        elif choice == '3':
            display_database()
        elif choice == '4':
            add_record()
        elif choice == '5':
            search_one_field()
        elif choice == '6':
            search_two_fields()
        elif choice == '0':
            break
        else:
            print("Нет такого варианта!")


def output_dash():
    print("-" * 50)


def select_file():
    global filename
    output_dash()
    filename = input("Введите имя файла: ")
    if os.path.isdir(filename):
        print("Ошибка: указанный путь является директорией.")
        filename = ''
    output_dash()


def initialize_database():
    output_dash()
    if not filename:
        print("Сначала выберите файл для работы.")
        output_dash()
        return

    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'w+') as f:
        f.write("name;members;leader_lastname;leader_firstname\n")

    print("Если захотите прекратить ввод, введите -1")
    while True:
        print(
            "Введите следующие данные через ';': название команды, количество участников, фамилия тимлида, имя тимлида:")
        data = input()

        if data == "-1":
            break

        if ';' in data:
            data = data.split(";")
            if len(data) == 4:
                name = data[0]
                members = data[1]
                last_name = data[2]
                first_name = data[3]
                if members.isdigit():
                    with open(filename, 'a') as f:
                        f.write(f"{name};{members};{last_name};{first_name}\n")
                        print("Запись добавлена!")
                else:
                    print("Введено некорректное количество участников команды (поле 'members')")
            else:
                print("Введены некорректные данные! Ожидается 4 поля.")
        else:
            print("Введены некорректные данные! Используйте ';' как разделитель.")
    output_dash()


def display_database():
    output_dash()
    if not filename:
        print("Сначала выберите файл для работы.")
        output_dash()
        return
    if not has_permission_read(filename):
        print("Ошибка: недостаточно прав для чтения файла.")
        return

    try:
        with open(filename, 'r') as f:
            headers = f.readline().strip().split(";")

            print("{:<50} {:<10} {:<20} {:<20}".format(headers[0], headers[1], headers[2], headers[3]))
            output_dash()

            for line in f:
                fields = line.strip().split(";")
                if len(fields) == 4:
                    print("{:<50} {:<10} {:<20} {:<20}".format(fields[0], fields[1], fields[2], fields[3]))
                else:
                    print("Неверный формат строки:", line.strip())

    except FileNotFoundError:
        print("Файл не найден!")

    output_dash()


def add_record():
    output_dash()
    if not filename:
        print("Сначала выберите файл для работы.")
        output_dash()
        return

    if not has_permission_write(filename):
        print("Ошибка: недостаточно прав для записи в файл.")
        return

    print("Введите следующие данные через ';': название команды, количество участников, фамилия тимлида, "
          "имя тимлида:")

    data = input().split(';')

    if len(data) == 4:
        name = data[0]
        members = data[1]
        last_name = data[2]
        first_name = data[3]

        if members.isdigit():
            with open(filename, 'a') as f:
                f.write(f"{name};{members};{last_name};{first_name}\n")
                print("Запись добавлена!")

        else:
            print("Введено некорректное количество участников команды (поле 'members')")

    else:
        print("Введены некорректные данные!")

    output_dash()


def search_one_field():
    output_dash()
    if not filename:
        print("Сначала выберите файл для работы.")
        output_dash()
        return

    if not has_permission_read(filename):
        print("Ошибка: недостаточно прав для чтения файла.")
        return

    field_name = input(
        "Введите имя поля для поиска ('name', 'members', 'leader_lastname', 'leader_firstname'): ")
    field_value = input("Введите значение для поиска: ")

    with open(filename, 'r') as f:
        headers = f.readline().strip().split(';')

        if field_name not in headers:
            print(f"Ошибка: поле '{field_name}' не найдено в заголовках.")
            return

        field_index = headers.index(field_name)

        found = False
        for line in f:
            fields = line.strip().split(';')
            if len(fields) > field_index and fields[field_index] == field_value:
                found = True
                print(line.strip())

        if not found:
            print("Ничего не найдено!")

    output_dash()


def search_two_fields():
    output_dash()
    if not filename:
        print("Сначала выберите файл для работы.")
        output_dash()
        return

    if not has_permission_read(filename):
        print("Ошибка: недостаточно прав для чтения файла.")
        return

    field1_name = input(
        "Введите имя первого поля для поиска ('name', 'members', 'leader_lastname', 'leader_firstname'): ")
    field1_value = input("Введите значение для первого поля: ")

    field2_name = input("Введите имя второго поля для поиска: ")
    field2_value = input("Введите значение для второго поля: ")

    with open(filename, 'r') as f:
        headers = f.readline().strip().split(';')

        if field1_name not in headers or field2_name not in headers:
            print(f"Ошибка: одно или оба поля '{field1_name}' или '{field2_name}' не найдены в заголовках.")
            return
        field1_index = headers.index(field1_name)
        field2_index = headers.index(field2_name)

        found = False
        for line in f:
            fields = line.strip().split(';')
            if len(fields) > max(field1_index, field2_index):
                if fields[field1_index] == field1_value and fields[field2_index] == field2_value:
                    found = True
                    print(line.strip())

        if not found:
            print("Ничего не найдено!")

    output_dash()


filename = ''
main_menu()
