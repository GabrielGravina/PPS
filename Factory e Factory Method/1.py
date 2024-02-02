from abc import ABC

class Vehicle(ABC):
    def manufacture(self):
        pass

class VehicleFactory(ABC):
    def produce_car(self):
        pass

    def produce_motorcycle(self):
        pass

    def produce_truck(self):
        pass

class Car(Vehicle):
    def manufacture(self):
        print("Produzindo um carro.")

class Motorcycle(Vehicle):
    def manufacture(self):
        print("Produzindo uma motocicleta.")

class Truck(Vehicle):
    def manufacture(self):
        print("Produzindo um caminhão.")

class ElectricVehicleFactory(VehicleFactory):
    def produce_car(self):
        return Car()

    def produce_motorcycle(self):
        return Motorcycle()

    def produce_truck(self):
        return Truck()

class FuelVehicleFactory(VehicleFactory):
    def produce_car(self):
        return Car()

    def produce_motorcycle(self):
        return Motorcycle()

    def produce_truck(self):
        return Truck()

def main():
    electric_factory = ElectricVehicleFactory()
    fuel_factory = FuelVehicleFactory()

    car1 = electric_factory.produce_car()
    motorcycle1 = electric_factory.produce_motorcycle()
    truck1 = electric_factory.produce_truck()

    car2 = fuel_factory.produce_car()
    motorcycle2 = fuel_factory.produce_motorcycle()
    truck2 = fuel_factory.produce_truck()

    car1.manufacture()
    motorcycle1.manufacture()
    truck1.manufacture()

    car2.manufacture()
    motorcycle2.manufacture()
    truck2.manufacture()

if __name__ == "__main__":
    main()
