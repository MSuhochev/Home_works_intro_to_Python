
def output_read(db: dict, _id: int) -> str: # вывод найденной записи на экран
    try: print(f'{db[_id]}')
    except: print("Такой записи не существует.")

def get_find_data() -> str: # получение от пользователя параметров поиска в словаре (ключ фамилия)
    find_filter = input("Введите фамилию: ")
    return find_filter

def get_user_data() -> tuple: # получение от пользователя значений записи словаря
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание контакта: ")
    return surname, name, phone, description

def print_data(db: dict) -> None: # вывод всех имеющихся записей на экран
    for _id, data in db.items():
        print(f'[{_id}: {data["surname"]} | {data["name"]} | {data["phone"]} | {data["description"]}]')

def get_export_file_name() -> str: # получение имени для инициализации файла экспорта
    return input("Введите имя файла для записи: ")

def get_import_file_name() -> str: # получение имени для инициализации файла импорта
    return input("Введите имя файла для считывания: ")

def show_menu() -> str: # вывод меню в консоль
    print("*"*20)
    print("Возможные действия:")
    print("1. Найти запись: ")
    print("2. Создать запись.")
    print("3. Изменить запись.")
    print("4. Удалить существующую запись.")
    print("5. Вывести имеющиеся данные.")
    print("6. Экспортировать данные в файл.")
    print("7. Импортировать данные из файла.")
    print("8. Выход.")
    return input("Введите действие > ")