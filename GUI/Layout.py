import pygame
from .Object import UIObject


class Layout:
    def __init__(self, padding: int = 0) -> None:
        self.padding = padding

    def apply(self, UI_object: UIObject):
        min_width, min_height = self.padding, self.padding
        for child in UI_object.children:
            if child.rect.top < self.padding:
                child.rect.y = self.padding
            if child.rect.left < self.padding:
                child.rect.x = self.padding
            if child.rect.right + self.padding > min_width:
                min_width = child.rect.right + self.padding
            if child.rect.bottom + self.padding > min_height:
                min_height = child.rect.bottom + self.padding
        UI_object.rect = pygame.Rect(UI_object.rect.x, UI_object.rect.y, max(min_width, UI_object.rect.width), max(min_height, UI_object.rect.height))
        return min_width, min_height


class VerticalLayout(Layout):
    def __init__(self, padding: int = 0, item_padding: int = 0) -> None:
        super().__init__(padding)
        self.item_padding = item_padding

    def apply(self, UI_object: UIObject):
        y = self.padding
        for child in UI_object.children:
            child_surface = child.render()
            child.rect.x = self.padding
            child.rect.y = y
            y += child_surface.get_height() + self.item_padding
        y -= self.item_padding
        y += self.padding
        min_width, min_height = super().apply(UI_object)
        for child in UI_object.children:
            child.rect.width = min_width - 2 * self.padding


class HorizontalLayout(Layout):
    def __init__(self, padding: int = 0, item_padding: int = 0) -> None:
        super().__init__(padding)
        self.item_padding = item_padding

    def apply(self, UI_object: UIObject):
        x = self.padding
        for child in UI_object.children:
            child_surface = child.render()
            child.rect.x = x
            child.rect.y = self.padding
            x += child_surface.get_width() + self.item_padding
        x -= self.item_padding
        x += self.padding
        min_width, min_height = super().apply(UI_object)
        for child in UI_object.children:
            child.rect.height = min_height - 2 * self.padding