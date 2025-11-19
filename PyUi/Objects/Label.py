from ..Graphics import Graphics
from ..Element import Element
import pygame
from pygame import Surface


class Label(Graphics):
    def __init__(self, text: str, font_name: str|None = None, font_size: int = 22, background_color = None, padding: int = 3):
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
        surf = self.font.render(self.text, True, self.color)
        # add padding around the text
        padded_surf = Surface((surf.get_width() + 2 * 5, surf.get_height() + 2 * 5), pygame.SRCALPHA)
        if self.background_color is not None:
            padded_surf.fill(self.background_color)
        padded_surf.blit(surf, (5, 5))
        return padded_surf