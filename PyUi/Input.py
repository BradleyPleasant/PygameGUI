from pygame.locals import *


class Input:
    def __init__(self, selectable: bool = True):
        self.selectable = selectable
    def on_mouse_button_down(self, element, event):
        pass
    def on_mouse_button_up(self, element, event):
        pass
    def on_mouse_motion(self, element, event):
        pass
    def on_key_down(self, element, event):
        pass
    def on_key_up(self, element, event):
        pass
    def on_text_input(self, element, event):
        pass
    def on_mouse_enter(self, element):
        pass
    def on_mouse_leave(self, element):
        pass
