class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Пример использования Singleton
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()

print(singleton_instance1 is singleton_instance2)  # Результат - True, это один и тот же объект