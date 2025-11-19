from ..Element import Element
from ..Input import Input
import pygame


class Draggable(Input):
    def __init__(self):
        super().__init__(selectable=True)

    def on_mouse_button_down(self, element: Element, event):
        if event.button == 1:  # Left mouse button
            element.app.cursor_capture = element

    def on_mouse_button_up(self, element: Element, event):
        if event.button == 1:  # Left mouse button
            element.app.cursor_capture = None

    def on_mouse_motion(self, element: Element, event):
        # set the mouse to the drag cursor
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)

        if element.app.cursor_capture is not element:
            return
        # Update element position based on mouse movement
        element.root.x += event.rel[0]
        element.root.y += event.rel[1]
