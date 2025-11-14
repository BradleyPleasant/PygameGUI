# __init__.py
from .Element import Element
from .Layout import VerticalLayout
from .Graphics import Graphics
from .Input import Input
import pygame


class Application:
    def __init__(self, size: tuple[int, int] = (800, 600)):
        Element.app = self
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.elements: list[Element] = []
        self.selected = None
        self.cursor_capture = None

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if lowest := self.get_lowest_selectable_child(event.pos):
                        print(lowest)
                        if self.selected is lowest: self.selected = None
                        else: self.selected = lowest
                        lowest.input.on_mouse_button_down(lowest, event)
                    else: self.selected = None

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected:
                        self.selected.input.on_mouse_button_up(self.selected, event)
                    else:
                        if lowest := self.get_lowest_selectable_child(event.pos):
                            lowest.input.on_mouse_button_up(lowest, event)

                elif event.type == pygame.MOUSEMOTION:
                    if self.cursor_capture:
                        self.cursor_capture.input.on_mouse_motion(self.cursor_capture, event)
                    else:
                        if lowest := self.get_lowest_selectable_child(event.pos):
                            lowest.input.on_mouse_motion(lowest, event)

                elif event.type == pygame.KEYDOWN:
                    if self.selected:
                        self.selected.input.on_key_down(self.selected, event)

                elif event.type == pygame.KEYUP:
                    if self.selected:
                        self.selected.input.on_key_up(self.selected, event)

                elif event.type == pygame.TEXTINPUT:
                    if self.selected:
                        self.selected.input.on_text_input(self.selected, event)


            # layout pass: measure + arrange + recursive organize
            for element in self.elements:
                if element.layout:
                    # measure to compute sizes without mutating positions
                    measured = element.layout.measure(element)
                    element.min_size = measured
            for element in self.elements:
                if element.layout:
                    # arrange to set children positions and element.size
                    element.layout.arrange(element)

            # render pass
            for element in self.elements:
                # prefer renderer alias if present, otherwise graphics
                if element.graphics:
                    surface = element.graphics.render(element)
                    self.screen.blit(surface, element.topleft)

            pygame.display.flip()

    def get_lowest_selectable_child(self, pos: tuple[int, int]) -> Element|None:
        for element in self.elements:
            if lowest := element.get_lowest_element_at_pos(pos):
                if lowest_selectable := lowest.get_lowest_selectable_parent():
                    return lowest_selectable
