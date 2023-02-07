"""Менеджер паролей."""

import json
import string
import random

letters = string.ascii_letters + string.digits + "!_?"
vowels = "aeyuioj"  # Гласные буквы.
consonants = "mctxhvnfbrzslgdkwqp"  # Согласные буквы.


def load_db(filename):
    """
    Функция загрузки данных из файла.
    :param filename: Название файла.
    :return: Возврат файла.
    """
    with open(filename) as file:  # Открываем файл на чтение.
        db = json.load(file)

    return db


def save_db(filename, db):
    """
    Функция сохранения данных в файл.
    :param filename: Название файла.
    :param db: Данные файла.
    """
    with open(filename, "w") as file:  # Сохранение файла на запись.
        json.dump(db, file, indent=2)


def add_pass(db):
    """
    Функция запроса данных от пользователя. Данные записываются по форме представленной ниже.
    :param db: Данные файла.
    """
    site = input("Введите название сайта: ")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    db.append(
        {
            "login": login,
            "password": password,
            "site": site
        },
    )


def change(subj, prev_subj):
    """
    Функция для смены записи.
    :param subj: Новое значение.
    :param prev_subj: Предыдущее значение.
    :return: Возврат предыдущего или нового значения.
    """
    ask = input(f"Ввести новое значение: ({subj}) Текущее: ({prev_subj})")  # Спрашиваем у пользователя.
    if ask == "":  # Если при запросе пустая строка, то:
        return prev_subj  # возвращаем предыдущее значение.
    else:
        return ask  # Если не пустая, то записываем новое значение.


def change_pass(info):
    """
    Функция записи данных.
    :param info: Имеет три вида входящих данных: login, password или site.
    """
    info["site"] = change("Название сайта", info["site"])  # Вызов функции с арг: "НОВОЕ значение" и "ТЕКУЩЕЕ значение".
    info["login"] = change("Логин", info["login"])  # Вызов функции с арг: "НОВОЕ значение" и "ТЕКУЩЕЕ значение".
    info["password"] = change("Пароль", info["password"])  # Вызов функции с арг: "НОВОЕ значение" и "ТЕКУЩЕЕ значение".


def compare(string_1, string_2):
    """
    Функция для сравнения символов.
    :param string_1: Строка 1.
    :param string_2: Строка 2.
    :return: Возврат если длина более 0.
    """
    str_1 = set(string_1)  # Строку 1 переделываем во множество.
    str_2 = set(string_2)  # Строку 2 переделываем во множество.
    inter = str_1.intersection(str_2)  # Делаем пересечение двух множеств для уникальности.

    return len(inter) > 0


def gen_pass(length):
    """
    Функция генерации и сравнение на уникальность с условиями.
    :param length: Длина пароля.
    :return: Возврат если условия не соблюдены.
    """
    while True:
        res = ""
        for i in range(length):  # В цикле перебираем по длине.
            res += random.choice(letters)  # Генерируем уникальные символы из заданных.

        bools = [compare(res, string.ascii_lowercase),  # Должны быть, буквы в нижнем регистре.
                 compare(res, string.ascii_uppercase),  # Должны быть, буквы в верхнем регистре.
                 compare(res, string.digits),  # Должны быть, цифры.
                 compare(res, "!_?"),  # Должны быть, символы.
                 res[0] not in string.ascii_uppercase  # Первым символом не может быть заглавная буква.
                 ]

        if all(bools):
            return res


def gen_easy_pass(length):
    """
    Функция создания упрощенного пароля.
    :param length: Длина пароля.
    :return: Если условия не соблюдены, то возврат.
    """
    res = ""
    for i in range(length - 3):  # Проходим циклом по длине пароля - 3 символа (они будут цифрами).
        if i % 2 == 0:  # Если четный, то:
            res += random.choice(consonants)  # согласные буквы добавляются.
        else:
            res += random.choice(vowels)  # либо гласные.

    for i in range(3):  # Добавляем к генерируемому паролю 3 цифры.
        res += random.choice(string.digits)

    return res


