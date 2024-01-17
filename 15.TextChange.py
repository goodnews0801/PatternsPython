class TextChangeListener:
    def on_text_change(self, old_text, new_text):
        pass

class IWillListen(TextChangeListener):
    def __init__(self):
        self.text = ""

    def on_text_change(self, old_text, new_text):
        self.text = f"Old: {old_text} -> New: {new_text}"
        print(self.text)

class SomeText:
    def __init__(self):
        self.listeners = []
        self._text = ""

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        for listener in self.listeners:
            listener.on_text_change(self._text, value)
        self._text = value

def main():
    some_text = SomeText()
    listener = IWillListen()
    some_text.listeners.append(listener)

    print(some_text.text)
    some_text.text = "Это новое значение"
    print(some_text.text)
    some_text.text = "тест значение"
    print(some_text.text)

if __name__ == "__main__":
    main()
