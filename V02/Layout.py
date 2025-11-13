from .Element import Element
from pygame import Rect

class VerticalLayout:
    def __init__(self, padding: int = 5, item_padding: int = 2):
        self.padding = padding
        self.item_padding = item_padding

    def arrange(self, element: Element) -> tuple[int, int]:
        total_width = 0
        total_height = self.padding

        for child in element.children:
            child_w, child_h = child.organizer.measure(child)
            child.rect.topleft = (self.padding, total_height)
            total_height += child_h + self.item_padding
            total_width = max(total_width, child_w)

        if element.children:
            total_height -= self.item_padding  # remove last spacing

        return total_width + self.padding * 2, total_height + self.padding

    def measure(self, element: Element) -> tuple[int, int]:
        if element.children:
            return self.arrange(element)
        elif element.renderer:
            return element.renderer.measure_content(element)
        else:
            return (self.padding * 2, self.padding * 2)

    def organize(self, element: Element) -> None:
        for child in element.children:
            # stretch width to fill parent (minus padding)
            child.rect.width = element.rect.width - self.padding * 2
            # recursive layout for nested elements
            child.organizer.organize(child)
