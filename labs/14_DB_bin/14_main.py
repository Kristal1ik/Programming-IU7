import os
import struct

RECORD_FORMAT = '50si20s20s'
RECORD_SIZE = struct.calcsize(RECORD_FORMAT)


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
        print("5. Удалить запись")
        print("6. Поиск по одному полю")
        print("7. Поиск по двум полям")
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
            delete_record()
        elif choice == '6':
            search_one_field()
        elif choice == '7':
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

    with open(filename, 'wb') as f:
        pass

    print("База данных инициализирована.")
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
        with open(filename, 'rb') as f:
            while True:
                record = f.read(RECORD_SIZE)
                if not record:
                    break
                name, members, last_name, first_name = struct.unpack(RECORD_FORMAT, record)
                print(
                    f"{name.decode('utf-8').strip()} | {members} | {last_name.decode('utf-8').strip()} | {first_name.decode('utf-8').strip()}")

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

    index = int(input("Введите индекс для добавления записи: "))

    name = input("Введите название команды (до 50 символов): ").encode('utf-8').ljust(50, b'\x00')
    members = int(input("Введите количество участников (число): "))
    last_name = input("Введите фамилию тимлида (до 20 символов): ").encode('utf-8').ljust(20, b'\x00')
    first_name = input("Введите имя тимлида (до 20 символов): ").encode('utf-8').ljust(20, b'\x00')

    record = struct.pack(RECORD_FORMAT, name, members, last_name, first_name)

    records = []
    with open(filename, 'rb') as f:
        while True:
            record_data = f.read(RECORD_SIZE)
            if not record_data:
                break
            records.append(record_data)

    if index < 0 or index > len(records):
        print(f"Ошибка: некорректный индекс {index}.")
        return

    records.insert(index, record)

    with open(filename, 'wb') as f:
        for rec in records:
            f.write(rec)

    print("Запись добавлена!")
    output_dash()


def delete_record():
    output_dash()
    if not filename:
        print("Сначала выберите файл для работы.")
        output_dash()
        return

    if not has_permission_read(filename) or not has_permission_write(filename):
        print("Ошибка: недостаточно прав для чтения или записи файла.")
        return

    try:
        index = int(input("Введите номер записи для удаления (начиная с 0): "))
    except ValueError:
        print("Ошибка: Неверный формат номера записи.")
        return

    try:
        with open(filename, 'rb') as infile:
            with open(filename + ".tmp", 'wb') as outfile:
                record_size = struct.calcsize(RECORD_FORMAT)
                for i, record in enumerate(iter(lambda: infile.read(record_size), b'')):
                    if i != index:
                        outfile.write(record)
        os.replace(filename + ".tmp", filename)
        print(f"Запись номер {index} удалена!")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        if os.path.exists(filename + ".tmp"):
            os.remove(filename + ".tmp")


def search_one_field():
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

    with open(filename, 'rb') as f:

        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break

            name, members, last_name, first_name = struct.unpack(RECORD_FORMAT, record)

            conditions_met = (
                    (field1_name == "name" and name.decode('utf-8').strip() == field1_value) or
                    (field1_name == "members" and str(members) == field1_value) or
                    (field1_name == "leader_lastname" and last_name.decode('utf-8').strip() == field1_value) or
                    (field1_name == "leader_firstname" and first_name.decode('utf-8').strip() == field1_value)
            )
            if conditions_met:
                print(
                    f"{name.decode('utf-8').strip()} | {members} | {last_name.decode('utf-8').strip()} | {first_name.decode('utf-8').strip()}")
            else:
                print("Ничего не найдено!")


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

    with open(filename, 'rb') as f:
        found = False

        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break

            name, members, last_name, first_name = struct.unpack(RECORD_FORMAT, record)

            conditions_met = (
                    (field1_name == "name" and name.decode('utf-8').strip() == field1_value) or
                    (field1_name == "members" and str(members) == field1_value) or
                    (field1_name == "leader_lastname" and last_name.decode('utf-8').strip() == field1_value) or
                    (field1_name == "leader_firstname" and first_name.decode('utf-8').strip() == field1_value)
            )

            conditions_met_2nd_field = (
                    (field2_name == "name" and name.decode('utf-8').strip() == field2_value) or
                    (field2_name == "members" and str(members) == field2_value) or
                    (field2_name == "leader_lastname" and last_name.decode('utf-8').strip() == field2_value) or
                    (field2_name == "leader_firstname" and first_name.decode('utf-8').strip() == field2_value)
            )

            if conditions_met and conditions_met_2nd_field:
                found = True
                print(
                    f"{name.decode('utf-8').strip()} | {members} | {last_name.decode('utf-8').strip()} | {first_name.decode('utf-8').strip()}")

        if not found:
            print("Ничего не найдено!")


if __name__ == "__main__":
    filename = ''
    main_menu()
