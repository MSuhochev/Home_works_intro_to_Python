import view

def find_id(db: dict, find_filter: str) -> int: # поиск заданной записи в словаре возвращает _id записи
    for _id in db:
        if find_filter.lower() in db[_id]['surname'].lower():
            return _id
        
def create(db: dict, _id: int, surname: str, name: str, phone: str, description: str) -> tuple: #  создание записи словаря возвращает dict(phone_book)
    db[_id] = {"surname": surname, "name": name, "phone": phone, "description": description}
    _id += 1
    return db, _id

def update_db(find_data, new_rec: dict, old_rec: dict) -> dict: # обновление существующей записи в словаре
    tmp_rec = new_rec[0][find_data]
    for _id in new_rec[0][find_data]:
        tmp_rec[_id] = new_rec[0][find_data][_id] if new_rec[0][find_data][_id] != "" else old_rec[_id]
    return tmp_rec

def delete_value_db(db: dict, find_data) -> dict: # удаление существующей записи в словаре
    db.pop(find_data)
    _id = 0
    for _id in db:
        _id +=1
        return db

def export_db(db: dict, filepath: str, delimeter: str = "#") -> None: # экспорт записей словаря в файл
    with open(filepath, "w", encoding="utf-8") as file:
        for _id, data in db.items():
            file.write(f'{data["surname"]}{delimeter}{data["name"]}{delimeter}{data["phone"]}{delimeter}{data["description"]}\n')

def import_db(db: dict, last_id: int, filepath: str, delimeter: str = "#") -> tuple: # импорт записей в словарь из внешнего источника
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            _data = line.strip().split(delimeter)
            db[last_id] = {"surname": _data[0], "name": _data[1], "phone": _data[2], "description": _data[3]}
            last_id += 1
    return db, last_id
