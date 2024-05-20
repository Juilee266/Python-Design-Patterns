from abc import ABC, abstractmethod

class JSONComponent(ABC):
    @abstractmethod
    def parse(self):
        pass

class JSONLeaf(JSONComponent):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def parse(self):
        return f"{'{'} {self.key} : {self.value} {'}'}"

class JSONObject(JSONComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def parse(self):
        res = ["{"]
        for child in self.children:
            res.append(child.parse())
        res.append("}")
        return '\n'.join(res)

def parse_json(data_from_json_file):
    root = JSONObject()
    for k, v in data_from_json_file.items():
        if isinstance(v, list):
            for x in v:
                obj = parse_json(x)
                root.add(obj)
        elif isinstance(v, dict):
            obj = parse_json(v)
            root.add(obj)
        else:
            leaf = JSONLeaf(k, v)
            root.add(leaf)
    return root

if __name__ == "__main__":
    data = {
        "name": "Juilee",
        "age": 25,
        "assistants": [
            {"name": "XXX", "age": 20},
            {"name": "YYY", "age": 18}
        ],
        "address": {
            "city": "Pune",
            "pincode": "412307"
        }
    }
    root = parse_json(data)
    print(root.parse())