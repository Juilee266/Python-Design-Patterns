
# Metaclass created by inheriting the type metaclass
class SingletonMetaClass(type):
    _instances = {}

    # Each time an instance of this metaclass's classes is initialised,
    # this method gets called
    def __call__(cls, *args, **kwargs):
        print("\n__call__ for", cls.__name__)
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaClass, cls).__call__(*args, **kwargs)
        else:
            # if __allow_reinitialization = True in the class,
            # the instance is reinitialised with new value
            attribute_name = "_"+cls.__name__+"__allow_reinitialization"
            if hasattr(cls, attribute_name) and cls.__getattribute__(cls, attribute_name):
                cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

class BaseClass(metaclass= SingletonMetaClass):
    def __init__(self, value):
        self.value = value
        print("\n__init__ called for BaseClass.", value)

class SubClass(BaseClass):
    __allow_reinitialization = True

    def __init__(self, value):
        self.value = value
        print("\n__init__ called for SubClass.", value)

class SubSubClass(SubClass):
    def __init__(self, value):
        self.value = value
        print("\n__init__ called for SubSubClass.", value)

if __name__ == "__main__":
    base1 = BaseClass(100)
    base2 = BaseClass(101)
    print("base1 is base2 -> ", base1 is base2)
    print("base1.value, base2.value -> ", base1.value, base2.value)

    sub1 = SubClass(200)
    sub2 = SubClass(201) # Value is reinitialised
    print("sub1 is sub2 -> ", sub1 is sub2)
    print("sub1.value, sub2.value -> ", sub1.value, sub2.value)

    sub_sub1 = SubSubClass(300)
    sub_sub2 = SubSubClass(301) # Value not initialised even though the parent has allowed so.
    print("sub_sub1 is sub_sub2 -> ", sub_sub1 is sub_sub2)
    print("sub_sub1.value, sub_sub2.value -> ", sub_sub1.value, sub_sub2.value)