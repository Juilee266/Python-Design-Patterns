from abc import ABC, abstractmethod

class EnemyFlyweight(ABC):
    @abstractmethod
    def render(self, position):
        pass

class EnemyTypeA(EnemyFlyweight):
    def __init__(self, texture):
        self.texture = texture

    def render(self, position):
        print(f"Rendering EnemyTypeA at {position} with {self.texture} {id(self)}")

class EnemyTypeB(EnemyFlyweight):
    def __init__(self, texture):
        self.texture = texture

    def render(self, position):
        print(f"Rendering EnemyTypeB at {position} with {self.texture} {id(self)}")

class EnemyFlyweightFactory:
    _flyweights = {}

    @staticmethod
    def get_flyweight(texture, fw_type):
        if texture not in EnemyFlyweightFactory._flyweights:
            EnemyFlyweightFactory._flyweights[texture] = EnemyTypeA(texture) if fw_type == "A" else EnemyTypeB(texture)
        return EnemyFlyweightFactory._flyweights[texture]

class GameArena:
    def __init__(self):
        self.enemies= []

    def add_enemy(self, position, texture, fw_type):
        flyweight = EnemyFlyweightFactory.get_flyweight(texture, fw_type)
        self.enemies.append((flyweight, position))

    def render_enemies(self):
        for flyweight, pos in self.enemies:
            flyweight.render(pos)

if __name__ == "__main__":
    ga = GameArena()
    ga.add_enemy((10, 20), "t1", "A")
    ga.add_enemy((20, 20), "t2", "B")
    ga.add_enemy((15, 20), "t1", "A")
    ga.add_enemy((15, 40), "t2", "B")

    ga.render_enemies()

