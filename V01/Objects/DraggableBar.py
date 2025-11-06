import pygame
from ..Object import UIObject


class DraggableBar(UIObject):
    def __init__(self, app, position: tuple[int, int] = (0, 0), size: tuple[int, int] = (50, 50), layout: "Layout" = None, color=None,
                 selectable=True, parent=None):
        super().__init__(app, position, size, layout, color, selectable, parent)

    def handle_event(self, event: "pygame.event.Event") -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # check the event pos is inside the object's rect
                if self.rect.collidepoint(event.pos[0] - self.global_position()[0], event.pos[1] - self.global_position()[1]):
                    self.app.dragged_object = self
                    self.app.selected_object = self
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if self.app.dragged_object == self:
                    self.app.dragged_object = None
        elif event.type == pygame.MOUSEMOTION:
            if self.app.dragged_object == self:
                # get the highest parent:
                top_parent = self.get_top_parent()
                top_parent.rect.x += event.rel[0]
                top_parent.rect.y += event.rel[1]