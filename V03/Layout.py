# Layout Class Defines Behaviour to scale and position the children of the element
# It does this via the Upwards Pass on all children that will "measure" and cache
# their minimum size.
# It then does a downwards pass from parent to child that will "arrange" all the children
# by looking at how much space we can offer the children and the setting their positions
# and sizes.
from V03 import Element, Graphics


class VerticalLayout:
    def __init__(self, element_padding: int = 5, child_padding: int = 2):
        self.element_padding = element_padding
        self.child_padding = child_padding

    def measure(self, element: Element) -> tuple[int, int]:
        # if the element doesn't have children we have reached the bottom of the tree and should return our own size
        if not element.children:
            # return the size of the element
            if element.graphics:
                size = element.graphics.draw(element).get_size() # TODO: Do we need to return rect size if it's bigger?
                # cache the size
                element.min_size = size
                return size
            # if no Graphics then just return the padding * 2
            return self.element_padding * 2, self.child_padding * 2
        # if the element does have children we must work out our minimum size as if all the children were arranged
        x = 0
        y = self.element_padding
        for child in element.children:
            if not child.layout: size = self.measure(child)
            else: size = child.layout.measure(child)
            x = max(size[0], x) # use the maximum size
            y += size[1] + self.child_padding
        # we don't need to check if we have children or not as the guard clause handles that case
        y -= self.child_padding # we need to account for the trailing padding from the for loop
        return x + self.element_padding * 2, y + self.element_padding # calculate for our padding

    def arrange(self, element: Element) -> tuple[int, int]:
        # if the element is too small increases it's size to the minimum height.
        if element.width < element.min_size[0]: element.width = element.min_size[0]
        if element.height < element.min_size[1]: element.height = element.min_size[1]
        # start from the parent and arrange children vertically. Also expand them to fill their parent's width
        y = self.element_padding
        for child in element.children:
            # set the position of the element to the correct place relative to the element
            child.topleft = (self.element_padding, y)
            y +=  child.height + self.child_padding
            if child.layout: child.layout.arrange(child) # Perform the parent to child arrange pass by arranging children




