# Task:
# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.

class Descriptor:

    def __get__(self, instance, owner):
        return instance.x * instance.y

    def __set__(self, instance, value):
        raise AttributeError()


class Rectangle:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    area = Descriptor()

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'


x = Rectangle(2, 5)
print(x.area)

