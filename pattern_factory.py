from abc import ABC, abstractmethod
import logging

# Налаштування логування для коректного виведення символів кирилиці
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

# Клас Car, який успадковує від Vehicle
class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Двигун запущено")

# Клас Motorcycle, який успадковує від Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Мотор заведено")

# Абстрактна фабрика VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

# Фабрика для створення транспортних засобів для США (US Spec)
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (US Spec)", model)

# Фабрика для створення транспортних засобів для ЄС (EU Spec)
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make, model):
        return Motorcycle(f"{make} (EU Spec)", model)

# Використання

# Створення фабрики для США
us_factory = USVehicleFactory()
us_car = us_factory.create_car("Ford", "Mustang")
us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

# Старт двигунів
us_car.start_engine()
us_motorcycle.start_engine()

# Створення фабрики для ЄС
eu_factory = EUVehicleFactory()
eu_car = eu_factory.create_car("Volkswagen", "Golf")
eu_motorcycle = eu_factory.create_motorcycle("BMW", "R1250")

# Старт двигунів
eu_car.start_engine()
eu_motorcycle.start_engine()
