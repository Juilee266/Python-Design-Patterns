from abc import ABC, abstractmethod
from enum import Enum

class Language(Enum):
    ENGLISH = 1
    FRENCH = 2
    GERMAN = 3

# Defining the product
class Translator(ABC):
    @abstractmethod
    def translate(self, text):
        pass

# Creating concrete products
class FrenchTranslator(Translator):
    def __init__(self):
        self.translations = {
            'yes': 'oui',
            'no': 'non'
        }
    def translate(self, text):
        if text in self.translations:
            return self.translations[text]
        return None

class GermanTranslator(Translator):
    def __init__(self):
        self.translations = {
            'yes': 'ja',
            'no': 'nein'
        }
    def translate(self, text):
        if text in self.translations:
            return self.translations[text]
        return None

class EnglishTranslator(Translator):
    def translate(self, text):
        return text

def create_translator(lang): # Factory method
    if lang == Language.ENGLISH:
        return EnglishTranslator()
    if lang == Language.GERMAN:
        return GermanTranslator()
    if lang == Language.FRENCH:
        return FrenchTranslator()
    raise ValueError("Translator not available for ", lang)

if __name__ == "__main__":
    eng_translator = create_translator(Language.ENGLISH)
    french_translator = create_translator(Language.FRENCH)
    german_translator = create_translator(Language.GERMAN)

    print(eng_translator.translate("yes"))
    print(german_translator.translate("yes"))
    print(french_translator.translate("yes"))