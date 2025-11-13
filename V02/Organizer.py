from pygame import FRect
from .Element import Element


class Organizer:
    def __init__(self, element_padding: int = 0, children_padding: int = 0) -> None:
        self.element_padding = element_padding
        self.children_padding = children_padding
        self.minimum_size: tuple[float, float] = (0, 0)


class VerticalOrganizer(Organizer):
    def measure(self, element: "Element") -> tuple[float, float]:
        """Measure total size required for the element and its children."""
        min_width, min_height = 0, 0

        # Measure all children
        for child in element.children:
            width, height = child.organizer.measure(child)  # bottom-up recursion
            min_width = max(min_width, width)
            min_height += height + self.children_padding

        # If no children, ask renderer for intrinsic size
        if not element.children and element.renderer:
            width, height = element.renderer.measure_content(element)
            min_width, min_height = width, height

        # Add element padding
        min_width += 2 * self.element_padding
        min_height += 2 * self.element_padding
        if element.children:
            min_height -= self.children_padding  # remove trailing space

        # Cache for later
        self.minimum_size = (min_width, min_height)
        element.rect.size = (
            max(element.rect.width, min_width),
            max(element.rect.height, min_height)
        )

        return self.minimum_size

    def organize(self, element: "Element") -> None:
        """Position children within this element's rect."""
        x, y = self.element_padding, self.element_padding
        for child in element.children:
            w, h = child.rect.size
            w = element.rect.width - 2 * self.element_padding
            # Position child in a vertical stack
            child.rect.topleft = (x, y)
            child.rect.size = (w, h)
            y += h + self.children_padding
            child.organizer.measure(child)


class HorizontalOrganizer(Organizer):
    def measure(self, element: "Element") -> tuple[float, float]:
        """Measure total size required for the element and its children (left to right)."""
        min_width, min_height = 0, 0

        # Measure all children
        for child in element.children:
            width, height = child.organizer.measure(child)  # bottom-up recursion
            min_width += width + self.children_padding
            min_height = max(min_height, height)

        # If no children, ask renderer for intrinsic size
        if not element.children and element.renderer:
            width, height = element.renderer.measure_content(element)
            min_width, min_height = width, height

        # Add element padding
        min_width += 2 * self.element_padding
        min_height += 2 * self.element_padding
        if element.children:
            min_width -= self.children_padding  # remove trailing space

        # Cache for later
        self.minimum_size = (min_width, min_height)
        element.rect.size = (
            max(element.rect.width, min_width),
            max(element.rect.height, min_height)
        )

        return self.minimum_size

    def organize(self, element: "Element") -> None:
        """Position children within this element's rect (left to right)."""
        x, y = self.element_padding, self.element_padding
        for child in element.children:
            w, h = child.rect.size
            h = element.rect.height - 2 * self.element_padding
            # Position child in a horizontal row
            child.rect.topleft = (x, y)
            child.rect.size = (w, h)
            x += w + self.children_padding
            child.organizer.measure(child)
