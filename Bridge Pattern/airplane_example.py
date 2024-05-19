from abc import ABC, abstractmethod

class Plane(ABC):
    def __init__(self, carrier):
        self.carrier = carrier

    @abstractmethod
    def carry(self):
        pass

class MilitaryPlane(Plane):
    def __init__(self, carrier, items):
        super(MilitaryPlane, self).__init__(carrier)
        self.items = items

    def carry(self):
        self.carrier.carry_military(self.items)

class CommercialPlane(Plane):
    def __init__(self, carrier, items):
        super(CommercialPlane, self).__init__(carrier)
        self.items = items

    def carry(self):
        self.carrier.carry_commercial(self.items)

class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass

class Passenger(Carrier):
    def carry_military(self, items):
        print(f"Military - Passenger - {items}")

    def carry_commercial(self, items):
        print(f"Commercial - Passenger - {items}")


class Cargo(Carrier):
    def carry_military(self, items):
        print(f"Military - Cargo - {items}")

    def carry_commercial(self, items):
        print(f"Commercial - Cargo - {items}")

if __name__ == "__main__":
    # Military - Passenger
    passenger1 = Passenger()
    military1 = MilitaryPlane(passenger1, 10)
    military1.carry()

    # Military - Cargo
    cargo2 = Cargo()
    military2 = MilitaryPlane(cargo2, 10)
    military2.carry()

    # Commercial - Passenger
    passenger3 = Passenger()
    commercial3 = CommercialPlane(passenger3, 200)
    commercial3.carry()

    # Commercial - Cargo
    cargo4 = Cargo()
    commercial4 = CommercialPlane(cargo4, 500)
    commercial4.carry()