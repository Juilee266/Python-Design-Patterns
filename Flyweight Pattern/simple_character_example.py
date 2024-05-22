
class CharFlyweight:
    def __init__(self, char):
        self.char = char

class CharFlyweightFactory:
    char_flyweights = {}

    @staticmethod
    def get_char(char):
        if char not in CharFlyweightFactory.char_flyweights:
            CharFlyweightFactory.char_flyweights[char] = CharFlyweight(char)
        return CharFlyweightFactory.char_flyweights[char]

class Character:
    def __init__(self, char, font_size):
        self.char_flyweight = CharFlyweightFactory.get_char(char)
        self.font_size = font_size

    def render(self):
        print(f"Character: {self.char_flyweight.char}, Font Size: {self.font_size}")

if __name__ == "__main__":
    characters = [Character('A', 12), Character("B", 13), Character("A", 12)]

    for ch in characters:
        ch.render()
        print(id(ch.char_flyweight))