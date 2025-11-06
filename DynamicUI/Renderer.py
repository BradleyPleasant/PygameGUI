import pygame
from .Element import Element


class Renderer:
    def __init__(self, background_color = (255, 255, 255)) -> None:
        self.background_color = background_color
        self.surface = None

    def measure_content(self, element: Element) -> tuple[float, float]:
        """Return width, height needed for the content (no rendering)."""
        if self.surface: return self.surface.get_size()
        return element.rect.size

    def render(self, element: Element) -> pygame.Surface:
        """Draw the element onto the given surface."""
        if self.surface: return self.surface
        self.surface = pygame.Surface(element.rect.size)
        self.surface.fill(self.background_color)
        for child in element.children:
            surface = child.renderer.render(child)
            self.surface.blit(surface, child.rect.topleft)
        return self.surface







