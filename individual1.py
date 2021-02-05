#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 18. Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

# Решить индивидуальное задание лабораторной работы 8, оформив каждую команду в виде
# отдельной функции.


import sys


def add(markets, shop, product, price):
    market = {
        'shop': shop,
        'product': product,
        'price': price
    }

    markets.append(market)
    if len(markets) > 1:
        markets.sort(key=lambda item: item.get('shop', ''))


def list(markets):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Магазин",
            "Товар",
            "Стоимость в руб."
        )
    )
    print(line)

    for idx, market in enumerate(markets, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                market.get('shop', ''),
                market.get('product', ''),
                market.get('price', 0)
            )
        )
        print(line)


def select(markets, period):
    result = []
    number = str(parts[1])
    count = 0
    for market in markets:
        if market.get('shop') == number:
            count += 1

    return result


if __name__ == '__main__':

    markets = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            shop = input("Название магазина? ")
            product = input("Название товара? ")
            price = int(input("Стоимость товара в руб.? "))

            add(markets, shop, product, price)

        elif command == 'list':
            print(list(markets))

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            selected = select(markets, str(parts[1]))

            if selected:
                for count, markets in enumerate(selected, 1):
                    print(
                        '{:>4}: {}'.format(count, markets.get('shop', ''))
                    )
            else:
                print("Товар не найден.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <товар> - информация о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
