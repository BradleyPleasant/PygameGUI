from .. import Element, Renderer, InputHandler
from pygame import Font, Event, Surface, SRCALPHA, MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION
import pygame


class ResizableInputHandler(InputHandler):
    def handle_event(self, event: Event, element: Element) -> None:
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                rect = element.global_rect()
                # if the mouse is near the bottom-right corner, start resizing
                if rect.right - 10 <= event.pos[0] <= rect.right and \
                   rect.bottom - 10 <= event.pos[1] <= rect.bottom:
                    element.app.resizing = element
                    element.app.selected = element

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                element.app.resizing = None

        elif event.type == MOUSEMOTION:
            rect = element.global_rect()
            # if the mouse is near the bottom-right corner, resize
            if rect.right - 10 <= event.pos[0] <= rect.right and \
                rect.bottom - 10 <= event.pos[1] <= rect.bottom:
                # set the cursor to a resize cursor
                print("mouse_changed")
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if element.app.resizing is element:
                element.rect.width += event.rel[0]
                element.rect.height += event.rel[1]
                element.renderer.invalidate(element)
