from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def display(self):
        pass

class AsusLaptop(Laptop):
    def display(self):
        print("This is an Asus Laptop.")

class SamsungLaptop(Laptop):
    def display(self):
        print("This is a Samsung Laptop.")

class SmartPhone(ABC):
    @abstractmethod
    def display(self):
        pass


class AsusSmartPhone(SmartPhone):
    def display(self):
        print("This is an Asus SmartPhone.")


class SamsungSmartPhone(SmartPhone):
    def display(self):
        print("This is a Samsung SmartPhone.")

class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self):
        pass

    @abstractmethod
    def create_smartphone(self):
        pass

class AsusFactory(DeviceFactory):

    def create_laptop(self):
        return AsusLaptop()

    def create_smartphone(self):
        return AsusSmartPhone()


class SamsungFactory(DeviceFactory):

    def create_laptop(self):
        return SamsungLaptop()

    def create_smartphone(self):
        return SamsungSmartPhone()

def get_factory(company: str) -> DeviceFactory:
    if company == "asus":
        return AsusFactory()
    elif company == "samsung":
        return SamsungFactory()

if __name__ == "__main__":
    factory1 = get_factory("asus")
    factory2 = get_factory("samsung")

    asus_laptop = factory1.create_laptop()
    asus_phone = factory1.create_smartphone()
    asus_laptop.display()
    asus_phone.display()

    samsung_laptop = factory2.create_laptop()
    samsung_phone = factory2.create_smartphone()
    samsung_laptop.display()
    samsung_phone.display()