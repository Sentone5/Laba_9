#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
# структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
# включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
# (например, «2004.08.31») и датой. Обязательными операциями являются: вычисление даты
# через заданное количество дней, вычитание заданного количества дней из даты,
# определение високосности года, присвоение и получение отдельных частей (год, месяц,
# день), сравнение дат (равно, до, после), вычисление количества дней между датами.

import datetime as d


class Date:

    def __init__(self):

        self.__year = 0
        self.__month = 0
        self.__day = 0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split('.')))

        self.__day = int(parts[2])
        self.__month = int(parts[1])
        self.__year = int(parts[0])
        self.__date = d.date(self.__year, self.__month, self.__day)

    # Инициализация даты числами
    def get_date1(self):
        return d.datetime.toordinal(self.__date)

    # Инициализация даты строкой «год.месяц.день»
    def get_date2(self):
        year = str(self.__year)
        month = str(self.__month)
        day = str(self.__day)
        date = year + '.' + month + '.' + day
        return date

    # Инициализация даты датой
    def get_date3(self):
        return self.__date

    def set_day(self, day):
        self.__day = day

    def set_month(self, month):
        self.__month = month

    def set_year(self, year):
        self.__year = year

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def calc_date(self, day):
        day = int(day)
        return d.datetime.fromordinal(day)

    def calc_day(self, days):
        days = int(days)
        day = d.datetime.toordinal(self.__date)
        days_new = day - days
        return d.datetime.fromordinal(days_new)

    def type_of_year(self):
        if self.__year % 4 != 0 or (self.__year % 100 == 0 and self.__year % 400 != 0):
            return 'Обычный'
        else:
            return 'Високосный'

    def raz_of_date(self, a, b):
        a = a.split('.')
        b = b.split('.')
        a = d.date(int(a[0]), int(a[1]), int(a[2]))
        b = d.date(int(b[0]), int(b[1]), int(b[2]))
        return a - b

    def srav_date(self, b):
        b = b.split('.')
        a = self.__date
        b = d.date(int(b[0]), int(b[1]), int(b[2]))
        if a == b:
            return 'Они равны'
        if a > b:
            return 'Данная дата будет до'
        else:
            return 'Данная дата будет после'

    def dispaly(self, days, date, date_1, date_2, date_3):
        print("Введенная дата в разных видах: {} дней, {}, {} \n"
              "Вычисление даты через заданные дни = {} \n"
              "Вычитание количества дней из даты = {} \n"
              "Определение високосного года -  Этот год - {} \n"
              "Количество дней между датами = {} \n"
              "Сравнение дат - {}".format(self.get_date1(), self.get_date2(),
                                          self.get_date3(), self.calc_date(days),
                                          self.calc_day(date),
                                          self.type_of_year(),
                                          self.raz_of_date(date_1, date_2),
                                          self.srav_date(date_3)
                                          )
              )


if __name__ == '__main__':
    print(((4**2+4+3)%20)+1)
    Time = Date()
    Time.read()
    days = input("Введите дни из которых нужны посчитать дату ")
    date = input("Введите дни которе нужно вычесть из даты ")
    date_1 = input("Введите первую дату для вычитания ")
    date_2 = input("Введите вторую дату для вычитания ")
    date_3 = input("Введите дату для сравнения ")
    Time.dispaly(days, date, date_1, date_2, date_3)
