# Element.py
import pygame

class Element(pygame.FRect):
    app = None

    def __init__(self, parent: "Element|None" = None, layout = None, graphics = None, input = None):
        # use a Rect instance on the element rather than subclassing it
        super().__init__(0, 0, 0, 0)
        self.min_size = (0, 0)
        self.parent = parent
        self.layout = layout
        self.graphics = graphics
        self.input = input
        self.children: list[Element] = []

        if self.parent:
            self.parent.children.append(self)

    def global_position(self):
        if self.parent:
            x, y = self.parent.global_position()
            return x + self.x, y + self.y
        return self.x, self.y

    def global_rect(self):
        return pygame.FRect(self.global_position(), self.size)

    def get_lowest_element_at_pos(self, pos: tuple[float, float]) -> "Element | None":
        if not self.global_rect().collidepoint(pos):
            return None
        for child in reversed(self.children):
            result = child.get_lowest_element_at_pos(pos)
            if result:
                return result
        return self


    def get_lowest_selectable_parent(self) -> "Element | None":
        if self.input:
            return self
        if self.parent:
            return self.parent.get_lowest_selectable_parent()
        return None

