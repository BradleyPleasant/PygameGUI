import pygame


class UIObject:
    def __init__(self, app, position: tuple[int, int] = (0, 0), size: tuple[int, int] = (50, 50), layout: "Layout" = None, color=None,
                 selectable=False, parent=None) -> None:
        self.app = app
        self.rect = pygame.Rect(*position, *size)
        self.children = []
        self.layout = layout
        self.parent = parent
        self.surface_buffer = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.color = color
        self.selectable = selectable
        if color: self.surface_buffer.fill(color)

    def get_top_parent(self):
        if self.parent:
            return self.parent.get_top_parent()
        return self

    def get_lowest_selectable_child_at_pos(self, pos: tuple[int, int]) -> "UIObject | None":
        for child in reversed(self.children):
            child_global_pos = child.global_position()
            child_rect = pygame.Rect(child_global_pos[0], child_global_pos[1], child.rect.width, child.rect.height)
            if child_rect.collidepoint(pos):
                if child.selectable:
                    deeper_child = child.get_lowest_selectable_child_at_pos(pos)
                    if deeper_child:
                        return deeper_child
                    return child
        if self.selectable: return self
        return None

    def add_child(self, child: "UIObject") -> None:
        """Use this instead of .children.append(...) so parent is set automatically."""
        child.parent = self
        self.children.append(child)

    def remove_child(self, child: "UIObject") -> None:
        if child in self.children:
            self.children.remove(child)
            child.parent = None

    def global_position(self) -> tuple[int, int]:
        if self.parent:
            parent_x, parent_y = self.parent.global_position()
            return self.rect.x + parent_x, self.rect.y + parent_y
        return self.rect.x, self.rect.y

    def global_rect(self) -> pygame.Rect:
        """Single canonical rect in screen coordinates."""
        x, y = self.global_position()
        return pygame.Rect(x, y, self.rect.width, self.rect.height)

    # add cache
    def render(self) -> pygame.Surface:
        # Let children update their rect sizes before layout
        for child in self.children:
            if hasattr(child, "update_size"):
                child.update_size()

        # if not self.buffer_dirty: return self.surface_buffer
        if self.layout: self.layout.apply(self)
        surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        if self.color: pygame.draw.rect(surface, self.color, pygame.Rect(0, 0, self.rect.width, self.rect.height), border_radius=10)
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, self.rect.width, self.rect.height),2 , border_radius=10)
        for child in self.children:
            child_surface = child.render()
            child_pos = (child.rect.x, child.rect.y)
            surface.blit(child_surface, child_pos)
        self.surface_buffer = surface
        return self.surface_buffer

    def handle_event(self, event: pygame.event.Event) -> None:
        pass