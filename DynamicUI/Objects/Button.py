from .. import Element, Renderer, InputHandler
from pygame import Font, Event, Surface, SRCALPHA, MOUSEBUTTONUP, MOUSEBUTTONDOWN


class ButtonInputHandler(InputHandler):
    def handle_event(self, event: Event, element: Element) -> None:
        if event.type == MOUSEBUTTONDOWN:
            print("Button pressed!")
        elif event.type == MOUSEBUTTONUP:
            print("Button released!")
