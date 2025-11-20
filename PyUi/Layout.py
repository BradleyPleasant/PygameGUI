from .Element import Element


# python
class VerticalLayout:
    def __init__(self, element_padding: int = 5, child_padding: int = 2):
        self.element_padding = element_padding
        self.child_padding = child_padding

    def measure(self, element: Element) -> tuple[int, int]:
        # leaf element: measure from graphics if present
        if not element.children:
            if element.graphics:
                size = element.graphics.draw(element).get_size()
                # ensure ints
                element.min_size = (int(size[0]), int(size[1]))
                return element.min_size
            # empty element minimal size = paddings
            element.min_size = (self.element_padding * 2, self.element_padding * 2)
            return element.min_size

        max_w = 0
        y = self.element_padding
        for child in element.children:
            size = child.layout.measure(child) if child.layout else self.measure(child)
            max_w = max(max_w, size[0])
            y += size[1] + self.child_padding
        y -= self.child_padding
        measured = (max_w + self.element_padding * 2, y + self.element_padding)
        # store integer sizes
        element.min_size = (int(measured[0]), int(measured[1]))
        return element.min_size

    def arrange(self, element: Element) -> tuple[int, int]:
        # ensure element meets its measured minimum
        if hasattr(element, 'min_size'):
            if element.width < element.min_size[0]:
                element.width = element.min_size[0]
            if element.height < element.min_size[1]:
                element.height = element.min_size[1]

        total_height = sum(child.height for child in element.children)
        extra_space = element.height - total_height - (self.child_padding * (len(element.children) - 1)) - (self.element_padding * 2)

        # position children using local coordinates (child.x, child.y)
        y = self.element_padding
        for child in element.children:
            # ensure child meets its measured minimum
            if hasattr(child, 'min_size'):
                if child.width < child.min_size[0]:
                    child.width = child.min_size[0]
                if child.height < child.min_size[1]:
                    child.height = child.min_size[1]

            # place child relative to parent (local coords)
            child.x = self.element_padding
            child.y = y

            # make sure the childs width fills the parent minus paddings
            child.width = element.width - self.element_padding * 2

            if child.height > child.min_size[1] and extra_space < 0:
                # reduce child's height proportionally if there's not enough space
                reduction = min(child.height - child.min_size[1], -extra_space)
                child.height -= reduction
                extra_space += reduction

            # make sure child's size tuple is synced and integral
            try:
                child.size = (int(child.width), int(child.height))
            except Exception:
                child.size = (int(getattr(child, 'width', 0)), int(getattr(child, 'height', 0)))

            # recurse: use child's own layout if present, otherwise fall back
            if child.layout:
                child.layout.arrange(child)
            elif child.children:
                self.arrange(child)

            y += child.height + self.child_padding

        # ensure element.size is synced too
        try:
            element.size = (int(element.width), int(element.height))
        except Exception:
            element.size = (int(getattr(element, 'width', 0)), int(getattr(element, 'height', 0)))

        return int(element.width), int(element.height)
