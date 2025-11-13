from ..Graphics import Graphics
from ..Element import Element
import pygame
from pygame import Surface


class Label(Graphics):
    def __init__(self, text: str, font_name: str|None = None, font_size: int = 22, background_color = None):
        super().__init__(background_color)
        self.text = text
        self.font = pygame.font.SysFont(font_name, font_size)
        self.color = (255, 255, 255)

    def draw(self, element: Element) -> Surface:
        return self.font.render(self.text, True, self.color)