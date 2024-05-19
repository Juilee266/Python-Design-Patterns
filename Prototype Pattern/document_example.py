from abc import ABC, abstractmethod
import copy

class DocumentPrototype(ABC):
    def __init__(self, doc_name):
        self.doc_name = doc_name

    @abstractmethod
    def clone(self):
        pass

class JSONDocument(DocumentPrototype):
    def __init__(self, doc_name, json_data):
        super(JSONDocument, self).__init__(doc_name)
        self.json_data = json_data

    def clone(self):
        return copy.deepcopy(self)

    def print(self):
        print(f"JSON: {self.doc_name} - {self.json_data} - {id(self)}")


class XMLDocument(DocumentPrototype):
    def __init__(self, doc_name, xml_data):
        super(XMLDocument, self).__init__(doc_name)
        self.xml_data = xml_data

    def clone(self):
        return copy.deepcopy(self)

    def print(self):
        print(f"XML: {self.doc_name} - {self.xml_data} - {id(self)}")


class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def add_prototype(self, name, prototype):
        self._prototypes[name] = prototype

    def get_prototype(self, name):
        return self._prototypes[name].clone() if name in self._prototypes else None

if __name__ == "__main__":
    json1 = JSONDocument("a1.json", "json_data_sample")
    xml1 = XMLDocument("a2.xml", "xml_data_sample")
    json1.print()
    xml1.print()

    registry = PrototypeRegistry()
    registry.add_prototype("JSONDocument", json1)
    registry.add_prototype("XMLDocument", xml1)

    json2 = registry.get_prototype("JSONDocument")
    xml2 = registry.get_prototype("XMLDocument")
    json2.print()
    xml2.print()