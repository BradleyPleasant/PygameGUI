from ..Graphics import Graphics
from ..Element import Element
import pygame
from pygame import Surface


class Label(Graphics):
    def __init__(self, text: str, font_name: str|None = None, font_size: int = 22, background_color = None):
        super().__init__(background_color)
        self.text = text
        self._font_name = font_name
        self._font_size = font_size
        self.font = None
        self.color = (255, 255, 255)

    def draw(self, element: Element) -> Surface:
        # lazy-init the pygame font (pygame.init() must be called first)
        if self.font is None:
            self.font = pygame.font.SysFont(self._font_name, self._font_size)
        return self.font.render(self.text, True, self.color)