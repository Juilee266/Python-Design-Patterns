from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_desc(self):
        pass

    @abstractmethod
    def get_score(self):
        pass

class BasicCharacter(Character):
    def get_desc(self):
        return "Basic character"

    def get_score(self):
        return 10

class CharacterDecorator(Character, ABC):
    def __init__(self, character):
        self._character = character

    @abstractmethod
    def get_desc(self):
        pass

    @abstractmethod
    def get_score(self):
        pass


class FireBallDecorator(CharacterDecorator):
    def get_desc(self):
        return self._character.get_desc() + " with fireball!"

    def get_score(self):
        return self._character.get_score() * 10


class InvisibilityDecorator(CharacterDecorator):
    def get_desc(self):
        return self._character.get_desc() + " with invisibility!"

    def get_score(self):
        return self._character.get_score() + 20


class FlightDecorator(CharacterDecorator):
    def get_desc(self):
        return self._character.get_desc() + " with flight!"

    def get_score(self):
        return self._character.get_score() * 2

if __name__ == "__main__":
    tron = BasicCharacter()

    tron_with_fireball = FireBallDecorator(tron)
    print(tron_with_fireball.get_desc(), tron_with_fireball.get_score())

    tron_with_inv = InvisibilityDecorator(tron)
    print(tron_with_inv.get_desc(), tron_with_inv.get_score())

    tron_with_inv_and_flight = InvisibilityDecorator(FlightDecorator(tron))
    print(tron_with_inv_and_flight.get_desc(), tron_with_inv_and_flight.get_score())
