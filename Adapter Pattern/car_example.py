
class Car:
    def __init__(self, name, driver=None):
        self.name = name
        self.driver = driver

    def accelerate(self):
        print(f"Car {self.name} is being accelerated")

    def apply_brakes(self):
        print(f"Applying brakes to the car {self.name}")

    def assign_driver(self, driver):
        self.driver = driver
        print(f"Assigned driver {self.driver} to car {self.name}")


class Bike:
    def __init__(self, name, rider=None):
        self.name = name
        self.rider = rider

    def rev_throttle(self):
        print(f"Bike {self.name} is being reverse throttled")

    def pull_brake_lever(self):
        print(f"Pulling brake lever of the bike {self.name}")

    def assign_rider(self, rider):
        self.rider = rider
        print(f"Assigned rider {self.rider} to bike {self.name}")

class BikeAdapter(Bike):
    def accelerate(self):
        self.rev_throttle()

    def apply_brakes(self):
        self.pull_brake_lever()

    def assign_driver(self, driver):
        self.assign_rider(driver)

if __name__ == "__main__":
    car1 = Car("Indica")
    bike1 = Bike("Yamaha")

    print("Car class methods called by Car object")
    car1.accelerate()
    car1.apply_brakes()
    car1.assign_driver("Indu")

    print("\nBike class methods called by Bike object")
    bike1.rev_throttle()
    bike1.pull_brake_lever()
    bike1.assign_rider("Yadu")

    print("\nCar class methods called by Bike object")
    bike_adapter = BikeAdapter("Hero")
    bike_adapter.accelerate()
    bike_adapter.apply_brakes()
    bike_adapter.assign_driver("Himesh")