# Task:
# 2) Реализуйте функционал, который будет запрещать установку полей класса
# любыми значениями, кроме целых чисел. Т.е., если тому или иному полю
# попытаться присвоить, например, строку, то должно быть возбужденно
# исключение.

class Descriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise AttributeError('int only')
        self.value = value

    def __delete__(self, instance):
        raise AttributeError('cannot be deleted')


class Rectangle:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    area = Descriptor(10)

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'


x = Rectangle(2, 5)
print(x)
x.area = '2000'
print(x.area)
print()
