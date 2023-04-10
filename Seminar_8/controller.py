import view
import model

def menu(db: dict, last_id: int) -> None: # меню
    while True:
        selection = view.show_menu()
        if selection == "":
            print("Пока - пока")
            break
        elif selection == "1":
            find_data = model.find_id(db, view.get_find_data())
            view.output_read(db, find_data)

        elif selection == "2":
            record = view.get_user_data()
            db, last_id = model.create(db, last_id, *record )

        elif selection == "3":
            find_data = model.find_id(db, view.get_find_data())                # определяем ID записи для изменения
            try:                                                               # обрабатываем исключение если записи нет в справочнике
                founder = db[find_data]                                        # получаем запись словаря которую надо изменить
                print(founder)                                                 # печатаем её
                if founder:
                    change_datas = view.get_user_data()                        # получаем кортеж для изменения словаря
                    print(change_datas)                                        # печатаем его
                    new_rec = {}                                               
                    new_rec = model.create(new_rec, find_data, *change_datas)  # создаём новую запись из кортежа
                    new_record = model.update_db(find_data, new_rec, founder)  # меняем старую запись на полученную - новую
                    db[find_data] = new_record                                 # обновляем справочник
            except: print("Искомая запись не найдена.")                        # обрабатываем исключение если записи нет в справочнике
  
        elif selection == "4":
            try:
                find_data = model.find_id(db, view.get_find_data())
                model.delete_value_db(db, find_data)
            except: print("Введённой записи не существует.")

        elif selection == "5":
            view.print_data(db)

        elif selection == "6":
            model.export_db(db, view.get_export_file_name())
            print("Экспортированные записи:")
            view.print_data(db)

        elif selection == "7":
            db, last_id = model.import_db(db, last_id, view.get_import_file_name())
            print("Импортированные записи:")
            view.print_data(db)

        elif selection == "8":
            break

        else:
            print("Недопустимый пункт меню.")