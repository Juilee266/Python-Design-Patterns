
class Customer:
    def __init__(self, store, name):
        self.name = name
        store.subscribe(self)

    def notify(self, *args, **kwargs):
        print(f"Customer: {self.name}, {args}, {kwargs}")

class Store:
    def __init__(self):
        self.item_count = 0
        self._customers = []

    def subscribe(self, customer):
        self._customers.append(customer)

    def unsubscribe(self, customer):
        self._customers.remove(customer)

    def add_items(self, count):
        self.item_count += count
        if self.item_count >= len(self._customers):
            for c in self._customers:
                c.notify("Product available!", f"Current count {self.item_count}")

if __name__ == "__main__":
    store = Store()

    c1 = Customer(store, "customer1")
    c2 = Customer(store, "customer2")
    c3 = Customer(store, "customer3")

    store.add_items(2)
    store.add_items(2)

    store.unsubscribe(c2)

    store.add_items(5)