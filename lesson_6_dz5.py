'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки...')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой...')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом...')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером...')


result_stationery = Stationery('Отрисовка')
result_stationery.draw()

result_pen = Pen('Ручка')
result_pen.draw()

result_pencil = Pencil('Карандаш')
result_pencil.draw()

result_handle = Handle('Маркер')
result_handle.draw()
