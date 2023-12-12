from abc import ABC, abstractmethod
import math

# Абстрактный класс для точек
class Point(ABC):
    @abstractmethod
    def get_coordinates(self):
        pass

# класс точки в декартовой системе координат
class CartesianPoint(Point):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return f"Декартовы координаты: ({self.x}, {self.y})"

# класс точки в полярной системе координат
class PolarPoint(Point):
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def get_coordinates(self):
        x = self.radius * math.cos(math.radians(self.angle))
        y = self.radius * math.sin(math.radians(self.angle))
        return f"Полярные координаты: (Ro={self.radius}, theta={self.angle}) конвертированы в декартовы координаты: ({x}, {y})"

# Фабрика точек
class PointFactory(ABC):
    @abstractmethod
    def create_point(self):
        pass

# Конкретные фабрики для создания точек в различных системах координат
class CartesianPointFactory(PointFactory):
    def create_point(self, x, y):
        return CartesianPoint(x, y)

class PolarPointFactory(PointFactory):
    def create_point(self, radius, angle):
        return PolarPoint(radius, angle)

# Пример использования фабричного метода
def use_point_factory(factory):
    point = factory.create_point(3, 4)  # Создание точки с координатами
    print(point.get_coordinates())  # Получение координат точки

# Создание фабрик и создание точек в различных системах координат
cartesian_factory = CartesianPointFactory()
polar_factory = PolarPointFactory()

use_point_factory(cartesian_factory)  # Использование фабрики для декартовых координат
use_point_factory(polar_factory)  # Использование фабрики для полярных координат