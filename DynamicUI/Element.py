from pygame import FRect


class Element:  # Entity in ECS - decided to use UI term Element as this is a UI library
    UID_COUNTER = 0
    ELEMENTS = {}
    app = None

    def __init__(self, organizer, renderer, input_handler,
                 parent:"Element | None" = None, rect = None) -> None:
        """
        The Base Class for all UI Elements.

        - generates a unique ID for each element

        - holds reference to manager, layout, graphics, and input handlers

        - sets parent to child relationships

        - sets root element reference

        :param app: Manager
        :param parent: UIElement | None
        :param layout_handler: LayoutHandler
        :param graphics_handler: GraphicsHandler
        :param input_handler: InputHandler
        """
        self.rect = FRect(rect) if rect else FRect(0, 0, 0, 0)  # must be between the minimum and maximum bounds
        self.uid = Element.UID_COUNTER
        Element.UID_COUNTER += 1  # increment the counter for next UID
        self.children = []
        self.parent = parent
        Element.ELEMENTS[self.uid] = self
        self.root = self  # default root is self
        if parent:
            parent.children.append(self)  # automatically add to parent's children list
            self.root = parent.root # set root to parent's root
        self.organizer = organizer
        self.renderer = renderer
        self.input_handler = input_handler

    def add_child(self, child:"Element") -> None:
        """
        Add a child element to this element.

        :param child: UIElement - child element to add
        """
        child.parent = self
        self.children.append(child)
        child.root = self.root  # set child's root to this element's root

    def remove_child(self, child:"Element") -> None:
        """
        Remove a child element from this element.

        :param child: UIElement - child element to remove
        """
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            child.root = child  # reset child's root to itself

    def global_position(self):
        if self.parent:
            x, y = self.parent.global_position()
            return x + self.rect.x, y + self.rect.y
        return self.rect.x, self.rect.y

    def global_rect(self):
        return FRect(self.global_position(), self.rect.size)

    def get_lowest_element_at_pos(self, pos: tuple[float, float]) -> "Element | None":
        if not self.global_rect().collidepoint(pos):
            return None
        for child in reversed(self.children):
            result = child.get_lowest_element_at_pos(pos)
            if result:
                return result
        return self


    def get_lowest_selectable_parent(self) -> "Element | None":
        if self.input_handler:
            return self
        if self.parent:
            return self.parent.get_lowest_selectable_parent()
        return None