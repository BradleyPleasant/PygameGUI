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


        # RESIZE
        w, h = element.size
        w += event.rel[0]
        h += event.rel[1]

        # MIN SIZE
        w = max(w, element.min_size[0])
        h = max(h, element.min_size[1])

        # MIN CONTENT SIZE
        content_min_w = 0
        content_min_h = 0

        if element.children:
            # compute child bounds relative to element
            for child in element.children:
                cx, cy = child.x, child.y
                cw, ch = child.min_size
                content_min_w = max(content_min_w, cx + cw)
                content_min_h = max(content_min_h, cy + ch)

        # padding from element layout
        pad = 0
        if element.layout:
            pad = element.layout.element_padding

        # enforce children bounds + padding
        w = max(w, content_min_w + pad)
        h = max(h, content_min_h + pad)

        # PARENT MAX AREA
        if element.parent:
            pw, ph = element.parent.size
            px, py = element.x, element.y

            parent_pad = 0
            if element.parent.layout:
                parent_pad = element.parent.layout.element_padding

            usable_w = pw - parent_pad
            usable_h = ph - parent_pad

            max_w = usable_w - px
            max_h = usable_h - py

            w = min(w, max_w)
            h = min(h, max_h)

        # apply
        element.size = (w, h)

        # redraw
        if element.graphics:
            element.graphics.invalidate(element)
