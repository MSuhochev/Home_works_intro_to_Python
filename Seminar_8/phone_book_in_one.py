# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара 
# и реализовать  Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# ##### Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода. 
#     Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# - Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# - Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
#   Берем первое совпадение по фамилии.
# - Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# - Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# ```(*)``` **Усложнение.**
# - Сделать тесты для функций
# - Разделить на model-view-controller

#phone_book = {'Ляшенко Дмитрий': ['+79284316582', 'семья'], 'Ляшенко Виктория': ['+79002436454', 'семья']}
#phone_book = [{'Ляшенко Дмитрий': ['+79284316582', 'семья']}, {'Ляшенко Виктория': ['+79002436454', 'семья']}]
#phone_book = [{1:['Ляшенко Дмитрий', '+79284316582', 'семья']}, {2: ['Ляшенко Виктория', '+79002436454', 'семья']}]
#phone_book = [{'surname': 'Ляшенко', 'name': 'Дмитрий', 'phone': '+79284316582', 'desription': 'семья'}, {'surname':'Ляшенко', 'name': 'Виктория', 'phone': '+79002436454', 'desription': 'семья'}]

phone_book = [{1: {'surname': 'Ляшенко', 'name': 'Дмитрий', 'phone': '+79284316582', 'desription': 'семья'}}, {2: {'surname':'Ляшенко', 'name': 'Виктория', 'phone': '+79002436454', 'desription': 'семья'}}]
phonebook = {}
phonebook_last_id = 0

#!def create(db: dict, _id: int, surname: str, name: str, phone: str, description: str) -> tuple: #  создание записи словаря возвращает dict(phone_book)
    db[_id] = {"surname": surname, "name": name, "phone": phone, "description": description}
    _id += 1
    return db, _id

#!def find_id(db: dict, find_filter: str) -> int: # поиск заданной записи в словаре возвращает _id записи
    for _id in db:
        if find_filter.lower() in db[_id]['surname'].lower():
            return _id

#!def output_read(db: dict, _id: int) -> str: # вывод найденной записи на экран
    print(f'{db[_id]}')

#!def get_find_data() -> str: # получение от пользователя параметров поиска в словаре (ключ фамилия)
    find_filter = input("Введите фамилию: ")
    return find_filter

#!def update_db(find_data, new_rec: dict, old_rec: dict) -> dict: # обновление существующей записи в словаре
    tmp_rec = new_rec[0][find_data]
    # print(new_rec)
    # print(old_rec)
    for _id in new_rec[0][find_data]:
        tmp_rec[_id] = new_rec[0][find_data][_id] if new_rec[0][find_data][_id] != "" else old_rec[_id]
    return tmp_rec

#!def delete_value_db(db: dict, find_data) -> dict: # удаление существующей записи в словаре
    db.pop(find_data)
    return db

#!def get_user_data() -> tuple: # получение от пользователя значений записи словаря
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    description = input("Введите описание контакта: ")
    return surname, name, phone, description

#!def print_data(db: dict) -> None: # вывод всех имеющихся записей на экран
    for _id, data in db.items():
        print(f'[{_id}: {data["surname"]} | {data["name"]} | {data["phone"]} | {data["description"]}]')

#!def export_db(db: dict, filepath: str, delimeter: str = "#") -> None: # экспорт записей словаря в файл
    with open(filepath, "w", encoding="utf-8") as file:
        for _id, data in db.items():
            file.write(f'{data["surname"]}{delimeter}{data["name"]}{delimeter}{data["phone"]}{delimeter}{data["description"]}\n')

#!def import_db(db: dict, last_id: int, filepath: str, delimeter: str = "#") -> tuple: # импорт записей в словарь из внешнего источника
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            _data = line.strip().split(delimeter)
            db[last_id] = {"surname": _data[0], "name": _data[1], "phone": _data[2], "description": _data[3]}
            last_id += 1
    return db, last_id

#!def get_file_name() -> str: # метод для инициализации файла импорта/экспорта
    return input("Введите имя файла для записи: ")

#!def menu(db: dict, last_id: int) -> None: # меню
    while True:
        print("Возможные действия:")
        print("1. Найти запись: ")
        print("2. Создать запись.")
        print("3. Изменить запись.")
        print("4. Удалить существующую запись.")
        print("5. Вывести имеющиеся данные.")
        print("6. Экспортировать данные в файл.")
        print("7. Импортировать данные из файла.")
        print("8. Выход.")
        user_input = input("Введите действие > ")

        if user_input == "1":
            find_data = find_id(db, get_find_data())
            output_read(db, find_data)

        elif user_input == "2":
            record = get_user_data()
            db, last_id = create(db, last_id, *record )

        elif user_input == "3":
            find_data = find_id(db, get_find_data())                           # определяем ID записи для изменения
            founder = db[find_data]                                            # получаем запись словаря которую надо изменить
            print(founder)                                                     # печатаем её
            if founder:
                change_datas = get_user_data()                                 # получаем кортеж для изменения словаря
                print(change_datas)  
                new_rec = {}                                                   # печатаем его
                new_rec = create(new_rec, find_data, *change_datas)            # создаём новую запись из кортежа
                #print(new_rec[find_data])                                     # печатаем её
                #rec = create_new(*get_find_data())
                new_record = update_db(find_data, new_rec, founder)            # меняем с тарую запись на полученную - новую
                db[find_data] = new_record                                    
        
        elif user_input == "4":
            find_data = find_id(db, get_find_data())
            delete_value_db(db, find_data)

        elif user_input == "5":
            print_data(db)

        elif user_input == "6":
            export_db(db, get_file_name())

        elif user_input == "7":
            #db, last_id = import_db(db, last_id, get_file_name())
            db, last_id = import_db(db, last_id, "data2.txt")

        elif user_input == "8":
            break

menu(phonebook, phonebook_last_id)      