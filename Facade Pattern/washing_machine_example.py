
class Washing:
    def wash(self):
        print("Washing the clothes...")

class Rinsing:
    def rinse(self):
        print("Rinsing the clothes...")

class Spinning:
    def spin(self):
        print("Spinning the clothes...")

class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def start_washing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()

if __name__ == "__main__":
    washing_machine = WashingMachine()
    washing_machine.start_washing()