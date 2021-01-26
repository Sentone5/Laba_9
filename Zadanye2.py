#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Pair (пара чисел); определить методы изменения полей и вычисления
# произведения чисел. Определить производный класс Rectangle (прямоугольник) с полямисторонами.
# Определить методы вычисления периметра и площади прямоугольника.


class Pair:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        for part in parts:
            if part == 0:
                raise ValueError()

        self.set_a(parts[0])
        self.set_b(parts[1])

    def pr(self):
        return self.__a * self.__b


class Rectangle(Pair):
    def __init__(self, a=0, b=0,):
        super(Rectangle, self).__init__(a, b)

    def per(self):
        return (self.get_a() + self.get_b())*2

    def pl(self):
        return self.pr()


if __name__ == '__main__':
    R1 = Rectangle()
    R1.read("Введите стороны прямоугольника через запятую ")
    print("Искомые величины "
          "Периметр P={} "
          "Площадь S={} ".format(R1.per(), R1.pl()))
