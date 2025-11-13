from .Element import Element
from .Organizer import VerticalOrganizer, HorizontalOrganizer
from .Renderer import Renderer
from .InputHandler import InputHandler

import pygame
pygame.init()
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP


class Application:
    def __init__(self, size: tuple[int, int] = (800, 600), title: str = "V02 Application") -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.elements = list()
        self.running = True
        self.selected = None
        self.dragging = None
        self.resizing = None
        self.clock = pygame.time.Clock()
        Element.app = self

    def add_element(self, element: Element):
        self.elements.append(element)

    def send_event_at_pos(self, event: pygame.event.Event, pos: tuple[int, int]) -> None:
        element = self.get_lowest_selectable_child(pos)
        if element: element.input_handler.handle_event(event, element)

    def get_lowest_selectable_child(self, pos: tuple[int, int]) -> Element|None:
        for element in self.elements:
            if lowest := element.get_lowest_element_at_pos(pos):
                if lowest_selectable := lowest.get_lowest_selectable_parent():
                    return lowest_selectable

    def run(self) -> None:
        while self.running:
            mouse_up_handled = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if lowest := self.get_lowest_selectable_child(event.pos):
                        if self.selected is lowest: self.selected = None
                        else: self.selected = lowest
                        lowest.input_handler.handle_event(event, lowest)
                    else: self.selected = None

                elif event.type == pygame.MOUSEBUTTONUP:
                    if not mouse_up_handled:
                        if self.selected:
                            self.selected.input_handler.handle_event(event, self.selected)
                            mouse_up_handled = True

                elif event.type == pygame.MOUSEMOTION:
                    for element in Element.ELEMENTS.values():
                        if element.input_handler:
                            element.input_handler.handle_event(event, element)



                elif event.type == pygame.KEYDOWN:
                    # send the event to the selected element
                    if self.selected: self.selected.input_handler.handle_event(event, self.selected)


            self.screen.fill((30, 30, 30))
            for element in self.elements:
                element.organizer.measure(element)
                element.organizer.organize(element)

                self.screen.blit(element.renderer.render(element), element.rect.topleft)
            # set caption to time elapsed since program start with pygame clock
            pygame.display.set_caption(f"V02 Application - {pygame.time.get_ticks() / 1000 :}s")

            pygame.draw.rect(self.screen, (200, 200, 200), self.selected.global_rect(), 3, border_radius=10) if self.selected else None
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
