# Using inheritance

class BaseSingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class SubSingleton1(BaseSingleton):
    def __init__(self):
        pass

class SubSingleton2(BaseSingleton):
    def __init__(self):
        pass

if __name__ == "__main__":
    instance1 = SubSingleton1()
    instance2 = SubSingleton1()
    instance3 = SubSingleton2()

    print("Implementation using a base class : instance1 is instance2 ->", instance1 is instance2)
    print("Two different child classes have different instances: instance3 is instance2 ->", instance3 is instance2)