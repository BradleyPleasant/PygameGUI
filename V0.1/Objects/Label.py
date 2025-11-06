import pygame
from ..Object import UIObject


class Label(UIObject):
    def __init__(self, app, position: tuple[int, int] = (0, 0), size: tuple[int, int] = (50, 50), layout: "Layout" = None, color=None,
                 selectable=False, parent=None, text = "", font: pygame.font.Font = None, text_color=(0, 0, 0)):
        super().__init__(app, position, size, layout, color, selectable, parent)
        self.text = text
        self.font = font if font else pygame.font.SysFont(None, 24)
        self.text_color = text_color

    def update_size(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        padding = self.layout.padding if self.layout else 0
        self.rect.width = text_surface.get_width() + padding * 2
        self.rect.height = text_surface.get_height() + padding * 2

    def render(self):
        surface = super().render()
        text_surface = self.font.render(self.text, True, self.text_color)
        padding = self.layout.padding if self.layout else 0
        surface.blit(text_surface, (padding, padding))
        return surface

