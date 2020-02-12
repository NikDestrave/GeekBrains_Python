'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''

from random import randint


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Автомобиль поехал')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, side):
        print(f'Автомобиль повернул {side}')

    def show_speed(self, speed):
        print(speed)


class TownCar(Car):
    def show_speed(self, speed):
        if int(self.speed) > 60:
            return 'Превышение скорости!'
        else:
            return ''


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        if int(self.speed) > 40:
            return 'Превышение скорости!'
        else:
            return ''


class PoliceCar(Car):
    pass


auto_1 = TownCar(randint(20, 80), 'Белая', 'Мазда')
auto_1.go()
print(f'{auto_1.color} {auto_1.name}, скорость: {auto_1.speed} км/ч {auto_1.show_speed({auto_1.speed})}')
auto_1.turn('налево')
auto_1.stop()

auto_2 = WorkCar(randint(20, 80), 'Серый', 'Мерседес')
auto_2.go()
print(f'{auto_2.color} {auto_2.name}, скорость: {auto_2.speed} км/ч {auto_2.show_speed({auto_2.speed})}')
auto_2.turn('направо')
auto_2.stop()
