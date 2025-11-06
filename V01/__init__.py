import pygame
from .Object import UIObject
from .Layout import Layout, VerticalLayout, HorizontalLayout
from .Objects.DraggableBar import DraggableBar
from .Objects.Label import Label

class Application:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.objects = list()
        self.dragged_object = None
        self.selected_object = None
        self.event_receivers = list()

    def send_event_at_pos(self, event: pygame.event.Event, pos: tuple[int, int]) -> None:
        for obj in self.objects:
            if obj.rect.collidepoint(pos):
                obj = obj.get_lowest_selectable_child_at_pos(pos)
                if obj is not self.dragged_object or obj is not self.selected_object:
                    if obj and obj.selectable:
                        print(obj)
                        obj.handle_event(event)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected_object = None
                    self.send_event_at_pos(event, event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.dragged_object:
                        self.dragged_object.handle_event(event)
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragged_object:
                        self.dragged_object.handle_event(event)
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.selected_object = None
                    if self.selected_object:
                        self.selected_object.handle_event(event)

            self.screen.fill((0, 255, 100))
            for root in self.objects:
                root_surface = root.render()
                self.screen.blit(root_surface, root.rect.topleft)

            if self.selected_object:
                pygame.draw.rect(self.screen, (255, 0, 0), self.selected_object.global_rect(), 3, border_radius=10)
            pygame.display.flip()

