'''Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).'''


class Worker:
    def __init__(self, name, surname, income, bonus):
        self.name = name
        self.surname = surname
        self._income = {"wage": income, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


worker = Position('Алексей', 'Алексеев', 32000.00, 5000.00)
print(worker.get_full_name(), worker.get_total_income())

worker = Position('Иван', 'Иванов', 15000.00, 8000.00)
print(worker.get_full_name(), worker.get_total_income())
