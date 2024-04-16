
# Using decorators

import functools

def singleton(class_):
    @functools.wraps(class_)
    def wrapper(*args, **kwargs):
        if wrapper.instance is None:
            wrapper.instance = class_(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper

@singleton
class ClassA:
    pass

@singleton
class ClassB:
    pass

if __name__ == "__main__":
    a1 = ClassA()
    a2 = ClassA()

    print("a1 is a2 -> ", a1 is a2)

    b1 = ClassB()
    b2 = ClassB()

    print("b1 is b2 -> ", b1 is b2)

    print("a1 is b2 -> ", a1 is b2)