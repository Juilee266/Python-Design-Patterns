# Using __new__

class SingletonClass:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance

if __name__ == "__main__":
   instance1 = SingletonClass()
   instance2 = SingletonClass()

   print("instance1 is instance2 -> ", instance1 is instance2)
