from ..Input import Input
import pygame


class Button(Input):
    def __init__(self, run_on_click=None):
        super().__init__(selectable=True)
        self.run_on_click = run_on_click
    def on_mouse_button_down(self, element, event):
        pass

    def on_mouse_button_up(self, element, event):
        element.app.selected = None
        # if the mouse is still over the button when released, consider it a click
        if element.global_rect().collidepoint(event.pos):
            if callable(self.run_on_click):
                self.run_on_click(element = element)

    def on_mouse_motion(self, element, event):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)