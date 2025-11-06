from .Element import Element
from .Organizer import VerticalOrganizer
from .Renderer import Renderer
import pygame


class Application:
    def __init__(self, size: tuple[int, int] = (800, 600), title: str = "DynamicUI Application") -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.elements = list()
        self.running = True

    def add_element(self, element: Element):
        self.elements.append(element)

    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((30, 30, 30))
            for element in self.elements:
                element.organizer.measure(element)
                element.organizer.organize(element)
                self.screen.blit(element.renderer.render(element), element.rect.topleft)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()