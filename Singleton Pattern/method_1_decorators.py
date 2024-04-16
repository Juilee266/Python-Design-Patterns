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
class SingletonClassA:
    pass

@singleton
class SingletonClassB:
    pass

if __name__ == "__main__":
    a1 = SingletonClassA()
    a2 = SingletonClassA()

    print("a1 is a2 -> ", a1 is a2)

    b1 = SingletonClassB()
    b2 = SingletonClassB()

    print("b1 is b2 -> ", b1 is b2)

    print("a1 is b2 -> ", a1 is b2)