from V02 import *
from V02.Objects.Draggable import DraggableInputHandler
from V02.Objects.Label import LabelRenderer, LabelInputHandler
from V02.Objects.Button import ButtonInputHandler
from V02.Objects.Resizable import ResizableInputHandler
from V02.Layout import VerticalLayout


app = Application()


root = Element(
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=Renderer(background_color=(70, 70, 200)),
    input_handler=None,
    rect=(20, 20, 0, 0)
)

child1 = Element(
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=LabelRenderer(text = "This is a child element inside the root element"),
    input_handler=ResizableInputHandler(),
    parent=root,
    rect=(0, 0, 0, 0)
)
child2 = Element(
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=LabelRenderer(text = "It is just a dataclass with an organizer, renderer, and event_handler", background_color=(20, 200, 20)),
    input_handler=ButtonInputHandler(),
    parent=root,
    rect=(0, 0, 0, 0)
)
child3 = Element(
    organizer=HorizontalOrganizer(element_padding=5, children_padding=5),
    renderer=Renderer(background_color=(20, 20, 200)),
    input_handler=ResizableInputHandler(),
    parent=root,
    rect=(0, 0, 0, 0)
); child4 = Element(
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=LabelRenderer(text="It let's you", anchor = "topright"),
    input_handler=LabelInputHandler(),
    parent=child3,
    rect=(0, 0, 0, 0)
); child5 = Element(
    organizer=VerticalOrganizer(element_padding=5, children_padding=5),
    renderer=LabelRenderer(text="Plug and Play!", anchor="midbottom"),
    input_handler=LabelInputHandler(),
    parent=child3,
    rect=(0, 0, 0, 0)
)

app.add_element(root)
app.run()