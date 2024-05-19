
class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Current station is {self.stations[self.pos]}, {self.name}")

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1.0", "2.0", "3.0"]
        self.name = "AM"
        self.pos = 0

    def toggle(self):
        print("\nSwitching to FM")
        self.radio.state = self.radio.fmstate


class FMState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["11.0", "12.0", "13.0"]
        self.name = "FM"
        self.pos = 0

    def toggle(self):
        print("\nSwitching to AM")
        self.radio.state = self.radio.amstate


class Radio:
    def __init__(self):
        self.fmstate = FMState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_state(self):
        self.state.toggle()

    def scan_stations(self):
        self.state.scan()

if __name__ == "__main__":
    radio1 = Radio()
    radio1.scan_stations()
    radio1.scan_stations()
    radio1.toggle_state()
    radio1.scan_stations()
    radio1.scan_stations()
    radio1.scan_stations()
    radio1.toggle_state()
    radio1.scan_stations()

