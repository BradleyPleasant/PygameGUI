from ..Input import Input
from ..Objects import Label
from ..Element import Element


class TextField(Input):
    def __init__(self):
        super().__init__(selectable=True)
        self.text = ""
        self.allowed_chars = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
                              ".,!?-_'\"@#$/\\()[]{}<>`~|+=*&^%§€£¥¢°")


    def on_text_input(self, element, event):
        for char in event.text:
            if char not in self.allowed_chars:
                return  # Ignore disallowed characters

        self.text += event.text
        if element.graphics:
            if hasattr(element.graphics, "text"):
                element.graphics.text = self.text
                element.graphics.invalidate(element)

    def on_key_down(self, element, event):
        if event.key == 8:  # Backspace
            self.text = self.text[:-1]
            if element.graphics:
                if hasattr(element.graphics, "text"):
                    element.graphics.text = self.text
                    element.graphics.invalidate(element)