def add_and_gen(db):
    """
    Функция добавления и генерации пароля.
    :param db: Данные файла.
    """
    site = input("Введите название сайта: ")  # Название сайта.
    login = input("Введите логин: ")  # Логин пользователя.
    length = int(input("Введите длину пароля: "))  # Длина пароля.
    pass_level = input("Генерировать сложный пароль ? (y/n)")  # Уровень сложности пароля = сложный (y) или простой (n).
    if "y" in pass_level.lower():  # Если ответ: "y"
        password = gen_pass(length)  # Генерируем сложный пароль.
    else:
        password = gen_easy_pass(length)  # Генерируем легкий пароль.

    db.append(
        {
            "login": login,
            "password": password,
            "site": site
        },
    )


def show(info, num):
    """
    Функция красивого вывода на экран.
    :param info: Информация об аккаунте.
    :param num: Порядковый номер в таблице.
    """
    print(f"| {num:3} | {info['site']:15} | {info['login']:15} | {info['password']:15} |")


def search(db):
    """
    Функция поиска сайта.
    :param db: Данные файла.
    """
    site = input("Введите название сайта: ")  # Запрос названия сайта.
    results = []  # Список с результатами.
    for info in db:  # Запускаем цикл.
        if site in info["site"]:  # Если сайт есть в инфо, то:
            results.append(info)  # добавляем в список results.

    for num, info in enumerate(results):  # Проходим циклом.
        show(info, num)  # Выводим инфо и порядковый номер.

    user_intake = pass_mode()  # Пользовательский ввод.
    if user_intake == "1":  # Изменить пароль.
        num = int(input("Введите номер: "))
        info = results[num]
        change_pass(info)
    elif user_intake == "2":  # Удалить пароль.
        num = int(input("Введите номер: "))
        db.remove(results[num])


def pass_mode():
    """Функция выбора действий в меню."""
    print("Список действий")
    print("-" * 14)
    print("1. Изменить пароль")
    print("2. Удалить пароль")
    print("3. Выйти из поиска")
    print("-" * 14)
    user_intake = input("Выберите номер действия: ")
    return user_intake


def check(db):
    """
    Функция проверки пароля на дубликат.
    :param db: Данные файла.
    """
    count = {}  # Счетчик
    for info in db:
        if info["password"] in count:  # Если пароль совпадает, то увеличиваем счетчик.
            count[info["password"]] += 1
        else:
            count[info["password"]] = 1

    for password, num in count.items():  # Если таких паролей
        if num > 1:  # больше одного, то:
            print(f"Пароль ({password}) не безопасен! Он используется на сайтах:")
            for info in db:  # Выводим сайты на которых уже задействован это пароль.
                if info["password"] == password:
                    print(f"| Сайт: {info['site']:15} | Логин: {info['login']:15} | Пароль: {info['password']:15} |")


def mode():
    """
    Функция выбора режимов в меню.
    """
    print("Список режимов")
    print("-" * 14)
    print("1. Добавить пароль")
    print("2. Сгенерировать пароль")
    print("3. Найти пароль")
    print("4. Найти уязвимости")
    print("5. Выход")
    print("-" * 14)
    user_intake = input("Выберите номер режима: ")
    return user_intake


def loop(filename):
    """Функция по запуску программного цикла."""
    db = load_db(filename)  # Загрузка данных из файла.
    while True:  # Запускаем вечный цикл.
        user_intake = mode()
        if user_intake == "1":
            add_pass(db)
        elif user_intake == "2":
            add_and_gen(db)
        elif user_intake == "3":
            search(db)
        elif user_intake == "4":
            check(db)
        elif user_intake == "5":
            break
        else:
            print("Нет такого режима")

    save_db(filename, db)  # Сохраняем данные.


db = load_db("user.json")
loop("user.json")
