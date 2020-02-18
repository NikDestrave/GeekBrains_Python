'''Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

class Warehouse:
    def __init__(self, row, place):
        self.row = row
        self.place = place

class Equipment(Warehouse):
    def equi(self, manufacturer, id, row, place):
        super().__init__(self, row, place)
        self.manufacturer = manufacturer
        self.id = id


class Printer(Equipment):
    def speed(self, speed):
        self.speed = speed

class Scanner(Equipment):
    def speed(self, quality):
        self.quality = quality

class Xerox(Equipment):
    def speed(self, volume):
        self.volume = volume

technic = Equipment('Samsung', 123451)