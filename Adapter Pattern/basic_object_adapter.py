class OldSystem:
    def legacy_operation(self):
        print("Legacy Operation")

class Adapter:
    def __init__(self, old_system:OldSystem):
        self.old_system = old_system

    def new_operation(self):
        print("some adapter code")
        self.old_system.legacy_operation()

def client_code(adapter: Adapter):
    adapter.new_operation()

if __name__ == "__main__":
    old_sys = OldSystem()
    adapter = Adapter(old_sys)
    client_code(adapter)
