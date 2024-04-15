def z10_1():
    import json
    with open("10.json", "r", encoding="utf8") as json_file:
        data = json.load(json_file)
    for d in data["products"]:
        print(f"Название: {d["name"]}")
        print(f"Цена: {d["price"]}")
        print(f"Вес: {d["weight"]}")
        if d["available"]:
            a = "В наличии"
        else:
            a = "Нет в наличии"
        print(a)
        print()

def z10_2():
    import json
    with open("json1.json", "r", encoding="utf8") as json_file:
        data = json.load(json_file)
    for d in data["products"]:
        print(f"Название: {d["name"]}")
        print(f"Цена: {d["price"]}")
        print(f"Вес: {d["weight"]}")
        if d["available"]:
            a = "В наличии"
        else:
            a = "Нет в наличии"
        print(a)
        print()

    new_p = {}
    new_p["name"] = input("Введите название продукта: ")
    new_p["price"] = input("Введите цену продукта: ")
    new_p["weight"] = input("Введите вес продукта: ")
    new_p["available"] = input("Этот товар в наличии? да/нет: ").lower() == "да"
    data["products"].append(new_p)
    print("Обновленное содержимое: ")
    with open("json1.json", "w") as json_file:
        json.dump(data, json_file)
    with open("json1.json", "r", encoding = "utf8") as json_file:
        new_data = json.load(json_file)
        for n in new_data["products"]:
            print(f"Название: {n["name"]}")
            print(f"Цена: {n["price"]}")
            print(f"Вес: {n["weight"]}")
            if n["available"]:
                b = "В наличии"
            else:
                b = "Нет в наличии"
            print(b)
            print()

def z10_3():
    en_ru_dict = {}
    # чтение данных из файла en-ru.txt
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()

        # обработка данных и заполнение словаря
        for line in data:
            words = line.strip().split(' - ')  # разделение ключа и значения
            english_word = words[0]  # переменная для английских слов
            if len(words) == 2:  # если для англ.слова сущ-ет перевод
                russian_translations = words[1].split(', ')  # отделяем каждое русское слово запятой, если слов несколько
                en_ru_dict[english_word] = russian_translations  # связывает англ.слово с переводами


    # сортировка словаря по алфавиту и вывод отсортированных данных
    sorted_en_ru_dict = dict(sorted(en_ru_dict.items()))
    with open('en-ru.txt', 'w', encoding='utf-8') as file:
        for english_word, russian_translations in sorted_en_ru_dict.items():
            file.write(f"{english_word} - {', '.join(russian_translations)}\n")

    # Создание русско-английского словаря
    ru_en_dict = {}
    for line in data:
        en_word, ru_translation = line.strip().split(' - ') #разделение ключа и значения
        ru_words = ru_translation.split(', ') #разделение слов в перечне
        for ru_word in ru_words:
            if ru_word in ru_en_dict: #проверка наличия русского слова в русско-английском словаре
                ru_en_dict[ru_word].append(en_word) #добавляем английское слово с список его переводов
            else:
                ru_en_dict[ru_word] = [en_word] #создание новой записи в словаре


    # Запись в файл ru-en.txt
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for ru_word in sorted(ru_en_dict.keys()): #проходимся по всем ключам (русским словам)
            en_words = ', '.join(ru_en_dict[ru_word]) #строка с английским переводом
            file.write(f'{ru_word} – {en_words}\n')

z10_3()

