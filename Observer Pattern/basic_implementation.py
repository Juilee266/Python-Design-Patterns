
class Observer:
    def __init__(self, observable, name):
        self.name = name
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print(f"{self.name} received {args} {kwargs} from {observable}")

class Observable:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)



if __name__ == "__main__":
    subject = Observable()
    for i in range(10):
        obs = Observer(subject, f"observer {i}")

    subject.notify_all("Message 1", msg="From the broadcaster")
    subject.notify_all("Message 2", msg="From the subject")
