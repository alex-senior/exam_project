from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, coordinates, cost, speed, year):
        self.coordinates = coordinates
        self.cost = cost
        self.speed = speed
        self.year = year

    @abstractmethod
    def dynamic_characteristics(self):
        pass

class Airplane(Transport):
    def __init__(self, coordinates, cost, speed, year, height, passengers):
        super().__init__(coordinates, cost, speed, year)
        self.height = height
        self.passengers = passengers

    def dynamic_characteristics(self):
        return f"Літак летить на висоті {self.height} метрів зі швидкістю {self.speed} км/год."

class Car(Transport):
    def __init__(self, coordinates, cost, speed, year):
        super().__init__(coordinates, cost, speed, year)

    def dynamic_characteristics(self):
        return f"Автомобіль рухається зі швидкістю {self.speed} км/год."

class Ship(Transport):
    def __init__(self, coordinates, cost, speed, year, passengers, port):
        super().__init__(coordinates, cost, speed, year)
        self.passengers = passengers
        self.port = port

    def dynamic_characteristics(self):
        return f"Корабель пливе зі швидкістю {self.speed} км/год і має порт приписки {self.port}."

# Приклад використання
airplane = Airplane((50.4501, 30.5234), 1000000, 900, 2020, 10000, 180)
car = Car((50.4501, 30.5234), 20000, 150, 2018)
ship = Ship((50.4501, 30.5234), 500000, 40, 2015, 300, "Одеса")

print(airplane.dynamic_characteristics())
print(car.dynamic_characteristics())
print(ship.dynamic_characteristics())
