"""Пример анализа валютного портфеля"""
import json
from copy import deepcopy


def save_data(data):  # Сохранение данных.
    with open("data.json", "w") as f:  # Открытие файла.
        json.dump(data, f, indent=2)  # Сохранение в файл.


def load_data():  # Загрузка данных.
    with open("data.json") as f:  # Открытие файла.
        data = json.load(f)  # Считывание данных из файла

    return data


def show_percent(name, percent, width=50):
    fill = "▊"
    empty = "-"
    bars = round(percent * width)
    progress = fill * bars + empty * (width - bars)
    print(f"{name:7} - {round(percent * 100)}% |{progress}|")


def plot_stat(data, signs, height=12):
    for i in range(height):
        if i % 3 == 0:
            current = max(data) - (max(data) - min(data)) / height * i
            line = f"{str(round(current, 2)):10}"
        else:
            line = " " * 10
        for num in data:
            if max(data) - (max(data) - min(data)) / height * (i + 1) < num:
                line += "▊   "
            else:
                line += "    "
        print(line)

    print(f"{str(round(min(data), 2)):10}" + "▊   " * len(data))
    print(" " * 10 + "▊   " * len(data))
    line = " " * 10
    for sign in signs:
        line += f"{sign:4}"

    print(line)


def show_convert(data):
    weeks = list(sorted(data.keys()))
    converted = []

    for week in weeks:
        currencies = data[week]
        total = 0
        for curr in currencies:
            total += curr["cost"] * curr["amount"]

        converted.append(round(total, 2))

    plot_stat(converted, weeks)


def show_stat(data, weeknum):
    total = 0
    for curr in data[weeknum]:
        total += curr["cost"] * curr["amount"]

    stats = []
    for curr in data[weeknum]:
        stats.append((curr["cost"] * curr["amount"] / total, curr["name"]))

    stats = reversed(sorted(stats))
    for s, name in stats:
        show_percent(name, s)


def select_mode():
    print()
    print("-" * 30)
    print("  Выберите режим работы:")
    print("  1. Добавить новую неделю")
    print("  2. Скопировать новую неделю")
    print("  3. Добавить информацию о валюте")
    print("  4. Изменить информацию о валюте")
    print("  5. Вывести статистику")
    print("  6. Вывести распределение валют")
    print("  7. Выйти из программы")
    print("-" * 30)
    print()
    return int(input("Ввод: "))


def loop():
    data = load_data()
    while True:
        mode = select_mode()

        if mode == 1:
            week = input("Введите номер новой недели: ")
            data[week] = []
        elif mode == 2:
            week = input("Введите номер новой недели: ")
            from_week = input("Введите номер недели, откуда будем копировать: ")
            data[week] = deepcopy(data[from_week])
        elif mode == 3:
            week = input("Введите номер недели: ")
            name = input("Введите название валюты: ")
            cost = float(input("Введите стоимость валюты: "))
            amount = float(input("Введите количество валюты: "))
            data[week].append({
                "name": name,
                "cost": cost,
                "amount": amount
            })
        elif mode == 4:
            week = input("Введите номер недели: ")
            name = input("Введите название валюты: ")

            num = None
            for i, curr in enumerate(data[week]):
                if curr["name"] == name:
                    num = i

            if num == None:
                print("Нет такой валюты!")
            else:
                curr_cost = data[week][num]["cost"]
                cost = input(f"Введите стоимость валюты ({curr_cost}): ")
                if cost:
                    data[week][num]["cost"] = float(cost)

                curr_amount = data[week][num]["amount"]
                amount = input(f"Введите стоимость валюты ({curr_amount}): ")
                if amount:
                    data[week][num]["amount"] = float(amount)
        elif mode == 5:
            show_convert(data)
        elif mode == 6:
            week = input("Введите номер недели: ")
            show_stat(data, week)
        elif mode == 7:
            print("Выход")
            break
        else:
            print("Некорректный режим!")

    save_data(data)


loop()
