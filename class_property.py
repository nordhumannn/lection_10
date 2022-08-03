# Task:
# Реализуйте свойство класса, которое обладает следующим
# функционалом: при установки значения этого свойства в файл с заранее
# определенным названием должно сохранятся время (когда устанавливали
# значение свойства) и установленное значение.

import datetime


class Student:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        with open('name_log.txt', 'a') as f:
            f.write(f'{datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} -- {value}\n')
        self.__name = value

    def __str__(self):
        return f'{self.name} {self.surname}, {self.age}'


x = Student('John', 'Doe', 21)

print(x)
