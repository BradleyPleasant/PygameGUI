import pygame
from .Element import Element


class InputHandler:
    def handle_event(self, event: pygame.event.Event, element: Element) -> None:
        print(event, event.dict)