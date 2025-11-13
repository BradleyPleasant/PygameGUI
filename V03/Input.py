from pygame.locals import *


class Input:
    def on_mouse_button_down(self, element, event):
        print(f"Event: {event}, Element: {element}")
    def on_mouse_button_up(self, element, event):
        print(f"Event: {event}, Element: {element}")
    def on_mouse_motion(self, element, event):
        print(f"Event: {event}, Element: {element}")
    def on_key_down(self, element, event):
        print(f"Event: {event}, Element: {element}")
    def on_key_up(self, element, event):
        print(f"Event: {event}, Element: {element}")
    def on_text_input(self, element, event):
        print(f"Event: {event}, Element: {element}")
