import math

# Функции для создания точек в различных системах координат

def create_point_factory(coord_system):
    def create_point(*args):
        if coord_system == 'cartesian':
            return create_cartesian_point(*args)
        elif coord_system == 'polar':
            return create_polar_point(*args)
        else:
            raise ValueError("Неизвестная система координат")
    
    return create_point

def create_cartesian_point(x, y):
    def get_coordinates():
        return f"Декартовы координаты: ({x}, {y})"
    return get_coordinates

def create_polar_point(radius, angle):
    def get_coordinates():
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        return f"Полярные координаты: (r={radius}, θ={angle}) конвертированы в декартовы координаты: ({x}, {y})"
    return get_coordinates

# Пример использования функционального подхода с callable фабричным методом

# Создание фабрики точек для различных систем координат
point_factory = create_point_factory('cartesian')

# Создание точек с помощью фабричного метода
cartesian_point = point_factory(3, 4)

# Использование функции для получения координат точки
print(cartesian_point())  # Получение координат точки