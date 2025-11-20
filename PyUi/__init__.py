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
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.elements: list[Element] = []
        self.selected = None
        self.cursor_capture = None
        # snapshot control: optionally write first rendered frame to a PNG
        self._snapshot_done = False

    def run(self):
        # INITIAL LAYOUT PASS (fixes the “first frame wrong” issue)
        for element in self.elements:
            if element.layout:
                element.min_size = element.layout.measure(element)

        for element in self.elements:
            if element.layout:
                element.layout.arrange(element)

        while True:
            self.screen.fill((0, 0, 0))

            # reset the mouse cursor each frame
            if not self.get_lowest_selectable_child(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if lowest := self.get_lowest_selectable_child(event.pos):
                        if self.selected is lowest: self.selected = None
                        else: self.selected = lowest
                        lowest.input.on_mouse_button_down(lowest, event)
                    else: self.selected = None

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.selected:
                        self.selected.input.on_mouse_button_up(self.selected, event) # diable type checker pycharm
                    elif self.cursor_capture:
                        self.cursor_capture.input.on_mouse_button_up(self.cursor_capture, event)
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

            # clear graphics caches for elements changed by layout so we re-render composition
            for element in self.elements:
                self.invalidate_recursive(element)

            # render pass
            for element in self.elements:
                # prefer renderer alias if present, otherwise graphics
                if element.graphics:
                    surface = element.graphics.render(element)
                    # blit at the element's global position so nested parents are placed correctly
                    gx, gy = element.global_position()
                    self.screen.blit(surface, (int(gx), int(gy)))

            if self.selected:
                rect = self.selected.global_rect()
                pygame.draw.rect(self.screen, (255, 0, 0), rect, 2)

            pygame.display.flip()

    def get_lowest_selectable_child(self, pos: tuple[int, int]) -> Element|None:
        for element in self.elements:
            if lowest := element.get_lowest_element_at_pos(pos):
                if lowest_selectable := lowest.get_lowest_selectable_parent():
                    return lowest_selectable
        return None

    def invalidate_recursive(self, element: Element):
        if element.graphics:
            element.graphics.invalidate(element)
        for child in element.children:
            self.invalidate_recursive(child)
