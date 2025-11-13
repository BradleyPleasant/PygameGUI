# Graphics.py
from .Element import Element
from pygame import Surface, font
import pygame
import random

class Graphics:
    def __init__(self, background_color = None):
        self.surface: Surface|None = None
        self.background_color = background_color

    def draw(self, element: Element) -> Surface:
        return Surface((0, 0))

    def render(self, element: Element) -> Surface:
        if self.surface: return self.surface

        surface = self.draw(element)
        self.surface = Surface(element.size, pygame.SRCALPHA)

        # fill background
        color = self.background_color
        if not color:
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
        print(self.surface)
        self.surface.fill(color)
        print(self.surface)
        self.surface.blit(surface, (0, 0)) # TODO: align within element? Should this be in the layout?

        # render & blit children onto this surface
        for child in element.children:
            if child.graphics:
                child_surf = child.graphics.render(child)
                # blit at child's rect.topleft relative to parent surface
                self.surface.blit(child_surf, child.topleft)

        return self.surface

