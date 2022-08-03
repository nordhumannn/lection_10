# Task
# 1) Создайте дескриптор, который будет делать поля класса управляемые им
# доступными только для чтения.

class Descriptor:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError('Field is read-only')

    def __delete__(self, instance):
        raise AttributeError('Cannot be deleted')


class Student:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    country = Descriptor('Ukraine')

    def __str__(self):
        return f'{self.name} {self.surname}'


a = Student('John', 'Doe')
print(a)
print(a.country)
a.country = 'USA'
