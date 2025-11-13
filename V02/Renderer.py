import pygame
from .Element import Element


class Renderer:
    def __init__(self, background_color = None) -> None:
        self.background_color = background_color
        self.surface = None

    def measure_content(self, element: Element) -> tuple[float, float]:
        """Return width, height needed for the content (no rendering)."""
        if self.surface: return self.surface.get_size()
        return element.rect.size

    def render(self, element: Element) -> pygame.Surface:
        """Draw the element onto the given surface."""
        if self.surface: return self.surface
        self.surface = pygame.Surface(element.rect.size, pygame.SRCALPHA)
        self.surface.fill(self.background_color) if self.background_color else self.surface.fill((0, 0, 0, 0))
        for child in element.children:
            if not child.renderer: continue
            surface = child.renderer.render(child)
            self.surface.blit(surface, child.rect.topleft)
        return self.surface

    def calculate_placement_from_anchor(self, element: Element, content_size: tuple[int, int], anchor: str) -> pygame.Rect:
        rect = pygame.Rect(0, 0, *content_size)
        if anchor == "center":
            rect.center = (element.rect.width // 2, element.rect.height // 2)
        elif anchor == "topleft":
            rect.topleft = (0, 0)
        elif anchor == "topright":
            rect.topright = (element.rect.width, 0)
        elif anchor == "bottomleft":
            rect.bottomleft = (0, element.rect.height)
        elif anchor == "bottomright":
            rect.bottomright = (element.rect.width, element.rect.height)
        elif anchor == "midtop":
            rect.midtop = (element.rect.width // 2, 0)
        elif anchor == "midbottom":
            rect.midbottom = (element.rect.width // 2, element.rect.height)
        elif anchor == "midleft":
            rect.midleft = (0, element.rect.height // 2)
        elif anchor == "midright":
            rect.midright = (element.rect.width, element.rect.height // 2)
        return rect

    def invalidate(self, element: Element) -> None:
        """Invalidate cached surface."""
        self.surface = None
        if element.parent:
            element.parent.renderer.invalidate(element.parent)

