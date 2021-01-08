#!/usr/bin/env python3
# -*- config: utf-8 -*-

import math

#   Решите следующую задачу: в основной ветке программы вызывается функция cylinder(),
#   которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
#   вычисляющая площадь круга по формуле . В теле cylinder() у пользователя
#   спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
#   которая вычисляется по формуле , или полную площадь цилиндра. В последнем
#   случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
#   вычислений функции circle().

def cylinder(r, h, full=True):
    def circle(r):
        return math.pi * (r ** 2)

    s_cylinder = 2 * math.pi * r * h

    if full:
        return s_cylinder + 2 * circle(r)
    else:
        print(s_cylinder)

if __name__ == '__main__':
    s_circle = 0
    a = float(input("Введите радиус: "))
    b = float(input("Введите высоту: "))

    c = input("side or full? ")
    s = cylinder(a, b, full=(c == 'full'))
    print(s)
    