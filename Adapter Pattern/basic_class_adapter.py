
class OldSystem:
    def legacy_operation(self):
        print("Legacy Operation")

class Adapter(OldSystem):
    def new_operation(self):
        print("some adapter code")
        self.legacy_operation()

def client_code(adapter: Adapter):
    adapter.new_operation()

if __name__ == "__main__":
    adapter = Adapter()
    client_code(adapter)