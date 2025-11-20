from ..Input import Input
import pygame


class ReSizable(Input):
    RESIZE_ZONE = 10

    def on_mouse_button_down(self, element, event):
        if event.button != 1:
            return

        rect = element.global_rect()
        if rect.right - self.RESIZE_ZONE <= event.pos[0] <= rect.right and \
           rect.bottom - self.RESIZE_ZONE <= event.pos[1] <= rect.bottom:
            element.app.cursor_capture = element

    def on_mouse_button_up(self, element, event):
        if event.button == 1:
            element.app.cursor_capture = None

    def on_mouse_motion(self, element, event):
        rect = element.global_rect()

        # cursor
        if rect.right - self.RESIZE_ZONE <= event.pos[0] <= rect.right and \
           rect.bottom - self.RESIZE_ZONE <= event.pos[1] <= rect.bottom:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if element.app.cursor_capture is not element:
            return

        # Resize element based on mouse movement
        element.width += event.rel[0]
        element.height += event.rel[1]

        # if resizing makes the element or it's siblings stretch beyond parent's bounds, adjust parent size too
        parent = element.parent
        if parent:
            total_width = max(sibling.width for sibling in parent.children)
            total_height = (sum(sibling.height for sibling in parent.children)
                            + (parent.child_padding() * (len(parent.children) - 1))
                            + (parent.element_padding() * 2))
            if parent.width < total_width:
                parent.width = total_width
            if parent.height < total_height:
                parent.height = total_height
