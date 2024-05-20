class WrittenText:
    def __init__(self, text):
        self._text = text

    def display(self):
        return self._text

class BoldWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def display(self):
        return "<b>{}</b>".format(self._wrapped.display())


class ItallicWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def display(self):
        return "<i>{}</i>".format(self._wrapped.display())


class UnderlineWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def display(self):
        return "<u>{}</u>".format(self._wrapped.display())

if __name__ == "__main__":
    text = WrittenText("Juilee")
    bold_text = BoldWrapper(text)
    print(bold_text.display())

    italic_text = ItallicWrapper(text)
    print(italic_text.display())

    bold_underlined_text = BoldWrapper(UnderlineWrapper(text))
    print(bold_underlined_text.display())