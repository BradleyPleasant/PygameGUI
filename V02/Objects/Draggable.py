from .. import Element, Renderer, InputHandler
from pygame import Font, Event, Surface, SRCALPHA, MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION


class DraggableInputHandler(InputHandler):
    def handle_event(self, event: Event, element: Element) -> None:
        if event.type == MOUSEBUTTONDOWN:
            element.app.dragging = element
        elif event.type == MOUSEBUTTONUP:
            element.app.dragging = None
        elif event.type == MOUSEMOTION:
            if element.app.dragging is element:
                element.rect.x += event.rel[0]
                element.rect.y += event.rel[1]
