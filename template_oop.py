"""
Шаблонный метод (Template Method) - это шаблон проектирования, который определяет структуру алгоритма, 
оставляя определение реализации некоторых шагов этого алгоритма на усмотрение подклассов.
"""
from abc import ABC, abstractmethod

# Абстрактный класс для напитков
class Beverage(ABC):
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print("Кипятим воду")

    def pour_in_cup(self):
        print("Переливаем напиток в чашку")

    # Хук, который подклассы могут переопределить
    def customer_wants_condiments(self):
        return True

# Конкретные классы для чая и кофе
class Tea(Beverage):
    def brew(self):
        print("Завариваем чай")

    def add_condiments(self):
        print("Добавляем лимон")

    def customer_wants_condiments(self):
        answer = input("Хотите добавить лимон? (да/нет): ")
        return True if answer.lower() == 'да' else False

class Coffee(Beverage):
    def brew(self):
        print("Варим кофе")

    def add_condiments(self):
        print("Добавляем молоко и сахар")

def make_beverage(beverage):
    beverage.prepare_beverage()

# Приготовление чая
print("Приготовление чая:")
tea = Tea()
make_beverage(tea)

print("\n")

# Приготовление кофе
print("Приготовление кофе:")
coffee = Coffee()
make_beverage(coffee)