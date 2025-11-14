from ..Input import Input
import pygame


class ReSizable(Input):
    def on_mouse_button_down(self, element, event):
        if event.button == 1:
            rect = element.global_rect()
            if rect.right - 10 <= event.pos[0] <= rect.right and \
                    rect.bottom - 10 <= event.pos[1] <= rect.bottom:
                element.app.cursor_capture = element

    def on_mouse_button_up(self, element, event):
        print("up")
        if event.button == 1:
            element.app.cursor_capture = None

    def on_mouse_motion(self, element, event):
        rect = element.global_rect()
        if rect.right - 10 <= event.pos[0] <= rect.right and \
                rect.bottom - 10 <= event.pos[1] <= rect.bottom:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if element.app.cursor_capture is element:
            w, h = element.size
            w += event.rel[0]
            h += event.rel[1]
            element.size = w, h
            if element.graphics:
                element.graphics.surface = None
            print(element.size)

